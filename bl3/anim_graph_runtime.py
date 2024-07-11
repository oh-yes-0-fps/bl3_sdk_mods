from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import animation_core


class AnimCustomInstance(engine.AnimInstance): ...


class AnimNotify_PlayMontageNotify(engine.AnimNotify):
    NotifyName: str


class AnimNotify_PlayMontageNotifyWindow(engine.AnimNotifyState):
    NotifyName: str


class AnimSequencerInstance(AnimCustomInstance): ...


class KismetAnimationLibrary(engine.BlueprintFunctionLibrary):

    def K2_TwoBoneIK(
        self,
        RootPos: core_uobject.Vector,
        JointPos: core_uobject.Vector,
        EndPos: core_uobject.Vector,
        JointTarget: core_uobject.Vector,
        Effector: core_uobject.Vector,
        OutJointPos: core_uobject.Vector,
        OutEndPos: core_uobject.Vector,
        bAllowStretching: bool,
        StartStretchRatio: float,
        MaxStretchScale: float,
    ): ...
    def K2_LookAt(
        self,
        CurrentTransform: core_uobject.Transform,
        TargetPosition: core_uobject.Vector,
        LookAtVector: core_uobject.Vector,
        bUseUpVector: bool,
        UpVector: core_uobject.Vector,
        ClampConeInDegree: float,
    ) -> core_uobject.Transform: ...


class PlayMontageCallbackProxy(unreal.UObject):
    OnCompleted: Any
    OnBlendOut: Any
    OnInterrupted: Any
    OnNotifyBegin: Any
    OnNotifyEnd: Any

    def OnNotifyEndReceived(
        self,
        NotifyName: str,
        BranchingPointNotifyPayload: engine.BranchingPointNotifyPayload,
    ): ...
    def OnNotifyBeginReceived(
        self,
        NotifyName: str,
        BranchingPointNotifyPayload: engine.BranchingPointNotifyPayload,
    ): ...
    def OnMontageEnded(self, Montage: engine.AnimMontage, bInterrupted: bool): ...
    def OnMontageBlendingOut(self, Montage: engine.AnimMontage, bInterrupted: bool): ...
    def CreateProxyObjectForPlayMontage(
        self,
        InSkeletalMeshComponent: engine.SkeletalMeshComponent,
        MontageToPlay: engine.AnimMontage,
        PlayRate: float,
        StartingPosition: float,
        StartingSection: str,
    ) -> PlayMontageCallbackProxy: ...


class AnimNode_SkeletalControlBase(engine.AnimNode_Base):
    ComponentPose: engine.ComponentSpacePoseLink
    LODThreshold: int
    ActualAlpha: float
    AlphaInputType: engine.EAnimAlphaInputType
    Alpha: float
    AlphaScaleBias: engine.InputScaleBias
    bAlphaBoolEnabled: bool
    AlphaBoolBlend: engine.InputAlphaBoolBlend
    AlphaCurveName: str
    AlphaScaleBiasClamp: engine.InputScaleBiasClamp
    LODInterpolationSpeed: float
    bBoolAlpha: bool
    bInvertAlpha: bool
    ScreenSizeThreshold: ScreenSizeSelection
    bUseScreenSizeThreshold: bool


class ScreenSizeSelection:
    Selection: EScreenSizeSelection
    Preset: str
    ScreenSize: float


class AnimNode_BlendSpacePlayer(engine.AnimNode_AssetPlayerBase):
    X: float
    Y: float
    Z: float
    PlayRate: float
    bLoop: bool
    StartPosition: float
    BlendSpace: engine.BlendSpaceBase
    bResetPlayTimeWhenBlendSpaceChanges: bool
    BlendFilter: engine.BlendFilter
    BlendSampleDataCache: unreal.WrappedArray[engine.BlendSampleData]
    PreviousBlendSpace: engine.BlendSpaceBase
    bUseRateScaleSpeed: bool
    RateScaleSpeed: float
    GaitScalingData: engine.NodeGaitScalingData
    SpeedBlendspaceAxis: int
    bCalcStartPositionFromCurrentPose: bool


class AnimNode_AimOffsetLookAt(AnimNode_BlendSpacePlayer):
    BasePose: engine.PoseLink
    LODThreshold: int
    bIsLODEnabled: bool
    LookAtLocation: core_uobject.Vector
    SourceSocketName: str
    PivotSocketName: str
    SocketAxis: core_uobject.Vector
    Alpha: float
    SocketBoneReference: engine.BoneReference
    SocketLocalTransform: core_uobject.Transform
    PivotSocketBoneReference: engine.BoneReference
    PivotSocketLocalTransform: core_uobject.Transform
    bUseBlendSpaceWeightInterpolation: bool


