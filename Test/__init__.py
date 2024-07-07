from mods_base import build_mod, ModType
from thoth import periodic

# @periodic(1.0, real_time=True, auto_enabled=True)
# def test_callback(delta: float):
#     print(f"Time: {delta}")

build_mod(
    mod_type=ModType.Library,
    auto_enable=True,
)