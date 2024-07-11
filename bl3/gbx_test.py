from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import gbx_probes
from . import gbx_game_system_core
from . import gbx_ui
from . import input_core
from . import gbx_probes_core


class AssetTrait(engine.DataAsset):
    TraitToWhitelist: AssetTrait


class AssetTraitMaterial(AssetTrait):
    UsedWithSkeletalMesh: OptionalBool
    UsedWithParticleSprites: OptionalBool
    UsedWithBeamTrails: OptionalBool
    UsedWithMeshParticles: OptionalBool
    UsedWithStaticLighting: OptionalBool
    UsedWithMorphTargets: OptionalBool
    UsedWithSplineMesh: OptionalBool
    UsedWithLandscape: OptionalBool
    UsedWithInstancedStaticMeshes: OptionalBool
    UsedWithClothing: OptionalBool
    HasPhysMatSet: OptionalBool


class AssetTraitMesh(AssetTrait):
    LODMinCount: OptionalInt32
    LODMaxCount: OptionalInt32
    MaxTriangleCount: OptionalInt32
    MaxVertexCount: OptionalInt32
    MinTexCoordCount: OptionalInt32
    MaxTexCoordCount: OptionalInt32
    MinSectionCount: OptionalInt32
    MaxSectionCount: OptionalInt32
    MinSocketCount: OptionalInt32
    MaxSocketCount: OptionalInt32
    HasSockets: OptionalBool


class AssetTraitParticleSystem(AssetTrait):
    MinEmitterCount: OptionalInt32
    MaxEmitterCount: OptionalInt32
    MinModuleCount: OptionalInt32
    MaxModuleCount: OptionalInt32
    MinLODCount: OptionalInt32
    MaxLODCount: OptionalInt32
    MinLODDistanceCheckTime: OptionalFloat
    MaxLODDistanceCheckTime: OptionalFloat
    MinUpdateTime: OptionalFloat
    MaxUpdateTime: OptionalFloat
    MaxWarmupTime: OptionalFloat
    MinDataAnimTrailCount: OptionalInt32
    MaxDataAnimTrailCount: OptionalInt32
    MinDataGPUSpritesCount: OptionalInt32
    MaxDataGPUSpritesCount: OptionalInt32
    MinDataMeshCount: OptionalInt32
    MaxDataMeshCount: OptionalInt32
    MinDataRibbonOrBeamCount: OptionalInt32
    MaxDataRibbonOrBeamCount: OptionalInt32
    MaxTemplateCost: OptionalFloat
    bHasDataAnimTrail: OptionalBool
    bHasDataGPUSprites: OptionalBool
    bHasDataMesh: OptionalBool
    bHasDataRibbonOrBeam: OptionalBool
    MaxDrawCount: OptionalInt32
    bKillOnCompletedNotSet: OptionalBool
    MinUnitScalar: OptionalFloat
    bUseInverseSquaredFalloffSet: OptionalBool
    bAllowInfiniteLifetimes: OptionalBool
    MaxLifetime: OptionalFloat


class AssetTraitSkeletalMesh(AssetTraitMesh): ...


class AssetTraitStaticMesh(AssetTraitMesh):
    MinPrimitiveCount: OptionalInt32
    MaxPrimitiveCount: OptionalInt32
    MinLightmapResolution: OptionalInt32
    MaxLightmapResolution: OptionalInt32
    MinLightMapIndex: OptionalInt32
    MaxLightMapIndex: OptionalInt32
    LODGroup: OptionalLODGroup
    CastShadow: OptionalBool
    EnableCollision: OptionalBool


class AssetTraitTexture(AssetTrait):
    CompressionMethod: OptionalTextureCompressionMethod
    LODGroup: OptionalTextureLODGroup
    MinLODBias: OptionalInt32
    MaxLODBias: OptionalInt32
    HasAlpha: OptionalBool
    HassRGB: OptionalBool