class AnimNode_AnimDynamics(AnimNode_SkeletalControlBase):
    SimulationSpace: AnimPhysSimSpaceType
    RelativeSpaceBone: engine.BoneReference
    bChain: bool
    BoundBone: engine.BoneReference
    ChainEnd: engine.BoneReference
    BoxExtents: core_uobject.Vector
    LocalJointOffset: core_uobject.Vector
    GravityScale: float
    bLinearSpring: bool
    bAngularSpring: bool
    LinearSpringConstant: float
    AngularSpringConstant: float
    bEnableWind: bool
    bWindWasEnabled: bool
    WindScale: float
    bOverrideLinearDamping: bool
    LinearDampingOverride: float
    bOverrideAngularDamping: bool
    AngularDampingOverride: float
    bOverrideAngularBias: bool
    AngularBiasOverride: float
    bDoUpdate: bool
    bDoEval: bool
    NumSolverIterationsPreUpdate: int
    NumSolverIterationsPostUpdate: int
    ConstraintSetup: AnimPhysConstraintSetup
    bUsePlanarLimit: bool
    PlanarLimits: unreal.WrappedArray[AnimPhysPlanarLimit]
    bUseSphericalLimits: bool
    SphericalLimits: unreal.WrappedArray[AnimPhysSphericalLimit]
    CollisionType: engine.AnimPhysCollisionType
    SphereCollisionRadius: float
    ExternalForce: core_uobject.Vector
    bForceNoStretch: bool


class AnimPhysSphericalLimit:
    DrivingBone: engine.BoneReference
    SphereLocalOffset: core_uobject.Vector
    LimitRadius: float
    LimitType: ESphericalLimitType


class AnimPhysPlanarLimit:
    DrivingBone: engine.BoneReference
    PlaneTransform: core_uobject.Transform


class AnimPhysConstraintSetup:
    LinearXLimitType: AnimPhysLinearConstraintType
    LinearYLimitType: AnimPhysLinearConstraintType
    LinearZLimitType: AnimPhysLinearConstraintType
    LinearAxesMin: core_uobject.Vector
    LinearAxesMax: core_uobject.Vector
    AngularConstraintType: AnimPhysAngularConstraintType
    TwistAxis: engine.AnimPhysTwistAxis
    ConeAngle: float
    AngularXAngle: float
    AngularYAngle: float
    AngularZAngle: float
    AngularLimitsMin: core_uobject.Vector
    AngularLimitsMax: core_uobject.Vector
    AngularTargetAxis: engine.AnimPhysTwistAxis
    AngularTarget: core_uobject.Vector
    bLinearFullyLocked: bool


class AnimNode_ApplyAdditive(engine.AnimNode_Base):
    Base: engine.PoseLink
    Additive: engine.PoseLink
    Alpha: float
    AlphaScaleBias: engine.InputScaleBias
    LODThreshold: int
    ActualAlpha: float
    AlphaInputType: engine.EAnimAlphaInputType
    bAlphaBoolEnabled: bool
    AlphaBoolBlend: engine.InputAlphaBoolBlend
    AlphaCurveName: str
    AlphaScaleBiasClamp: engine.InputScaleBiasClamp
    bBoolAlpha: bool
    bInvertAlpha: bool


class AnimNode_ApplyLimits(AnimNode_SkeletalControlBase):
    AngularRangeLimits: unreal.WrappedArray[AngularRangeLimit]
    AngularOffsets: unreal.WrappedArray[core_uobject.Vector]


class AngularRangeLimit:
    LimitMin: core_uobject.Vector
    LimitMax: core_uobject.Vector
    Bone: engine.BoneReference


class AnimNode_BlendBoneByChannel(engine.AnimNode_Base):
    A: engine.PoseLink
    B: engine.PoseLink
    Alpha: float
    AlphaScaleBias: engine.InputScaleBias
    BoneDefinitions: unreal.WrappedArray[BlendBoneByChannelEntry]
    TransformsSpace: int
    InternalBlendAlpha: float
    bBIsRelevant: bool
    ValidBoneEntries: unreal.WrappedArray[BlendBoneByChannelEntry]
    bInvertAlpha: bool


