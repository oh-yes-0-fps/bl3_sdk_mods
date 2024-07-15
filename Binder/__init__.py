from __future__ import annotations

from argparse import Namespace
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Self, cast
import mods_base
from mods_base import command
from unrealsdk import find_all, find_class, unreal
import json

def pascal_case_to_snake_case(text: str) -> str:
    last_upper = False
    for i, char in enumerate(text):
        this_upper = char.isupper()
        if this_upper and last_upper:
            text = text[:i] + char.lower() + text[i + 1:]
        last_upper = this_upper
    return "".join(["_" + char.lower() if char.isupper() else char for char in text]).lstrip("_")

def is_valid_py_ident(ident: str) -> bool:
        WHITE_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_123456789"
        if ident[0].isdigit():
            return False
        for char in ident:
            if char not in WHITE_LIST:
                return False
        return True

def convert_to_valid_py_ident(ident: str) -> str:
    WHITE_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_123456789."
    if ident[0].isdigit():
        ident = f"_{ident}"
    return "".join([char if char in WHITE_LIST else "_" for char in ident])

def function_writer_v2(
        ident: str,
        return_type: str | None,
        args: list[tuple[str, str]],
        path: str
    ) -> str:
    return_type_str = f" -> {return_type}" if return_type else ""
    arg_str = ", ".join([f"{name}: {type}" for name, type in args])
    if len(args) == 0:
        call = f"def __call__(self){return_type_str}: ..."
    else:
        call = f"def __call__(self, {arg_str}){return_type_str}: ..."
    output = f"""
    class __{ident}(TypedUFunction, Protocol):
        @staticmethod
        def _path_name() -> str: return \"{path}\"
        {call}
        class Params(unreal.WrappedStruct):
        
"""
    output += "\n            ".join([f"{name}: {type}" for name, type in args])

    return output

def class_writer(ident: str, parent: str, fields: list[tuple[str, str]], functions: list[str], is_struct: bool) -> str:
    extra_parent = "TypedUStruct" if is_struct else "TypedUClass"
    ident = convert_to_valid_py_ident(ident)
    parent_str = f"({convert_to_valid_py_ident(parent)}, {extra_parent})" if parent \
        else f"({extra_parent})"
    if len(fields) == 0 and len(functions) == 0:
        return f"\nclass {ident}{parent_str}: ..."
    field_str = "\n".join([f"    {name}: {type}" for name, type in fields])
    function_str = "\n".join(functions)
    return f"\nclass {ident}{parent_str}:\n{field_str}\n{function_str}"


def enum_writer(ident: str, values: list[str]) -> str:
    def fix_none(value: str) -> str:
        if value == "None":
            return "None_"
        return value
    ident = convert_to_valid_py_ident(ident)
    if len(values) == 0:
        return f"\nclass {ident}(TypedUEnum, enum.Enum): ..."
    value_str = "\n".join([f"    {fix_none(name)} = {i}" for i, name in enumerate(values)])
    return f"\nclass {ident}(TypedUEnum, enum.Enum):\n{value_str}"

@dataclass(slots=True, frozen=True)
class TyPath:
    name: str
    package: str

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "package": self.package,
        }

    def resolve_package(self) -> str:
        if self.package == "python":
            return ""
        if self.package.startswith("/Script/"):
            return pascal_case_to_snake_case(self.package[8:].replace("/", ""))
        return "bp"

    def py_type(self) -> str:
        text = self.name
        if text == "Object":
            return "unreal.UObject"
        elif text == "Class":
            return "unreal.UClass"
        elif text == "Struct":
            return "unreal.UStruct"
        elif text == "Enum":
            return "unreal.UEnum"
        package = self.resolve_package()
        if len(package) > 0:
            return f"{package}.{text}"
        return text

    def is_valid_py_ident(self) -> bool:
        return is_valid_py_ident(self.name)

    @staticmethod
    def from_json(data: dict) -> TyPath:
        return TyPath(
            name=data["name"],
            package=data["package"],
        )

    @staticmethod
    def from_unreal(obj: unreal.UObject) -> TyPath:
        outer = obj.Outer
        return TyPath(obj.Name, outer.Name if outer else "")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TyPath):
            return False
        return self.name == other.name and self.package == other.package

    def __hash__(self) -> int:
        return hash((self.name, self.package))


