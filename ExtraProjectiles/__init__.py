
from typing import Any, List, cast
from unrealsdk import find_all, hooks, find_object
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, UFunction
from mods_base import build_mod, command
from bl3.gbx_weapon import LightProjectileData

HOOKS_TO_DISABLE: List[str] = []

def OnDamage(caller: UObject, params: WrappedStruct, _3: Any, _4: BoundFunction):
    cast(LightProjectileData, caller).bCallOnDamageEventOncePerHit = False
    data = params.Projectile.Data
    if data:
        data.bCallOnDamageEventOncePerHit = False

def is_subfunc_of(func: UFunction, parent: UFunction) -> bool:
    super_funcs = func._superfields()
    for super_func in super_funcs:
        if super_func._path_name() == parent._path_name():
            return True
    return False

PARENT = cast(UFunction, find_object("Function", "/Script/GbxWeapon.LightProjectileData:OnDamage"))

def on_enable():
    hooks.add_hook(PARENT._path_name(), hooks.Type.PRE, PARENT._path_name() + "_hook", OnDamage)
    for obj in find_all("Function", False):
        func = cast(UFunction, obj)
        if func.Name == "OnDamage":
            if func._inherits(PARENT):
                name = func._path_name()
                HOOKS_TO_DISABLE.append(name)
                hooks.remove_hook(name, hooks.Type.PRE, name + "_hook")
                hooks.add_hook(name, hooks.Type.PRE, name + "_hook", OnDamage)

def on_disable():
    hooks.remove_hook(PARENT._path_name(), hooks.Type.PRE, PARENT._path_name() + "_hook")
    for name in HOOKS_TO_DISABLE:
        hooks.remove_hook(name, hooks.Type.PRE, name + "_hook")

@command()
def ExtraProjectilesDebug(_):
    for hook in HOOKS_TO_DISABLE:
        print(hook)

build_mod(
    auto_enable=True
)