class BlendBoneByChannelEntry:
    SourceBone: engine.BoneReference
    TargetBone: engine.BoneReference
    bBlendTranslation: bool
    bBlendRotation: bool
    bBlendScale: bool


class AnimNode_BlendListBase(engine.AnimNode_Base):
    BlendPose: unreal.WrappedArray[engine.PoseLink]
    BlendTime: unreal.WrappedArray[float]
    BlendType: engine.EAlphaBlendOption
    CustomBlendCurve: engine.CurveFloat
    BlendProfile: engine.BlendProfile
    Blends: unreal.WrappedArray[engine.AlphaBlend]
    BlendWeights: unreal.WrappedArray[float]
    RemainingBlendTimes: unreal.WrappedArray[float]
    LastActiveChildIndex: int
    PerBoneSampleData: unreal.WrappedArray[engine.BlendSampleData]
    bResetChildOnActivation: bool


class AnimNode_BlendListByBool(AnimNode_BlendListBase):
    bActiveValue: bool


class AnimNode_BlendListByEnum(AnimNode_BlendListBase):
    EnumToPoseIndex: unreal.WrappedArray[int]
    ActiveEnumValue: int


class AnimNode_BlendListByInt(AnimNode_BlendListBase):
    ActiveChildIndex: int


class AnimNode_BlendSpaceEvaluator(AnimNode_BlendSpacePlayer):
    NormalizedTime: float


class AnimNode_BoneDrivenController(AnimNode_SkeletalControlBase):
    SourceBone: engine.BoneReference
    SourceComponent: int
    DrivingCurve: engine.CurveFloat
    Multiplier: float
    bUseRange: bool
    RangeMin: float
    RangeMax: float
    RemappedMin: float
    RemappedMax: float
    DestinationMode: EDrivenDestinationMode
    ParameterName: str
    TargetBone: engine.BoneReference
    TargetComponent: int
    bAffectTargetTranslationX: bool
    bAffectTargetTranslationY: bool
    bAffectTargetTranslationZ: bool
    bAffectTargetRotationX: bool
    bAffectTargetRotationY: bool
    bAffectTargetRotationZ: bool
    bAffectTargetScaleX: bool
    bAffectTargetScaleY: bool
    bAffectTargetScaleZ: bool
    ModificationMode: EDrivenBoneModificationMode


class AnimNode_Constraint(AnimNode_SkeletalControlBase):
    BoneToModify: engine.BoneReference
    ConstraintSetup: unreal.WrappedArray[Constraint]
    ConstraintWeights: unreal.WrappedArray[float]


class Constraint:
    TargetBone: engine.BoneReference
    OffsetOption: EConstraintOffsetOption
    TransformType: animation_core.ETransformConstraintType
    PerAxis: animation_core.FilterOptionPerAxis


class AnimNode_CopyBone(AnimNode_SkeletalControlBase):
    SourceBone: engine.BoneReference
    TargetBone: engine.BoneReference
    bCopyTranslation: bool
    bCopyRotation: bool
    bCopyScale: bool
    ControlSpace: int


class AnimNode_CopyBoneDelta(AnimNode_SkeletalControlBase):
    SourceBone: engine.BoneReference
    TargetBone: engine.BoneReference
    bCopyTranslation: bool
    bCopyRotation: bool
    bCopyScale: bool
    CopyMode: CopyBoneDeltaMode
    TranslationMultiplier: float
    RotationMultiplier: float
    ScaleMultiplier: float


class AnimNode_CopyPoseFromMesh(engine.AnimNode_Base):
    SourceMeshComponent: engine.SkeletalMeshComponent
    bUseAttachedParent: bool
    bCopyCurves: bool


class AnimNode_CurveSource(engine.AnimNode_Base):
    SourcePose: engine.PoseLink
    SourceBinding: str
    Alpha: float
    CurveSource: Any


class AnimNode_Fabrik(AnimNode_SkeletalControlBase):
    EffectorTransform: core_uobject.Transform
    EffectorTransformSpace: int
    EffectorTransformBone: engine.BoneReference
    EffectorTarget: BoneSocketTarget
    EffectorRotationSource: int
    TipBone: engine.BoneReference
    RootBone: engine.BoneReference
    Precision: float
    MaxIterations: int
    bEnableDebugDraw: bool


class BoneSocketTarget:
    bUseSocket: bool
    BoneReference: engine.BoneReference
    SocketReference: SocketReference