class TyGenericTemplates(Enum):
    Array = "WrappedArray"
    Set = "Set"
    Map = "Map"
    SubclassOf = "type"
    SoftClassPtr = "SoftClassPtr"
    SoftObjectPtr = "SoftObjectPtr"
    WeakObjectPtr = "WeakObjectPtr"
    EnumAsByte = "EnumAsByte"


@dataclass(slots=True, frozen=True)
class TyGenericPath(TyPath):
    template: TyGenericTemplates

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "package": self.package,
            "template": self.template.value,
        }

    def py_type(self) -> str:
        text = TyPath.py_type(self)
        if self.template == TyGenericTemplates.Array:
            return f"unreal.WrappedArray[{text}]"
        elif self.template == TyGenericTemplates.SubclassOf:
            return f"type[{text}]"
        return text

    @staticmethod
    def from_json(data: dict) -> TyGenericPath:
        return TyGenericPath(
            name=data["name"],
            package=data["package"],
            template=TyGenericTemplates(data["template"]),
        )

    @staticmethod
    def from_unreal(obj: unreal.UObject, template: TyGenericTemplates) -> TyGenericPath:
        return TyGenericPath(obj.Name, obj.Outer.Name if obj.Outer else "", template)


@dataclass(slots=True, frozen=True)
class TyStruct(TyPath):
    parent: Self | None
    properties: list[TyProperty]

    def to_json(self) -> dict:
        return {
            "type": "struct",
            "name": self.name,
            "package": self.package,
            "parent": TyPath.to_json(self.parent) if self.parent else None,
            "fields": [f.to_json() for f in self.properties],
        }

    def valid_properties(self) -> list[TyProperty]:
        return [prop for prop in self.properties if prop.is_valid_py()]

    def invalid_properties(self) -> list[TyProperty]:
        return [prop for prop in self.properties if not prop.is_valid_py()]

    def get_parents(self) -> list[Self]:
        parents = []
        current = self
        while current.parent:
            parents.append(current.parent)
            current = current.parent
        return parents

    @staticmethod
    def from_json(data: dict) -> TyStruct:
        return TyStruct(
            name=data["name"],
            package=data["package"],
            parent=TyStruct.from_json(data["parent"]) if data["parent"] else None,
            properties=[TyProperty.from_json(f) for f in data["fields"]],
        )

    @staticmethod
    def get_or_create(unreal_struct: unreal.UStruct) -> TyStruct:
        name = unreal_struct.Name
        package = unreal_struct.Outer.Name if unreal_struct.Outer else ""

        equal_struct = TyStruct(name, package, None, [])
        if equal_struct in DATA_BASE.types:
            return DATA_BASE.types[equal_struct] # type: ignore
        else:
            parent = None
            super_fields = list(unreal_struct._superfields())
            if len(super_fields) > 1:
                parent = TyStruct.get_or_create(super_fields[1])

            properties = []
            for field in unreal_struct._fields():
                if isinstance(field, unreal.UProperty):
                    prop = TyProperty.create(cast(unreal.UProperty, field))
                    if parent and prop in parent.properties:
                        break
                    properties.append(prop)

            new_struct = TyStruct(name, package, parent, properties)
            DATA_BASE.types[new_struct] = new_struct
            return new_struct

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TyPath):
            return False
        return self.name == other.name and self.package == other.package

    def __hash__(self) -> int:
        return hash((self.name, self.package))


