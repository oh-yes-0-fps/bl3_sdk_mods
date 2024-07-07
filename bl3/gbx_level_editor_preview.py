from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import engine



class GbxLevelEditorPreviewComponent(engine.SceneComponent):
    Definition: GbxLevelEditorPreviewDefinition
    InstanceData: GbxLevelEditorPreviewInstanceData
    CachedInstanceNamePrefix: str



class GbxLevelEditorPreviewDefinition(unreal.UObject):
    PreviewTitle: str



class GbxLevelEditorPreviewAnimation(GbxLevelEditorPreviewDefinition):
    DescriptorList: unreal.WrappedArray[PreviewAnimationDescriptor]



class GbxLevelEditorPreviewSettings(engine.DeveloperSettings):
    AllowLevelEditorPreviewComponent: bool



class GbxLevelEditorPreviewInstanceData: ...


class PreviewAnimationDescriptor:
    Title: str
    SkeletalMesh: engine.SkeletalMesh
    Animation: engine.AnimationAsset

