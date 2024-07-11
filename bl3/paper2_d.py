from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import slate_core


class MaterialExpressionSpriteTextureSampler(
    engine.MaterialExpressionTextureSampleParameter2D
):
    bSampleAdditionalTextures: bool
    AdditionalSlotIndex: int
    SlotDisplayName: str


class PaperCharacter(engine.Character):
    Sprite: PaperFlipbookComponent


class PaperFlipbook(unreal.UObject):
    FramesPerSecond: float
    KeyFrames: unreal.WrappedArray[PaperFlipbookKeyFrame]
    DefaultMaterial: engine.MaterialInterface
    CollisionSource: int

    def IsValidKeyFrameIndex(self, Index: int) -> bool: ...
    def GetTotalDuration(self) -> float: ...
    def GetSpriteAtTime(self, Time: float, bClampToEnds: bool) -> PaperSprite: ...
    def GetSpriteAtFrame(self, FrameIndex: int) -> PaperSprite: ...
    def GetNumKeyFrames(self) -> int: ...
    def GetNumFrames(self) -> int: ...
    def GetKeyFrameIndexAtTime(self, Time: float, bClampToEnds: bool) -> int: ...


class PaperFlipbookActor(engine.Actor):
    RenderComponent: PaperFlipbookComponent


class PaperFlipbookComponent(engine.MeshComponent):
    SourceFlipbook: PaperFlipbook
    Material: engine.MaterialInterface
    PlayRate: float
    bLooping: bool
    bReversePlayback: bool
    bPlaying: bool
    AccumulatedTime: float
    CachedFrameIndex: int
    SpriteColor: core_uobject.LinearColor
    CachedBodySetup: engine.BodySetup
    OnFinishedPlaying: Any

    def Stop(self): ...
    def SetSpriteColor(self, NewColor: core_uobject.LinearColor): ...
    def SetPlayRate(self, NewRate: float): ...
    def SetPlaybackPositionInFrames(self, NewFramePosition: int, bFireEvents: bool): ...
    def SetPlaybackPosition(self, NewPosition: float, bFireEvents: bool): ...
    def SetNewTime(self, NewTime: float): ...
    def SetLooping(self, bNewLooping: bool): ...
    def SetFlipbook(self, NewFlipbook: PaperFlipbook) -> bool: ...
    def ReverseFromEnd(self): ...
    def Reverse(self): ...
    def PlayFromStart(self): ...
    def Play(self): ...
    def OnRep_SourceFlipbook(self, OldFlipbook: PaperFlipbook): ...
    def IsReversing(self) -> bool: ...
    def IsPlaying(self) -> bool: ...
    def IsLooping(self) -> bool: ...
    def GetPlayRate(self) -> float: ...
    def GetPlaybackPositionInFrames(self) -> int: ...
    def GetPlaybackPosition(self) -> float: ...
    def GetFlipbookLengthInFrames(self) -> int: ...
    def GetFlipbookLength(self) -> float: ...
    def GetFlipbookFramerate(self) -> float: ...
    def GetFlipbook(self) -> PaperFlipbook: ...


class PaperGroupedSpriteActor(engine.Actor):
    RenderComponent: PaperGroupedSpriteComponent


class PaperGroupedSpriteComponent(engine.MeshComponent):
    InstanceMaterials: unreal.WrappedArray[engine.MaterialInterface]
    PerInstanceSpriteData: unreal.WrappedArray[SpriteInstanceData]

    def UpdateInstanceTransform(
        self,
        InstanceIndex: int,
        NewInstanceTransform: core_uobject.Transform,
        bWorldSpace: bool,
        bMarkRenderStateDirty: bool,
        bTeleport: bool,
    ) -> bool: ...
    def UpdateInstanceColor(
        self,
        InstanceIndex: int,
        NewInstanceColor: core_uobject.LinearColor,
        bMarkRenderStateDirty: bool,
    ) -> bool: ...
    def SortInstancesAlongAxis(self, WorldSpaceSortAxis: core_uobject.Vector): ...
    def RemoveInstance(self, InstanceIndex: int) -> bool: ...
    def GetInstanceTransform(
        self,
        InstanceIndex: int,
        OutInstanceTransform: core_uobject.Transform,
        bWorldSpace: bool,
    ) -> bool: ...
    def GetInstanceCount(self) -> int: ...
    def ClearInstances(self): ...
    def AddInstance(
        self,
        Transform: core_uobject.Transform,
        Sprite: PaperSprite,
        bWorldSpace: bool,
        Color: core_uobject.LinearColor,
    ) -> int: ...