@dataclass(slots=True, frozen=True)
class TyClass(TyStruct):
    functions: list[TyFunction]
    blueprint_generated: bool

    def to_json(self) -> dict:
        return {
            "type": "class",
            "name": self.name,
            "package": self.package,
            "parent": TyPath.to_json(self.parent) if self.parent else None,
            "fields": [f.to_json() for f in self.properties],
            "functions": [f.to_json() for f in self.functions],
            "blueprint_generated": self.blueprint_generated,
        }

    def valid_functions(self) -> list[TyFunction]:
        return [func for func in self.functions if func.is_valid_py()]

    @staticmethod
    def from_json(data: dict) -> TyClass:
        return TyClass(
            name=data["name"],
            package=data["package"],
            parent=TyClass.from_json(data["parent"]) if data["parent"] else None,
            properties=[TyProperty.from_json(f) for f in data["fields"]],
            functions=[TyFunction.from_json(f) for f in data["functions"]],
            blueprint_generated=data["blueprint_generated"],
        )

    @staticmethod
    def get_or_create(unreal_class: unreal.UClass) -> TyClass:
        name = unreal_class.Name
        package = unreal_class.Outer.Name if unreal_class.Outer else ""

        equal_class = TyClass(name, package, None, [], [], False)
        if equal_class in DATA_BASE.types:
            return DATA_BASE.types[equal_class] # type: ignore

        parent = None
        super_fields = list(unreal_class._superfields())
        if len(super_fields) > 1:
            parent = TyClass.get_or_create(cast(unreal.UClass, super_fields[1]))

        parent_props = []
        parent_funcs = []
        if parent:
            parents = parent.get_parents() + [parent]
            for p in parents:
                parent_props += p.properties
                parent_funcs += p.functions

        functions = []
        properties = []
        for field in unreal_class._fields():
            if isinstance(field, unreal.UProperty):
                prop = TyProperty.create(cast(unreal.UProperty, field))
                if prop in parent_props:
                    break
                properties.append(prop)
        for field in unreal_class._fields():
            if isinstance(field, unreal.UFunction):
                func = TyFunction.create(cast(unreal.UFunction, field))
                if func in parent_funcs:
                    break
                functions.append(func)

        new_class = TyClass(name, package, parent, properties, functions, isinstance(unreal_class, unreal.UBlueprintGeneratedClass))
        DATA_BASE.types[new_class] = new_class
        return new_class

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TyPath):
            return False
        return self.name == other.name and self.package == other.package

    def __hash__(self) -> int:
        return hash((self.name, self.package))