class SocketReference:
    SocketName: str


class AnimNode_HandIKRetargeting(AnimNode_SkeletalControlBase):
    RightHandFK: engine.BoneReference
    LeftHandFK: engine.BoneReference
    RightHandIK: engine.BoneReference
    LeftHandIK: engine.BoneReference
    IKBonesToMove: unreal.WrappedArray[engine.BoneReference]
    HandFKWeight: float


class AnimNode_LayeredBoneBlend(engine.AnimNode_Base):
    BasePose: engine.PoseLink
    BlendPoses: unreal.WrappedArray[engine.PoseLink]
    LayerSetup: unreal.WrappedArray[engine.InputBlendPose]
    BlendWeights: unreal.WrappedArray[float]
    bMeshSpaceRotationBlend: bool
    CurveBlendOption: int
    bBlendRootMotionBasedOnRootBone: bool
    bHasRelevantPoses: bool
    LODThreshold: int
    PerBoneBlendWeights: unreal.WrappedArray[engine.PerBoneBlendWeight]
    SkeletonGuid: core_uobject.Guid
    VirtualBoneGuid: core_uobject.Guid
    bBoolBlendWeights: unreal.WrappedArray[bool]
    bUseBoolBlendWeights: unreal.WrappedArray[bool]
    bInvertWeight: unreal.WrappedArray[bool]


class AnimNode_LayeredBoneSetBlend(engine.AnimNode_Base):
    BasePose: engine.PoseLink
    BlendPoses: unreal.WrappedArray[engine.PoseLink]
    BoneSets: unreal.WrappedArray[engine.GbxBoneSet]
    BoneSetGuids: unreal.WrappedArray[core_uobject.Guid]
    BlendWeights: unreal.WrappedArray[float]
    CurveBlendOption: int
    bBlendRootMotionBasedOnRootBone: bool
    bHasRelevantPoses: bool
    PerBoneBlendWeights: unreal.WrappedArray[engine.BoneSetWeight]
    SkeletonGuid: core_uobject.Guid
    VirtualBoneGuid: core_uobject.Guid
    bBoolBlendWeights: unreal.WrappedArray[bool]
    bUseBoolBlendWeights: unreal.WrappedArray[bool]
    bInvertWeight: unreal.WrappedArray[bool]


class AnimNode_LegIK(AnimNode_SkeletalControlBase):
    ReachPrecision: float
    MaxIterations: int
    LegsDefinition: unreal.WrappedArray[AnimLegIKDefinition]
    LegsData: unreal.WrappedArray[AnimLegIKData]


class AnimLegIKData: ...


class AnimLegIKDefinition:
    IKFootBone: engine.BoneReference
    FKFootBone: engine.BoneReference
    NumBonesInLimb: int
    FootBoneForwardAxis: int
    HingeRotationAxis: int
    bEnableRotationLimit: bool
    MinRotationAngle: float
    MaxRotationAngle: float
    bEnableKneeTwistCorrection: bool


class IKChain: ...


class IKChainLink: ...


class AnimNode_LookAt(AnimNode_SkeletalControlBase):
    BoneToModify: engine.BoneReference
    LookAtBone: engine.BoneReference
    LookAtSocket: str
    LookAtTarget: BoneSocketTarget
    LookAtLocation: core_uobject.Vector
    LookAtAxis: int
    CustomLookAtAxis: core_uobject.Vector
    LookAt_Axis: animation_core.AXIS
    bUseLookUpAxis: bool
    LookUpAxis: int
    CustomLookUpAxis: core_uobject.Vector
    LookUp_Axis: animation_core.AXIS
    LookAtClamp: float
    InterpolationType: int
    InterpolationTime: float
    InterpolationTriggerThreashold: float
    bUseRollCorrection: bool
    RollCorrectionLookUpAxis: animation_core.AXIS


class AnimNode_MakeDynamicAdditive(engine.AnimNode_Base):
    Base: engine.PoseLink
    Additive: engine.PoseLink
    bMeshSpaceAdditive: bool
    bIgnoreCurves: bool


class AnimNode_ModifyBone(AnimNode_SkeletalControlBase):
    BoneToModify: engine.BoneReference
    Translation: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Scale: core_uobject.Vector
    TranslationMode: int
    RotationMode: int
    ScaleMode: int
    TranslationSpace: int
    RotationSpace: int
    ScaleSpace: int
    BoneOverrideTag: str
    bOverrideBoneToModify: bool