class AutomationMenuHelper(unreal.UObject):

    def PrevPage(self): ...
    def PageName(self) -> str: ...
    def NumPages(self) -> int: ...
    def NextPage(self): ...
    def NextFocus(self, Direction: EAutomationUIDirection): ...
    def MenuName(self) -> str: ...
    def HasOpenMenu(self) -> bool: ...
    def FocusName(self) -> str: ...
    def FocusInfo(self) -> AutomationMenuFocusInfo: ...
    def CurrentDepth(self) -> int: ...
    def CreateAutomationMenuHelper(
        self,
        PlayerController: gbx_game_system_core.GbxPlayerController,
        SimulateAllInputs: bool,
    ) -> AutomationMenuHelper: ...
    def BackOut(self): ...
    def ActuateFocus(self, Action: EAutomationUIAction): ...


class AutomationUILibrary(engine.BlueprintFunctionLibrary):

    def ForceDisableTutorials(self, ForceDisable: bool): ...


class GbxTestContentAuditCommandlet(engine.Commandlet): ...


class GbxTestJiraCommandlet(engine.Commandlet): ...


class GbxTestContentAuditSettings(unreal.UObject):
    WhitelistDirectories: unreal.WrappedArray[str]


class GbxTestParticleMaterialAuditCommandlet(engine.Commandlet): ...


class GbxTestSettings(unreal.UObject):
    TestContentPaths: unreal.WrappedArray[str]


class PerfMapCapture(unreal.UObject):

    def SavePerfMapCapturesFromConfiguration(
        self,
        World: engine.World,
        Path: str,
        Configuration: MapParameters,
        LatentInfo: engine.LatentActionInfo,
    ): ...
    def SavePerfMapCaptures(
        self,
        World: unreal.UObject,
        Path: str,
        Density: float,
        bLighting: bool,
        bSpecular: bool,
        Gamma: float,
        Width: int,
        Height: int,
        VolumeX: float,
        VolumeY: float,
        VolumeZ: float,
        OutputPattern: str,
    ) -> bool: ...


class PerformanceSnapshotCollector(engine.BlueprintFunctionLibrary):

    def ResetSnapshotProviders(self): ...
    def CreatePerformanceSnapshotCollector(
        self, StatSection: str, ExecOut: ESnapshotExecOutput
    ) -> PerformanceSnapshotCollector: ...
    def CollectSnapshot(
        self,
        WorldContextObject: unreal.UObject,
        ReportContext: str,
        LatentInfo: engine.LatentActionInfo,
    ): ...
    def CollectProbeSnapshot(
        self,
        WorldContextObject: unreal.UObject,
        ReportContext: str,
        ProbeId: gbx_probes_core.GbxProbeId,
        Test: str,
        ExtraDataArray: unreal.WrappedArray[gbx_probes.GbxProbeExtraData],
        LatentInfo: engine.LatentActionInfo,
    ): ...


class MatcherFunctionality(unreal.UObject):

    def Size(self) -> int: ...
    def Ready(self) -> bool: ...
    def GetSuffix(self) -> str: ...
    def GetPrefix(self) -> str: ...
    def GetPosition(self, Start: int) -> int: ...
    def GetMatch(self, Index: int) -> str: ...
    def GetLength(self) -> int: ...
    def GetAtIndex(self, Index: int) -> str: ...
    def Empty(self) -> bool: ...


class RegexFunctionality(unreal.UObject):
    Regex: Regex

    def RegexSearch(
        self, Regex: Regex, Matcher: MatcherFunctionality, Input: str
    ) -> bool: ...
    def RegexRepleace(self, Regex: Regex, Input: str, Repleacement: str) -> str: ...
    def RegexMatch2(
        self, Regex: Regex, Matcher: MatcherFunctionality, Input: str
    ) -> bool: ...
    def RegexMatch(self, Regex: Regex, Input: str) -> bool: ...
    def FindAll(self, Regex: Regex, String: str): ...
    def Assign2(self, Regex: Regex, Pattern: str, Flags: ESyntaxOption): ...
    def Assign(self, Regex: Regex, Pattern: str): ...