@dataclass(slots=True, frozen=True)
class TyProperty:
    name: str
    type: TyPath

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "type": self.type.to_json(),
        }

    def is_valid_py(self) -> bool:
        return self.type.is_valid_py_ident() and is_valid_py_ident(self.name)

    @staticmethod
    def from_json(data: dict) -> TyProperty:
        return TyProperty(
            name=data["name"],
            type=TyStruct.from_json(data["type"]),
        )

    @staticmethod
    def create(unreal_property: unreal.UProperty) -> TyProperty:
        name = unreal_property.Name
        if isinstance(unreal_property, unreal.UStructProperty):
            prop_type = TyPath.from_unreal(
                cast(unreal.UStructProperty, unreal_property).Struct
            )
        elif isinstance(unreal_property, unreal.UObjectProperty):
            cls = cast(unreal.UObjectProperty, unreal_property).PropertyClass
            if cls:
                prop_type = TyPath.from_unreal(cls)
            else:
                prop_type = TyPath("Any", "python")
        elif isinstance(unreal_property, unreal.UEnumProperty):
            prop_type = TyPath.from_unreal(
                cast(unreal.UEnumProperty, unreal_property).Enum
            )
        elif isinstance(unreal_property, unreal.UArrayProperty):
            inner_type = TyProperty.create(cast(unreal.UArrayProperty, unreal_property).Inner).type
            prop_type = TyGenericPath(
                inner_type.name,
                inner_type.package,
                TyGenericTemplates.Array,
            )
        elif isinstance(unreal_property, unreal.UBoolProperty):
            prop_type = TyPath("bool", "python")
        elif isinstance(unreal_property, unreal.UFloatProperty):
            prop_type = TyPath("float", "python")
        elif isinstance(unreal_property, unreal.UDoubleProperty):
            prop_type = TyPath("float", "python")
        elif isinstance(unreal_property, unreal.UByteProperty):
            prop_type = TyPath("int", "python")
        elif isinstance(unreal_property, unreal.UIntProperty):
            prop_type = TyPath("int", "python")
        elif isinstance(unreal_property, unreal.UUInt64Property):
            prop_type = TyPath("int", "python")
        elif isinstance(unreal_property, unreal.UUInt32Property):
            prop_type = TyPath("int", "python")
        elif isinstance(unreal_property, unreal.UUInt16Property):
            prop_type = TyPath("int", "python")
        elif isinstance(unreal_property, unreal.UInt64Property):
            prop_type = TyPath("int", "python")
        elif isinstance(unreal_property, unreal.UInt16Property):
            prop_type = TyPath("int", "python")
        elif isinstance(unreal_property, unreal.UInt8Property):
            prop_type = TyPath("int", "python")
        elif isinstance(unreal_property, unreal.UClassProperty):
            prop_type = TyGenericPath.from_unreal(
                cast(unreal.UClassProperty, unreal_property).MetaClass,
                TyGenericTemplates.SubclassOf,
            )
        elif isinstance(unreal_property, unreal.UNameProperty):
            prop_type = TyPath("str", "python")
        elif isinstance(unreal_property, unreal.UTextProperty):
            prop_type = TyPath("str", "python")
        elif isinstance(unreal_property, unreal.UStrProperty):
            prop_type = TyPath("str", "python")
        else:
            prop_type = TyPath("Any", "python")
        return TyProperty(name, prop_type)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TyProperty):
            return False
        return self.name == other.name and self.type == other.type

    def __hash__(self) -> int:
        return hash((self.name, self.type))


@dataclass(slots=True, frozen=True)
class TyFunction:
    name: str
    return_type: TyProperty | None
    params: list[TyProperty]

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "return_type": self.return_type.to_json() if self.return_type else None,
            "params": [p.to_json() for p in self.params],
        }

    def is_valid_py(self) -> bool:
        if self.return_type and not self.return_type.is_valid_py():
            return False
        for param in self.params:
            if not param.is_valid_py():
                return False
        return is_valid_py_ident(self.name)

    @staticmethod
    def from_json(data: dict) -> TyFunction:
        return TyFunction(
            name=data["name"],
            return_type=(
                TyProperty.from_json(data["return_type"])
                if data["return_type"]
                else None
            ),
            params=[TyProperty.from_json(p) for p in data["params"]],
        )

    @staticmethod
    def create(unreal_function: unreal.UFunction) -> TyFunction:
        PARAM_PREFIX_BLACKLIST = ["Temp_struct", "CallFunc", "K2Node", "ReturnValue", "Return"]
        name = unreal_function.Name
        return_type = None
        if unreal_function._find_return_param():
            return_type = TyProperty.create(
                cast(unreal.UProperty, unreal_function._find_return_param())
            )
        params = []
        for param in list(unreal_function._superfields())[-1]._fields():
            if isinstance(param, unreal.UProperty):
                for prefix in PARAM_PREFIX_BLACKLIST:
                    if param.Name.startswith(prefix):
                        break
                else:
                    params.append(TyProperty.create(cast(unreal.UProperty, param)))

        return TyFunction(name, return_type, params)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TyFunction):
            return False
        return self.name == other.name and self.return_type == other.return_type and self.params == other.params

    def __hash__(self) -> int:
        return hash((self.name, self.return_type, tuple(self.params)))


