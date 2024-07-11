from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine
from . import gameplay_tags
from . import gbx_probes_core


class GbxProbesBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def ResolveGbxProbeId(
        self,
        InObj: unreal.UObject,
        InTag: gameplay_tags.GameplayTag,
        OutId: gbx_probes_core.GbxProbeId,
        IsValid: bool,
    ): ...
    def MakeProbeId(
        self, Class: str, Type: str, SubType: str, OutId: gbx_probes_core.GbxProbeId
    ): ...
    def IsValidId(self, ProbeId: gbx_probes_core.GbxProbeId, IsValid: bool): ...
    def IsTestProbeEnabled(
        self, ProbeId: gbx_probes_core.GbxProbeId, Test: str, IsEnabled: bool
    ): ...
    def IsTestEnabled(self, Test: str, IsEnabled: bool): ...
    def IsClassEnabled(self, Class: str, IsEnabled: bool): ...
    def FlushPendingTestProbes(self): ...
    def EmitTestProbeResultWithData(
        self,
        ProbeId: gbx_probes_core.GbxProbeId,
        Test: str,
        Result: gbx_probes_core.EGbxProbeResult,
        ExtraDataArray: unreal.WrappedArray[GbxProbeExtraData],
    ): ...
    def EmitTestProbeResult(
        self,
        ProbeId: gbx_probes_core.GbxProbeId,
        Test: str,
        Result: gbx_probes_core.EGbxProbeResult,
        ExtraData: str,
    ): ...


class GbxProbeExtraData:
    Name: str
    Value: str