class AnimNode_ModifyCurve(engine.AnimNode_Base):
    SourcePose: engine.PoseLink
    ApplyMode: EModifyCurveApplyMode
    CurveValues: unreal.WrappedArray[float]
    LastCurveValues: unreal.WrappedArray[float]
    CurveNames: unreal.WrappedArray[str]
    Alpha: float


class AnimNode_MultiWayBlend(engine.AnimNode_Base):
    Poses: unreal.WrappedArray[engine.PoseLink]
    DesiredAlphas: unreal.WrappedArray[float]
    bAdditiveNode: bool
    bNormalizeAlpha: bool
    AlphaScaleBias: engine.InputScaleBias
    bInvertAlpha: unreal.WrappedArray[bool]


class AnimNode_ObserveBone(AnimNode_SkeletalControlBase):
    BoneToObserve: engine.BoneReference
    DisplaySpace: int
    bRelativeToRefPose: bool
    Translation: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Scale: core_uobject.Vector


class AnimNode_PoseHandler(engine.AnimNode_AssetPlayerBase):
    PoseAsset: engine.PoseAsset


class AnimNode_PoseBlendNode(AnimNode_PoseHandler):
    SourcePose: engine.PoseLink
    BlendOption: engine.EAlphaBlendOption
    CustomCurve: engine.CurveFloat


class AnimNode_PoseByName(AnimNode_PoseHandler):
    PoseName: str
    PoseWeight: float


class AnimNode_PoseDriver(AnimNode_PoseHandler):
    SourcePose: engine.PoseLink
    SourceBones: unreal.WrappedArray[engine.BoneReference]
    bOnlyDriveSelectedBones: bool
    OnlyDriveBones: unreal.WrappedArray[engine.BoneReference]
    EvalSpaceBone: engine.BoneReference
    RBFParams: RBFParams
    DriveSource: EPoseDriverSource
    DriveOutput: EPoseDriverOutput
    PoseTargets: unreal.WrappedArray[PoseDriverTarget]
    SourceBone: engine.BoneReference
    TwistAxis: int
    Type: EPoseDriverType
    RadialScaling: float


class PoseDriverTarget:
    BoneTransforms: unreal.WrappedArray[PoseDriverTransform]
    TargetRotation: core_uobject.Rotator
    TargetScale: float
    bApplyCustomCurve: bool
    CustomCurve: engine.RichCurve
    DrivenName: str


class PoseDriverTransform:
    TargetTranslation: core_uobject.Vector
    TargetRotation: core_uobject.Rotator


class RBFParams:
    TargetDimensions: int
    Radius: float
    Function: ERBFFunctionType
    DistanceMethod: ERBFDistanceMethod
    TwistAxis: int
    WeightThreshold: float


class AnimNode_PoseSnapshot(engine.AnimNode_Base):
    Mode: ESnapshotSourceMode
    SnapshotName: str
    Snapshot: engine.PoseSnapshot


class AnimNode_RandomPlayer(engine.AnimNode_Base):
    bShuffleMode: bool
    Entries: unreal.WrappedArray[RandomPlayerSequenceEntry]
    IdlePose: engine.PoseLink
    EntryPoseData: RandomPlayerInputEntryData


class RandomPlayerInputEntryData:
    BlendIn: engine.AlphaBlend
    MinPlayTime: float
    MaxPlayTime: float


class RandomPlayerSequenceEntry:
    Sequence: engine.AnimSequence
    ChanceToPlay: float
    MinLoopCount: int
    MaxLoopCount: int
    MinPlayRate: float
    MaxPlayRate: float
    BlendIn: engine.AlphaBlend
    AnimAssetName: str
    LastAnimAssetName: str
    bUseRateScaleSpeed: bool
    RateScaleSpeed: float
    Duration: float


class AnimNode_MeshSpaceRefPose(engine.AnimNode_Base): ...


class AnimNode_RefPose(engine.AnimNode_Base):
    RefPoseType: int


class AnimNode_Root(engine.AnimNode_Base):
    Result: engine.PoseLink


class AnimNode_RotateRootBone(engine.AnimNode_Base):
    BasePose: engine.PoseLink
    Pitch: float
    Yaw: float
    PitchScaleBiasClamp: engine.InputScaleBiasClamp
    YawScaleBiasClamp: engine.InputScaleBiasClamp
    MeshToComponent: core_uobject.Rotator
    ActualPitch: float
    ActualYaw: float