@dataclass(slots=True, frozen=True)
class TyEnum(TyPath):
    values: list[str]

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "package": self.package,
            "values": self.values,
        }

    @staticmethod
    def from_json(data: dict) -> TyEnum:
        return TyEnum(
            name=data["name"],
            package=data["package"],
            values=data["values"],
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TyPath):
            return False
        return self.name == other.name and self.package == other.package

    def __hash__(self) -> int:
        return hash((self.name, self.package))


@dataclass
class TypingDatabase:
    types: dict[TyPath, TyStruct | TyClass | TyEnum]

    def to_json(self) -> dict:
        return {
            "types": [t.to_json() for t in self.types]
        }

    def clear(self) -> None:
        self.types.clear()

@dataclass
class TyPackageOrganizer:
    packages: dict[str, str]

    def add_to_package(self, package: str, cls: str) -> None:
        old = self.packages.get(package, "")
        old += f"\n{cls}\n"
        self.packages[package] = old

    def make_modules(self) -> None:
        suffix = "py"
        alpha = \
"""from __future__ import annotations # type: ignore
from unrealsdk import unreal
from typing import Any, Protocol, override
import enum

from . import (
    TypedUStruct,
    TypedUClass,
    TypedUEnum,
    TypedUFunction,
    FuncProxy
)

"""
        for package, content in self.packages.items():
            with open(get_ouput_path(f"{package}.{suffix}"), "w") as f:
                beta = alpha
                for other_package in self.packages.keys():
                    if other_package != package and f"{other_package}." in content:
                        beta += f"from . import {other_package}\n"
                beta += "\n"
                f.write(beta)
                f.write(content.replace(f"{package}.", ""))
        with open(get_ouput_path(f"__init__.{suffix}"), "w") as f:
            f.write("\n".join([f"from . import {package}" for package in self.packages.keys()]))
            f.write("\n")
            f.write("__all__: tuple[str, ...] = (\n")
            for package in self.packages.keys():
                f.write(f"    \"{package}\",\n")
            f.write(")")
            f.write(
"""

import mods_base
import unrealsdk
import typing
from abc import ABC, abstractmethod

class TypedUStruct(ABC):
    @classmethod
    def ustruct(cls) -> unrealsdk.unreal.UStruct:
        return unrealsdk.find_object(unrealsdk.unreal.UStruct.Class, cls._path_name()) # type: ignore

    @abstractmethod
    @staticmethod
    def _path_name() -> str:
        raise NotImplementedError

class TypedUClass(ABC):
    @classmethod
    def uclass(cls) -> unrealsdk.unreal.UClass:
        return unrealsdk.find_class(cls._path_name(), True)

    @abstractmethod
    @staticmethod
    def _path_name() -> str:
        raise NotImplementedError

class TypedUFunction(typing.Protocol):
    @classmethod
    def ufunction(cls) -> unrealsdk.unreal.UFunction:
        path = cls._path_name().split(":")
        return unrealsdk.find_class(path[0], True)._find(path[1]) # type: ignore

    @abstractmethod
    @staticmethod
    def _path_name() -> str:
        raise NotImplementedError

class TypedUEnum(enum.Enum):
    @classmethod
    def uenum(cls) -> unrealsdk.unreal.UEnum:
        return unrealsdk.find_enum(cls._path_name(), True) # type: ignore

    @abstractmethod
    @staticmethod
    def _path_name() -> str:
        raise NotImplementedError

class StaticUFunctionCallError(NotImplementedError):
    pass

@dataclass
class FuncProxy:
    path: str
    Params: type[typing.Any] = unrealsdk.unreal.WrappedStruct

    def _path_name(self) -> str:
        return self.path

    def __call__(self, *args, **kwargs) -> typing.Never:
        raise StaticUFunctionCallError

    @classmethod
    def ufunction(cls) -> unrealsdk.unreal.UFunction:
        raise StaticUFunctionCallError

def get_pc() -> bp.BPCont_Player_C:
    return typing.cast(bp.BPCont_Player_C, mods_base.get_pc())

def find_object[T: TypedUClass](cls: type[T], name: str) -> T:
    return typing.cast(T, unrealsdk.find_object(cls.uclass(), name))

def find_all[T: TypedUClass](cls: type[T], exact: bool = True) -> typing.Iterator[T]:
    return typing.cast(typing.Iterator[T], unrealsdk.find_all(cls.uclass(), exact))

mods_base.build_mod(
    mod_type=mods_base.ModType.Library,
    cls=mods_base.Library,
    auto_enable=True,
)
"""
            )