class GbxTestHierarchicalCommands(engine.DataAsset):
    Commands: unreal.WrappedArray[GbxTestHierarchicalCommandL1]


class TestLibrary(engine.BlueprintFunctionLibrary):

    def TakeScreenshot(
        self,
        CustomFilename: str,
        OverrideResolution: core_uobject.Vector2D,
        ShowUI: bool,
        AddUniqueSuffix: bool,
    ): ...
    def SortStrings(
        self, Values: unreal.WrappedArray[str], Descending: bool
    ) -> unreal.WrappedArray[str]: ...
    def SortObjectsByName(
        self, Values: unreal.WrappedArray[unreal.UObject], Descending: bool
    ) -> unreal.WrappedArray[unreal.UObject]: ...
    def SortIntegers(
        self, Values: unreal.WrappedArray[int], Descending: bool
    ) -> unreal.WrappedArray[int]: ...
    def SortFloats(
        self, Values: unreal.WrappedArray[float], Descending: bool
    ) -> unreal.WrappedArray[float]: ...
    def SimulateInputKey(
        self,
        PlayerController: engine.PlayerController,
        Key: input_core.Key,
        EVENTTYPE: int,
        AmountDepressed: float,
    ): ...
    def SimulateInputAxis(
        self,
        PlayerController: engine.PlayerController,
        Key: input_core.Key,
        Delta: float,
        InterpTime: float,
        LatentInfo: engine.LatentActionInfo,
    ): ...
    def RemoveItemFromCollection(self, CollectionName: str, ObjectName: str): ...
    def RemoveArrayFromCollection(
        self, CollectionName: str, objectNames: unreal.WrappedArray[str]
    ): ...
    def ReadFromIni(
        self, Section: str, Key: str, Values: unreal.WrappedArray[str]
    ) -> bool: ...
    def MoveItemCollection(
        self, fromCollection: str, toCollection: str, ObjectName: str
    ): ...
    def MoveArrayCollection(
        self,
        fromCollection: str,
        toCollection: str,
        objectNames: unreal.WrappedArray[str],
    ): ...
    def LoadBlueprintAsset(self, Path: str, Object: unreal.UObject): ...
    def LoadAsset(self, Path: str, Object: unreal.UObject): ...
    def IsEditorSession(self) -> bool: ...
    def IsAssetInCollectionEx(
        self, CollectionName: str, CollectionType: int, ObjectName: str
    ) -> bool: ...
    def IsAssetInCollection(self, CollectionName: str, ObjectName: str) -> bool: ...
    def GetWorldForActor(self, Actor: engine.Actor) -> engine.World: ...
    def GetTestDriversFromStrings(
        self,
        Strings: unreal.WrappedArray[str],
        TestDrivers: unreal.WrappedArray[unreal.UClass],
        UndiscoveredItems: str,
    ): ...
    def GetReferencedBlueprintClasses(
        self,
        Object: unreal.UObject,
        Class: unreal.UClass,
        Classes: unreal.WrappedArray[unreal.UClass],
    ): ...
    def GetObjectTags(
        self, ObjectTags: unreal.WrappedArray[engine.ObjectTag], Asset: unreal.UObject
    ): ...
    def GetAssetPath(self, Asset: unreal.UObject, AssetPath: str): ...
    def GetAssetName(self, AssetPath: str, AssetName: str): ...
    def FilterDiscoveredAssets(
        self,
        InPathNames: unreal.WrappedArray[str],
        InPrettyNames: unreal.WrappedArray[str],
        OutPathNames: unreal.WrappedArray[str],
        OutPrettyNames: unreal.WrappedArray[str],
        AssetNamePrefix: str,
        AssetNamePostfix: str,
        AssetNameContains: str,
        AssetPathContains: str,
    ): ...
    def DiscoverAssets(
        self,
        PathNames: unreal.WrappedArray[str],
        PrettyNames: unreal.WrappedArray[str],
        Directories: unreal.WrappedArray[str],
        Classes: unreal.WrappedArray[unreal.UClass],
        ExcludeRecursiveClasses: unreal.WrappedArray[unreal.UClass],
        bRecursiveDirectories: bool,
        bRecursiveClasses: bool,
    ): ...
    def CreateLocalCollection(self, CollectionName: str, ParentName: str) -> str: ...
    def ContainsSubPath(self, Path: str, SubPath: str) -> bool: ...
    def ContainsObjectTag(
        self,
        ObjectTags: unreal.WrappedArray[engine.ObjectTag],
        Category: str,
        Name: str,
        bExactCategory: bool,
        bCaseSensitiveCategory: bool,
        bExactName: bool,
        bCaseSensitiveName: bool,
    ) -> bool: ...
    def CollectionExistsEx(self, CollectionName: str, CollectionType: int) -> bool: ...
    def CollectionExists(self, CollectionName: str) -> bool: ...
    def AddItemToCollection(self, CollectionName: str, ObjectName: str): ...
    def AddArrayToCollection(
        self, CollectionName: str, objectNames: unreal.WrappedArray[str]
    ): ...


