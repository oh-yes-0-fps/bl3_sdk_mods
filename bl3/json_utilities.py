from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


class JsonUtilitiesDummyObject(unreal.UObject): ...


class JsonObjectWrapper:
    JsonString: str