DATA_BASE: TypingDatabase = TypingDatabase({})


def get_ouput_path(file: str) -> str:
    root = Path(__file__).parent
    output_dir = root / "bl3"
    if not output_dir.exists():
        output_dir.mkdir()
    return str(output_dir / file)


def get_all_structs() -> list[unreal.UStruct]:
    struct = find_class("Struct")
    return list(find_all(struct, False))  # type: ignore


def get_all_enums() -> list[unreal.UEnum]:
    struct = find_class("Enum")
    return list(find_all(struct, False))  # type: ignore


def get_parents(obj: unreal.UStruct) -> list[unreal.UStruct]:
    return list(obj._superfields())[1:]


def is_class(obj: unreal.UStruct) -> bool:
    return isinstance(obj, unreal.UClass)


def is_function(obj: unreal.UStruct) -> bool:
    return isinstance(obj, unreal.UFunction)


import timeit

@command()
def bind(_: Namespace) -> None:
    DATA_BASE.clear()

    def search_and_parse():
        for struct in get_all_structs():
            if is_class(struct):
                obj = TyClass.get_or_create(cast(unreal.UClass, struct))
            elif is_function(struct):
                continue
            else:
                obj = TyStruct.get_or_create(struct)
            DATA_BASE.types[obj] = obj
        for enum in get_all_enums():
            obj = TyEnum(enum.Name, enum.Outer.Name if enum.Outer else "", enum._as_py()._member_names_)
            DATA_BASE.types[obj] = obj

    def debug_write_out():
        with open(get_ouput_path("types.json"), "w") as f:
            f.write(json.dumps(DATA_BASE.to_json(), indent=4))

    def write_pyi():
        packages = TyPackageOrganizer({})
        for obj in DATA_BASE.types.values():
            if isinstance(obj, TyClass):
                packages.add_to_package(
                    obj.resolve_package(),
                    class_writer(
                        obj.name,
                        obj.parent.py_type() if obj.parent else "",
                        [(p.name, p.type.py_type()) for p in obj.valid_properties()],
                        [
                            function_writer_v2(
                                f.name,
                                f.return_type.type.py_type() if f.return_type else None,
                                [(p.name, p.type.py_type()) for p in f.params],
                                f"{obj.package}.{obj.name}:{f.name}"
                            ) for f in obj.valid_functions()
                        ],
                        False
                    )
                )
            elif isinstance(obj, TyStruct):
                packages.add_to_package(
                    obj.resolve_package(),
                    class_writer(
                        obj.name,
                        obj.parent.py_type() if obj.parent else "",
                        [(p.name, p.type.py_type()) for p in obj.valid_properties()],
                        [],
                        True
                    )
                )
            elif isinstance(obj, TyEnum):
                packages.add_to_package(
                    obj.resolve_package(),
                    enum_writer(
                        obj.name,
                        obj.values
                    )
                )

        packages.make_modules()

    print(timeit.timeit(search_and_parse, number=1))
    # print(timeit.timeit(debug_write_out, number=1))
    print(timeit.timeit(write_pyi, number=1))

@command()
def binds_available(_: Namespace) -> None:
    print(f"Available binds: {len(get_all_structs())}")


mods_base.build_mod(mod_type=mods_base.ModType.Library)