class TestLibraryContent(engine.BlueprintFunctionLibrary):

    def LoadAssetTexture(self, ObjectPath: str) -> engine.Texture: ...
    def LoadAssetStaticMesh(self, ObjectPath: str) -> engine.StaticMesh: ...
    def LoadAssetSkeletalMesh(self, ObjectPath: str) -> engine.SkeletalMesh: ...
    def LoadAssetParticleSystem(self, ObjectPath: str) -> engine.ParticleSystem: ...
    def LoadAssetMaterial(self, ObjectPath: str) -> engine.Material: ...
    def GetTestInfoTexture(self, Asset: engine.Texture, Info: TestInfoTexture): ...
    def GetTestInfoStaticMeshLOD(
        self, Asset: engine.StaticMesh, LODIndex: int, Info: TestInfoMeshLOD
    ): ...
    def GetTestInfoStaticMesh(
        self,
        Asset: engine.StaticMesh,
        LODSummary: TestInfoMeshLODSummary,
        Mesh: TestInfoMesh,
        StaticMesh: TestInfoStaticMesh,
    ): ...
    def GetTestInfoSkeletalMeshLOD(
        self, Asset: engine.SkeletalMesh, LODIndex: int, Info: TestInfoMeshLOD
    ): ...
    def GetTestInfoSkeletalMesh(
        self,
        Asset: engine.SkeletalMesh,
        LODSummary: TestInfoMeshLODSummary,
        Mesh: TestInfoMesh,
        SkeletalMesh: TestInfoSkeletalMesh,
    ): ...
    def GetTestInfoParticleSystem(
        self, Asset: engine.ParticleSystem, Info: TestInfoParticleSystem
    ): ...
    def GetTestInfoParticleEmitter(
        self,
        Asset: engine.ParticleSystem,
        EmitterIndex: int,
        Info: TestInfoParticleEmitter,
    ): ...
    def GetTestInfoMaterial(self, Asset: engine.Material, Info: TestInfoMaterial): ...
    def GetAllPersistentGameMaps(
        self, OutMapNames: unreal.WrappedArray[str], ShortNamesOnly: bool
    ): ...
    def ContentAuditSingleObject(
        self, Asset: unreal.UObject
    ) -> unreal.WrappedArray[str]: ...


class TestLibraryPerformance(engine.BlueprintFunctionLibrary):

    def WaitForFrames(
        self,
        WorldContextObject: unreal.UObject,
        NumFrames: int,
        LatentInfo: engine.LatentActionInfo,
    ): ...
    def GenerateLevelGrid(
        self,
        GridLocations: unreal.WrappedArray[core_uobject.Vector],
        Pawn: engine.Pawn,
        GridSize: float,
        bWalkableOnly: bool,
    ): ...


