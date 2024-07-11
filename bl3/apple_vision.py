from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class AppleVisionDetectFacesAsyncTaskBlueprintProxy(unreal.UObject):
    OnSuccess: Any
    OnFailure: Any
    FaceDetectionResult: FaceDetectionResult

    def CreateProxyObjectForDetectFaces(
        self, SourceImage: engine.Texture
    ) -> AppleVisionDetectFacesAsyncTaskBlueprintProxy: ...


class FaceDetectionResult:
    DetectedFaces: unreal.WrappedArray[DetectedFace]


class DetectedFeature:
    Confidence: float


class DetectedFeatureRegion(DetectedFeature):
    Points: unreal.WrappedArray[core_uobject.Vector2D]


class DetectedFace(DetectedFeatureRegion):
    BoundingBox: core_uobject.Box2D
    Features: unreal.WrappedArray[DetectedFaceFeature2D]
    FeatureRegions: unreal.WrappedArray[DetectedFaceFeatureRegion]


class DetectedFaceFeatureRegion(DetectedFeatureRegion):
    FeatureType: EDetectedFaceFeatureType


class DetectedFeature2D(DetectedFeature):
    BoundingBox: core_uobject.Box2D


class DetectedFaceFeature2D(DetectedFeature2D):
    FeatureType: EDetectedFaceFeatureType


class EDetectedFaceFeatureType(enum.Enum):
    FaceContour = 0
    InnerLips = 1
    LeftEyebrow = 2
    NoseCrest = 3
