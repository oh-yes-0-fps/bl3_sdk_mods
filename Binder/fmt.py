def convert_to_valid_py_ident(ident: str) -> str:
    WHITE_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_123456789."
    if ident[0].isdigit():
        ident = f"_{ident}"
    return "".join([char if char in WHITE_LIST else "_" for char in ident])




def function_writer(
    ident: str, return_type: str | None, args: list[tuple[str, str]], path: str
) -> str:
    return_type_str = f" -> {return_type}" if return_type else ""
    arg_str = ", ".join([f"{name}: {type} | None" for name, type in args])
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
    if len(args) == 0:
        output += "pass"
    else:
        output += "\n            ".join([f"{name}: {type} | None" for name, type in args])
    output += "\n"
    output += f"    {ident}: __{ident} = FuncProxy(__{ident}._path_name())\n"

    return output


def class_writer(
    package: str,
    ident: str,
    parent: str,
    fields: list[tuple[str, str]],
    functions: list[str],
    is_struct: bool,
) -> str:
    extra_parent = "TypedUStruct" if is_struct else "TypedUClass"
    ident = convert_to_valid_py_ident(ident)
    parent_str = (
        f"({convert_to_valid_py_ident(parent)}, {extra_parent})"
        if parent
        else f"({extra_parent})"
    )
    if len(fields) == 0 and len(functions) == 0:
        return f"\nclass {ident}{parent_str}: ..."
    field_str = "\n".join([f"    {name}: {type}" for name, type in fields])
    function_str = "\n".join(functions)
    return f"""
class {ident}{parent_str}:
    @staticmethod
    def _path_name() -> str: return "{package}.{ident}"
{field_str}
{function_str}


"""






def enum_writer(ident: str, values: list[str]) -> str:
    def fix_none(value: str) -> str:
        if value == "None":
            return "None_"
        return value

    ident = convert_to_valid_py_ident(ident)
    if len(values) == 0:
        return f"\nclass {ident}(TypedUEnum, enum.Enum): ..."
    value_str = "\n".join(
        [f"    {fix_none(name)} = {i}" for i, name in enumerate(values)]
    )
    return f"\nclass {ident}(TypedUEnum, enum.Enum):\n{value_str}"