class AnimNode_RotationMultiplier(AnimNode_SkeletalControlBase):
    TargetBone: engine.BoneReference
    SourceBone: engine.BoneReference
    Multiplier: float
    RotationAxisToRefer: int
    bIsAdditive: bool


class AnimNode_RotationOffsetBlendSpace(AnimNode_BlendSpacePlayer):
    BasePose: engine.PoseLink
    LODThreshold: int
    bIsLODEnabled: bool
    AlphaInputType: engine.EAnimAlphaInputType
    Alpha: float
    AlphaScaleBias: engine.InputScaleBias
    ActualAlpha: float
    bAlphaBoolEnabled: bool
    AlphaBoolBlend: engine.InputAlphaBoolBlend
    AlphaCurveName: str
    AlphaScaleBiasClamp: engine.InputScaleBiasClamp


class AnimNode_ScaleChainLength(engine.AnimNode_Base):
    InputPose: engine.PoseLink
    DefaultChainLength: float
    ChainStartBone: engine.BoneReference
    ChainEndBone: engine.BoneReference
    ChainInitialLength: EScaleChainInitialLength
    TargetLocation: core_uobject.Vector
    Alpha: float
    ActualAlpha: float
    AlphaScaleBias: engine.InputScaleBias
    bBoneIndicesCached: bool


class AnimNode_SequenceEvaluator(engine.AnimNode_AssetPlayerBase):
    Sequence: engine.AnimSequenceBase
    ExplicitTime: float
    bShouldLoop: bool
    bTeleportToExplicitTime: bool
    StartPosition: float
    ReinitializationBehavior: int
    bReinitialized: bool


class AnimNode_Slot(engine.AnimNode_Base):
    Source: engine.PoseLink
    SlotName: str
    bAlwaysUpdateSourcePose: bool
    bAlwaysEvaluateSource: bool
    CameraRefPose: engine.AnimSequence


class AnimNode_SplineIK(AnimNode_SkeletalControlBase):
    StartBone: engine.BoneReference
    EndBone: engine.BoneReference
    BoneAxis: ESplineBoneAxis
    bAutoCalculateSpline: bool
    PointCount: int
    ControlPoints: unreal.WrappedArray[core_uobject.Transform]
    Roll: float
    TwistStart: float
    TwistEnd: float
    TwistBlend: engine.AlphaBlend
    Stretch: float
    Offset: float
    BoneSpline: engine.SplineCurves
    OriginalSplineLength: float
    CachedBoneReferences: unreal.WrappedArray[SplineIKCachedBoneData]
    CachedBoneLengths: unreal.WrappedArray[float]
    CachedOffsetRotations: unreal.WrappedArray[core_uobject.Quat]


class SplineIKCachedBoneData:
    Bone: engine.BoneReference
    RefSkeletonIndex: int


class AnimNode_SpringBone(AnimNode_SkeletalControlBase):
    SpringBone: engine.BoneReference
    bLimitDisplacement: bool
    MaxDisplacement: float
    SpringStiffness: float
    SpringDamping: float
    ErrorResetThresh: float
    bNoZSpring: bool
    bTranslateX: bool
    bTranslateY: bool
    bTranslateZ: bool
    bRotateX: bool
    bRotateY: bool
    bRotateZ: bool


class AnimNode_Trail(AnimNode_SkeletalControlBase):
    TrailBone: engine.BoneReference
    ChainLength: int
    ChainBoneAxis: int
    bInvertChainBoneAxis: bool
    TrailRelaxation: float
    TrailRelaxationSpeed: engine.RuntimeFloatCurve
    RelaxationSpeedScale: float
    RelaxationSpeedScaleInputProcessor: engine.InputScaleBiasClamp
    bLimitStretch: bool
    StretchLimit: float
    FakeVelocity: core_uobject.Vector
    bActorSpaceFakeVel: bool
    BaseJoint: engine.BoneReference


class AnimNode_TwistCorrectiveNode(AnimNode_SkeletalControlBase):
    BaseFrame: ReferenceBoneFrame
    TwistFrame: ReferenceBoneFrame
    TwistPlaneNormalAxis: animation_core.AXIS
    RangeMax: float
    RemappedMin: float
    RemappedMax: float
    Curve: engine.AnimCurveParam


class ReferenceBoneFrame:
    Bone: engine.BoneReference
    AXIS: animation_core.AXIS


