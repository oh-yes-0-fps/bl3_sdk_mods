from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine


class EnumerateTelemetryCommandlet(engine.Commandlet): ...


class SparkBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def PostLeviathanEventWithAttribute(
        self,
        PlayerController: engine.PlayerController,
        EventName: str,
        AttributeName: str,
        AttributeValue: str,
    ): ...
    def PostLeviathanEvent(
        self, PlayerController: engine.PlayerController, EventName: str
    ): ...