class PaperRuntimeSettings(unreal.UObject):
    bEnableSpriteAtlasGroups: bool
    bEnableTerrainSplineEditing: bool
    bResizeSpriteDataToMatchTextures: bool


class PaperSprite(unreal.UObject):
    SourceUV: core_uobject.Vector2D
    SourceDimension: core_uobject.Vector2D
    SourceTexture: engine.Texture2D
    AdditionalSourceTextures: unreal.WrappedArray[engine.Texture]
    BakedSourceUV: core_uobject.Vector2D
    BakedSourceDimension: core_uobject.Vector2D
    BakedSourceTexture: engine.Texture2D
    DefaultMaterial: engine.MaterialInterface
    AlternateMaterial: engine.MaterialInterface
    Sockets: unreal.WrappedArray[PaperSpriteSocket]
    SpriteCollisionDomain: int
    PixelsPerUnrealUnit: float
    BodySetup: engine.BodySetup
    AlternateMaterialSplitIndex: int
    BakedRenderData: unreal.WrappedArray[core_uobject.Vector4]


class PaperSpriteActor(engine.Actor):
    RenderComponent: PaperSpriteComponent


class PaperSpriteAtlas(unreal.UObject): ...


class PaperSpriteBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def MakeBrushFromSprite(
        self, Sprite: PaperSprite, Width: int, Height: int
    ) -> slate_core.SlateBrush: ...


class PaperSpriteComponent(engine.MeshComponent):
    SourceSprite: PaperSprite
    MaterialOverride: engine.MaterialInterface
    SpriteColor: core_uobject.LinearColor

    def SetSpriteColor(self, NewColor: core_uobject.LinearColor): ...
    def SetSprite(self, NewSprite: PaperSprite) -> bool: ...
    def GetSprite(self) -> PaperSprite: ...


class PaperTerrainActor(engine.Actor):
    DummyRoot: engine.SceneComponent
    SplineComponent: PaperTerrainSplineComponent
    RenderComponent: PaperTerrainComponent


class PaperTerrainComponent(engine.PrimitiveComponent):
    TerrainMaterial: PaperTerrainMaterial
    bClosedSpline: bool
    bFilledSpline: bool
    AssociatedSpline: PaperTerrainSplineComponent
    RandomSeed: int
    SegmentOverlapAmount: float
    TerrainColor: core_uobject.LinearColor
    ReparamStepsPerSegment: int
    SpriteCollisionDomain: int
    CollisionThickness: float
    CachedBodySetup: engine.BodySetup

    def SetTerrainColor(self, NewColor: core_uobject.LinearColor): ...


class PaperTerrainMaterial(engine.DataAsset):
    Rules: unreal.WrappedArray[PaperTerrainMaterialRule]
    InteriorFill: PaperSprite


class PaperTerrainSplineComponent(engine.SplineComponent): ...


class PaperTileLayer(unreal.UObject):
    LayerName: str
    LayerWidth: int
    LayerHeight: int
    bHiddenInGame: bool
    bLayerCollides: bool
    bOverrideCollisionThickness: bool
    bOverrideCollisionOffset: bool
    CollisionThicknessOverride: float
    CollisionOffsetOverride: float
    LayerColor: core_uobject.LinearColor
    AllocatedWidth: int
    AllocatedHeight: int
    AllocatedCells: unreal.WrappedArray[PaperTileInfo]
    TileSet: PaperTileSet
    AllocatedGrid: unreal.WrappedArray[int]