class TestLibrarySimulation(engine.BlueprintFunctionLibrary):

    def TestIntInRangeFromPlayMap(
        self,
        Value: int,
        Min: int,
        Max: int,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestIntCompareFromPlayMap(
        self,
        Value: int,
        Other: int,
        Comparison: ECompare,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestFloatInRangeFromPlayMap(
        self,
        Value: float,
        Min: float,
        Max: float,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestFloatCompareFromPlayMap(
        self,
        Value: float,
        Other: float,
        Comparison: ECompare,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
        Tolerance: float,
    ): ...
    def TestBoolIsTrueFromPlayMap(
        self,
        Value: bool,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestBoolIsFalseFromPlayMap(
        self,
        Value: bool,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def StopPlayTest(self): ...
    def SimulatePlayerInput(
        self,
        WorldContextObject: unreal.UObject,
        PlayerController: engine.PlayerController,
        InputDescription: unreal.WrappedArray[GbxTestInputAction],
        PreDelay: float,
        PostDelay: float,
        LatentInfo: engine.LatentActionInfo,
    ): ...
    def SetReportContext(
        self,
        WorldContextObject: unreal.UObject,
        AssetContexts: unreal.WrappedArray[gbx_probes_core.GbxProbeId],
    ): ...
    def SetReceiveBackgroundInput(
        self, PlayerController: engine.PlayerController, AllowBackgroundInput: bool
    ) -> bool: ...
    def ResetTestTimeout(self): ...
    def ReportResultFromPlayMap(
        self,
        bSucceeded: bool,
        IssueCategory: str,
        IssueMessage: str,
        AssetContext: gbx_probes_core.GbxProbeId,
        FailedIssueType: ETestIssueType,
    ): ...
    def ReportIssueFromPlayMap(
        self, IssueType: ETestIssueType, IssueCategory: str, IssueMessage: str
    ): ...
    def PushWorldContext(self, WorldContextObject: unreal.UObject): ...
    def PushAssetContext(self, ID: gbx_probes_core.GbxProbeId): ...
    def PopWorldContext(self): ...
    def PopAssetContext(self, ID: gbx_probes_core.GbxProbeId): ...
    def IsPlayMapRunning(self) -> bool: ...
    def IsHLQNoClipEnabled(self, PlayerController: engine.PlayerController) -> bool: ...
    def IsGodEnabled(self, PlayerController: engine.PlayerController) -> bool: ...
    def IsGhostEnabled(self, PlayerController: engine.PlayerController) -> bool: ...
    def IsDemiGodEnabled(self, PlayerController: engine.PlayerController) -> bool: ...
    def GetPolicyForPlayMap(self) -> TestPolicySimulation: ...
    def CanReceiveBackgroundInput(
        self, PlayerController: engine.PlayerController
    ) -> bool: ...


class GbxTestPlanCommandlet(engine.Commandlet): ...


class TestPolicy(unreal.UObject):
    DiscoveryMethod: EDiscovery
    HierarchicalCommands: Any
    Contact: str
    TestPlan: EGbxTestPlan

    def TestIntInRange(
        self,
        Value: int,
        Min: int,
        Max: int,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestIntCompare(
        self,
        Value: int,
        Other: int,
        Comparison: ECompare,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestFloatInRange(
        self,
        Value: float,
        Min: float,
        Max: float,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestFloatCompare(
        self,
        Value: float,
        Other: float,
        Comparison: ECompare,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
        Tolerance: float,
    ): ...
    def TestBoolIsTrue(
        self,
        Value: bool,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestBoolIsFalse(
        self,
        Value: bool,
        IssueType: ETestIssueType,
        IssueCategory: str,
        IssueMessage: str,
    ): ...
    def TestAssetTraits(self, Asset: unreal.UObject): ...
    def TestAssetAudit(self, Asset: unreal.UObject): ...
    def SetReportContext(
        self,
        WorldContextObject: unreal.UObject,
        AssetContexts: unreal.WrappedArray[gbx_probes_core.GbxProbeId],
    ): ...
    def ReportResult(
        self,
        bSucceeded: bool,
        IssueCategory: str,
        IssueMessage: str,
        AssetContext: gbx_probes_core.GbxProbeId,
        FailedIssueType: ETestIssueType,
    ): ...
    def ReportIssue(
        self, IssueType: ETestIssueType, IssueCategory: str, IssueMessage: str
    ): ...
    def PushAssetContext(self, ID: gbx_probes_core.GbxProbeId): ...
    def PopAssetContext(self, ID: gbx_probes_core.GbxProbeId): ...
    def OnRunTestCommand(self, TestCommand: str): ...
    def OnGetTestCommands(
        self,
        TestCommands: unreal.WrappedArray[str],
        PrettyNames: unreal.WrappedArray[str],
    ): ...
    def ClearSavedTestCommand(self): ...


class TestPolicyContent(TestPolicy):

    def OnValidForImport(self, ImportObject: unreal.UObject, Result: bool): ...


class TestPolicySimulation(TestPolicy):

    def StopPlay(self): ...
    def RunTestDrivers(
        self,
        TestDrivers: unreal.WrappedArray[unreal.UClass],
        Timeout: float,
        TimeLimit: float,
    ): ...
    def PlayTestMap(
        self,
        MapName: str,
        TestDrivers: unreal.WrappedArray[unreal.UClass],
        Timeout: float,
        TimeLimit: float,
        bLoadMapOnce: bool,
        bLoadMapIfNotLoaded: bool,
    ): ...
    def PlayMap(
        self,
        MapName: str,
        TestDrivers: unreal.WrappedArray[unreal.UClass],
        Timeout: float,
        TimeLimit: float,
    ): ...
    def OnMapTraveled(self, NewWorld: engine.World): ...
    def IntendToMapTravel(self, WillMapTravel: bool): ...
    def AddTestDriver(self, TestDriver: unreal.UClass): ...


class AutomationMenuFocusInfo:
    ClassName: str
    ObjectName: str
    ObjectNum: int
    Index: int
    Label: str
    ButtonType: gbx_ui.EGbxGFxButtonType
    IsButton: bool
    IsListCell: bool
    IsListItem: bool
    IsGridList: bool


class OptionalValue:
    bEnabled: bool


class OptionalName(OptionalValue):
    Value: str


class OptionalTextureLODGroup(OptionalName): ...


class OptionalTextureCompressionMethod(OptionalName): ...


class OptionalLODGroup(OptionalName): ...


class OptionalFloat(OptionalValue):
    Value: float


class OptionalInt32(OptionalValue):
    Value: int


class OptionalBool(OptionalValue):
    Value: bool


class MapParameters:
    Density: float
    Width: int
    Height: int
    bLighting: bool
    bSpecular: bool
    Gamma: float
    VolumeX: float
    VolumeY: float
    VolumeZ: float
    StartIndexX: int
    StartIndexY: int
    OutputPattern: str


class Regex: ...


class GbxTestHierarchicalCommandL1:
    DisplayName: str
    TestCommand: str
    SubCommands: unreal.WrappedArray[GbxTestHierarchicalCommandL2]


class GbxTestHierarchicalCommandL2:
    DisplayName: str
    TestCommand: str
    SubCommands: unreal.WrappedArray[GbxTestHierarchicalCommandL3]


class GbxTestHierarchicalCommandL3:
    DisplayName: str
    TestCommand: str


class TestInfoMaterial:
    AssetTraits: unreal.WrappedArray[AssetTraitMaterial]
    bUsedWithSkeletalMesh: bool
    bUsedWithParticleSprites: bool
    bUsedWithBeamTrails: bool
    bUsedWithMeshParticles: bool
    bUsedWithStaticLighting: bool
    bUsedWithMorphTargets: bool
    bUsedWithSplineMesh: bool
    bUsedWithInstancedStaticMeshes: bool
    bUsedWithClothing: bool
    bHasPhysMatSet: bool


class TestInfoMeshLOD:
    LODIndex: int
    TriangleCount: int
    VertexCount: int
    TexCoordCount: int
    SectionCount: int
    ScreenSize: float
    bHasDegenerateSections: bool


class TestInfoMesh:
    Bounds: core_uobject.BoxSphereBounds
    SocketCount: int
    HasSockets: bool


class TestInfoMeshLODSummary:
    LODCount: int
    LODMaxTriangleCount: int
    LODMaxVertexCount: int
    LODMinTexCoordCount: int
    LODMaxTexCoordCount: int
    LODMinSectionCount: int
    LODMaxSectionCount: int
    LODMinScreenSize: float
    LODMaxScreenSize: float


class TestInfoParticleSystem:
    AssetTraits: unreal.WrappedArray[AssetTraitParticleSystem]
    EmitterInfo: unreal.WrappedArray[TestInfoParticleEmitter]
    FixedRelativeBoundsSize: float
    UpdateTime: float
    WarmupTime: float
    LODDistanceCheckTime: float
    TemplateCost: float
    EmitterCount: int
    MinModuleCount: int
    MaxModuleCount: int
    LODCount: int
    AnimTrailDataCount: int
    GpuSpriteDataCount: int
    MeshDataCount: int
    RibbonOrBeamDataCount: int
    bUsesFixedRelativeBounds: bool
    bZAxisOrientedTowardsCamera: bool
    bAllEmittersHaveRequiredModules: bool
    bAllEmittersHaveLowestLOD: bool
    bKillFlagsNotSet: bool


class TestInfoParticleEmitter:
    EmitterIndex: int
    EmitterName: str
    SuperMaxDrawCount: int
    MinUnitScalar: float
    bHasLowestLOD: bool
    bHasAnimTrailData: bool
    bHasGpuSpriteData: bool
    bHasMeshData: bool
    bHasRibbonOrBeamData: bool
    bHasRequiredModule: bool
    bHasSpawnPerUnitModule: bool
    bHasLifetimeModule: bool
    bHasLightModule: bool
    bUseMaxDrawCountDisabled: bool
    bHasInfiniteMaxDrawCount: bool
    bHasInfiniteLifetime: bool
    bKillOnCompletedNotSet: bool
    bUseInverseSquaredFalloffSet: bool


class TestInfoSkeletalMesh:
    AssetTraits: unreal.WrappedArray[AssetTraitSkeletalMesh]
    Placeholder: bool


class TestInfoStaticMesh:
    AssetTraits: unreal.WrappedArray[AssetTraitStaticMesh]
    PrimitiveCount: int
    LightMapResolution: int
    LightMapIndex: int
    LODGroupName: str
    CastShadow: bool
    EnableCollision: bool


class TestInfoTexture:
    AssetTraits: unreal.WrappedArray[AssetTraitTexture]
    CompressionMethod: str
    LODGroup: str
    LODBias: int
    HasAlpha: bool
    HassRGB: bool


class GbxTestInputAction:
    InputEvent: int
    InputKey: input_core.Key
    StartTime: float
    LifeTime: float
    AmountDepressed: float
    AmountDelta: float


class EAutomationUIAction(enum.Enum):
    PressDigitalDown = 0
    PressDigitalLeft = 1
    PressFaceTop = 2
    PressLeftStick = 3


class EAutomationUIDirection(enum.Enum):
    Left = 0
    Down = 1
    EAutomationUIDirection_MAX = 2


class ECompare(enum.Enum):
    NE = 0
    GT = 1
    LT = 2


class ESnapshotExecOutput(enum.Enum):
    Failed = 0
    ESnapshotExecOutput_MAX = 1


class ESyntaxOption(enum.Enum):
    E_ECMASCRIPT = 0
    E_NOSUBS = 1
    E_OPTIMIZE = 2
    E_GREP = 3


class ETestIssueType(enum.Enum):
    Warning = 0
    Skipped = 1
    Critical = 2


class ECollectionType(enum.Enum):
    ECT_Private = 0
    ECT_Local = 1
    ECT_MAX = 2


class EGbxTestPlanOutput(enum.Enum):
    Console = 0
    Commandline = 1


class EGbxTestPlan(enum.Enum):
    Nightly = 0
    ABT = 1


class EDiscovery(enum.Enum):
    AllContent = 0
    Ignore = 1
    AllPersistentGameMaps = 2
    Custom = 3