class AnimNode_TwoBoneIK(AnimNode_SkeletalControlBase):
    IKBone: engine.BoneReference
    bAllowStretching: bool
    StartStretchRatio: float
    MaxStretchScale: float
    StretchLimits: core_uobject.Vector2D
    bTakeRotationFromEffectorSpace: bool
    bMaintainEffectorRelRot: bool
    EffectorLocationSpace: int
    EffectorSpaceBoneName: str
    EffectorLocation: core_uobject.Vector
    EffectorTarget: BoneSocketTarget
    JointTargetLocationSpace: int
    JointTargetLocation: core_uobject.Vector
    JointTargetSpaceBoneName: str
    JointTarget: BoneSocketTarget
    bAllowTwist: bool
    TwistAxis: animation_core.AXIS
    bNoTwist: bool


class AnimNode_TwoWayBlend(engine.AnimNode_Base):
    A: engine.PoseLink
    B: engine.PoseLink
    AlphaInputType: engine.EAnimAlphaInputType
    Alpha: float
    AlphaScaleBias: engine.InputScaleBias
    bAlphaBoolEnabled: bool
    AlphaBoolBlend: engine.InputAlphaBoolBlend
    AlphaCurveName: str
    AlphaScaleBiasClamp: engine.InputScaleBiasClamp
    InternalBlendAlpha: float
    bAIsRelevant: bool
    bBIsRelevant: bool
    bResetChildOnActivation: bool
    bInvertAlpha: bool


class AnimSequencerInstanceProxy(engine.AnimInstanceProxy): ...


class RBFEntry:
    Values: unreal.WrappedArray[float]


class RBFTarget(RBFEntry):
    ScaleFactor: float
    bApplyCustomCurve: bool
    CustomCurve: engine.RichCurve


class ESphericalLimitType(enum.Enum):
    Outer = 0
    ESphericalLimitType_MAX = 1


class AnimPhysSimSpaceType(enum.Enum):
    Actor = 0
    World = 1
    BoneRelative = 2


class AnimPhysLinearConstraintType(enum.Enum):
    AnimPhysLinearConstraintType_MAX = 0
    Limited = 1


class AnimPhysAngularConstraintType(enum.Enum):
    Cone = 0
    AnimPhysAngularConstraintType_MAX = 1


class EDrivenDestinationMode(enum.Enum):
    MaterialParameter = 0
    MorphTarget = 1


class EDrivenBoneModificationMode(enum.Enum):
    ReplaceComponent = 0
    AddToRefPose = 1


class EConstraintOffsetOption(enum.Enum):
    Offset_RefPose = 0
    EConstraintOffsetOption_MAX = 1


class CopyBoneDeltaMode(enum.Enum):
    Copy = 0
    CopyBoneDeltaMode_MAX = 1


class EInterpolationBlend(enum.Enum):
    Cubic = 0
    Sinusoidal = 1
    EaseInOutExponent3 = 2


class EBoneModificationMode(enum.Enum):
    BMM_Replace = 0
    BMM_Additive = 1


class EModifyCurveApplyMode(enum.Enum):
    RemapCurve = 0
    Scale = 1
    Blend = 2


class EPoseDriverOutput(enum.Enum):
    EPoseDriverOutput_MAX = 0
    DriveCurves = 1


class EPoseDriverSource(enum.Enum):
    EPoseDriverSource_MAX = 0
    Translation = 1


class EPoseDriverType(enum.Enum):
    SwingOnly = 0
    Translation = 1


class ESnapshotSourceMode(enum.Enum):
    SnapshotPin = 0
    ESnapshotSourceMode_MAX = 1


class ERefPoseType(enum.Enum):
    EIT_Additive = 0
    EIT_MAX = 1


class EScaleChainInitialLength(enum.Enum):
    ChainLength = 0
    Distance = 1


class ESequenceEvalReinit(enum.Enum):
    StartPosition = 0
    ExplicitTime = 1


class ESplineBoneAxis(enum.Enum):
    X = 0
    Y = 1
    ESplineBoneAxis_MAX = 2


class ERBFDistanceMethod(enum.Enum):
    Quaternion = 0
    SwingAngle = 1


class ERBFFunctionType(enum.Enum):
    Linear = 0
    Exponential = 1
    Quintic = 2


class EScreenSizeSelection(enum.Enum):
    Preset = 0
    EScreenSizeSelection_MAX = 1