class PaperTileMap(unreal.UObject):
    MapWidth: int
    MapHeight: int
    TileWidth: int
    TileHeight: int
    PixelsPerUnrealUnit: float
    SeparationPerTileX: float
    SeparationPerTileY: float
    SeparationPerLayer: float
    SelectedTileSet: Any
    Material: engine.MaterialInterface
    TileLayers: unreal.WrappedArray[PaperTileLayer]
    CollisionThickness: float
    SpriteCollisionDomain: int
    ProjectionMode: int
    HexSideLength: int
    BodySetup: engine.BodySetup
    LayerNameIndex: int


class PaperTileMapActor(engine.Actor):
    RenderComponent: PaperTileMapComponent


class PaperTileMapComponent(engine.MeshComponent):
    MapWidth: int
    MapHeight: int
    TileWidth: int
    TileHeight: int
    DefaultLayerTileSet: PaperTileSet
    Material: engine.MaterialInterface
    TileLayers: unreal.WrappedArray[PaperTileLayer]
    TileMapColor: core_uobject.LinearColor
    UseSingleLayerIndex: int
    bUseSingleLayer: bool
    TileMap: PaperTileMap

    def SetTileMapColor(self, NewColor: core_uobject.LinearColor): ...
    def SetTileMap(self, NewTileMap: PaperTileMap) -> bool: ...
    def SetTile(self, X: int, Y: int, Layer: int, NewValue: PaperTileInfo): ...
    def SetLayerColor(self, NewColor: core_uobject.LinearColor, Layer: int): ...
    def SetLayerCollision(
        self,
        Layer: int,
        bHasCollision: bool,
        bOverrideThickness: bool,
        CustomThickness: float,
        bOverrideOffset: bool,
        CustomOffset: float,
        bRebuildCollision: bool,
    ): ...
    def SetDefaultCollisionThickness(
        self, Thickness: float, bRebuildCollision: bool
    ): ...
    def ResizeMap(self, NewWidthInTiles: int, NewHeightInTiles: int): ...
    def RebuildCollision(self): ...
    def OwnsTileMap(self) -> bool: ...
    def MakeTileMapEditable(self): ...
    def GetTilePolygon(
        self,
        TileX: int,
        TileY: int,
        Points: unreal.WrappedArray[core_uobject.Vector],
        LayerIndex: int,
        bWorldSpace: bool,
    ): ...
    def GetTileMapColor(self) -> core_uobject.LinearColor: ...
    def GetTileCornerPosition(
        self, TileX: int, TileY: int, LayerIndex: int, bWorldSpace: bool
    ) -> core_uobject.Vector: ...
    def GetTileCenterPosition(
        self, TileX: int, TileY: int, LayerIndex: int, bWorldSpace: bool
    ) -> core_uobject.Vector: ...
    def GetTile(self, X: int, Y: int, Layer: int) -> PaperTileInfo: ...
    def GetMapSize(self, MapWidth: int, MapHeight: int, NumLayers: int): ...
    def GetLayerColor(self, Layer: int) -> core_uobject.LinearColor: ...
    def CreateNewTileMap(
        self,
        MapWidth: int,
        MapHeight: int,
        TileWidth: int,
        TileHeight: int,
        PixelsPerUnrealUnit: float,
        bCreateLayer: bool,
    ): ...
    def AddNewLayer(self) -> PaperTileLayer: ...


class PaperTileSet(unreal.UObject):
    TileSize: core_uobject.IntPoint
    TileSheet: engine.Texture2D
    AdditionalSourceTextures: unreal.WrappedArray[engine.Texture]
    BorderMargin: IntMargin
    PerTileSpacing: core_uobject.IntPoint
    DrawingOffset: core_uobject.IntPoint
    WidthInTiles: int
    HeightInTiles: int
    AllocatedWidth: int
    AllocatedHeight: int
    PerTileData: unreal.WrappedArray[PaperTileMetadata]
    Terrains: unreal.WrappedArray[PaperTileSetTerrain]
    TileWidth: int
    TileHeight: int
    Margin: int
    Spacing: int


class TileMapBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def MakeTile(
        self,
        TileIndex: int,
        TileSet: PaperTileSet,
        bFlipH: bool,
        bFlipV: bool,
        bFlipD: bool,
    ) -> PaperTileInfo: ...
    def GetTileUserData(self, Tile: PaperTileInfo) -> str: ...
    def GetTileTransform(self, Tile: PaperTileInfo) -> core_uobject.Transform: ...
    def BreakTile(
        self,
        Tile: PaperTileInfo,
        TileIndex: int,
        TileSet: PaperTileSet,
        bFlipH: bool,
        bFlipV: bool,
        bFlipD: bool,
    ): ...


class IntMargin:
    Left: int
    Top: int
    Right: int
    Bottom: int


class PaperFlipbookKeyFrame:
    Sprite: PaperSprite
    FrameRun: int


class SpriteInstanceData:
    Transform: core_uobject.Matrix
    SourceSprite: PaperSprite
    VertexColor: core_uobject.Color
    MaterialIndex: int


class PaperSpriteSocket:
    LocalTransform: core_uobject.Transform
    SocketName: str


class PaperSpriteAtlasSlot:
    SpriteRef: Any
    AtlasIndex: int
    X: int
    Y: int
    Width: int
    Height: int


class PaperTerrainMaterialRule:
    StartCap: PaperSprite
    Body: unreal.WrappedArray[PaperSprite]
    EndCap: PaperSprite
    MinimumAngle: float
    MaximumAngle: float
    bEnableCollision: bool
    CollisionOffset: float
    DrawOrder: int


class PaperTileInfo:
    TileSet: PaperTileSet
    PackedTileIndex: int


class PaperTileSetTerrain:
    TerrainName: str
    CenterTileIndex: int


class PaperTileMetadata:
    UserDataName: str
    CollisionData: SpriteGeometryCollection
    TerrainMembership: int


class SpriteGeometryCollection:
    Shapes: unreal.WrappedArray[SpriteGeometryShape]
    GeometryType: int
    PixelsPerSubdivisionX: int
    PixelsPerSubdivisionY: int
    bAvoidVertexMerging: bool
    AlphaThreshold: float
    DetailAmount: float
    SimplifyEpsilon: float


class SpriteGeometryShape:
    ShapeType: ESpriteShapeType
    Vertices: unreal.WrappedArray[core_uobject.Vector2D]
    BoxSize: core_uobject.Vector2D
    BoxPosition: core_uobject.Vector2D
    Rotation: float
    bNegativeWinding: bool


class SpriteDrawCallRecord:
    Destination: core_uobject.Vector
    BaseTexture: engine.Texture
    Color: core_uobject.Color


class SpriteAssetInitParameters: ...


class EFlipbookCollisionMode(enum.Enum):
    FirstFrameCollision = 0
    EachFrameCollision = 1


class EPaperSpriteAtlasPadding(enum.Enum):
    PadWithZero = 0
    EPaperSpriteAtlasPadding_MAX = 1


class ETileMapProjectionMode(enum.Enum):
    IsometricDiamond = 0
    IsometricStaggered = 1
    ETileMapProjectionMode_MAX = 2


class ESpritePivotMode(enum.Enum):
    Center_Center = 0
    Top_Center = 1
    Top_Right = 2
    Bottom_Right = 3


class ESpritePolygonMode(enum.Enum):
    TightBoundingBox = 0
    ShrinkWrapped = 1
    Diced = 2


class ESpriteShapeType(enum.Enum):
    Polygon = 0
    Circle = 1


class ESpriteCollisionMode(enum.Enum):
    Use2DPhysics = 0
    Use3DPhysics = 1
