from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class BlueprintGameplayTagLibrary(engine.BlueprintFunctionLibrary):

    def RemoveGameplayTag(
        self, TagContainer: GameplayTagContainer, Tag: GameplayTag
    ) -> bool: ...
    def NotEqual_TagTag(self, A: GameplayTag, B: str) -> bool: ...
    def NotEqual_TagContainerTagContainer(
        self, A: GameplayTagContainer, B: str
    ) -> bool: ...
    def NotEqual_GameplayTagContainer(
        self, A: GameplayTagContainer, B: GameplayTagContainer
    ) -> bool: ...
    def NotEqual_GameplayTag(self, A: GameplayTag, B: GameplayTag) -> bool: ...
    def MatchesTag(
        self, TagOne: GameplayTag, TagTwo: GameplayTag, bExactMatch: bool
    ) -> bool: ...
    def MatchesAnyTags(
        self,
        TagOne: GameplayTag,
        OtherContainer: GameplayTagContainer,
        bExactMatch: bool,
    ) -> bool: ...
    def MakeLiteralGameplayTagContainer(
        self, Value: GameplayTagContainer
    ) -> GameplayTagContainer: ...
    def MakeLiteralGameplayTag(self, Value: GameplayTag) -> GameplayTag: ...
    def MakeGameplayTagQuery(self, TagQuery: GameplayTagQuery) -> GameplayTagQuery: ...
    def MakeGameplayTagContainerFromTag(
        self, SingleTag: GameplayTag
    ) -> GameplayTagContainer: ...
    def MakeGameplayTagContainerFromArray(
        self, GameplayTags: unreal.WrappedArray[GameplayTag]
    ) -> GameplayTagContainer: ...
    def IsGameplayTagValid(self, GameplayTag: GameplayTag) -> bool: ...
    def HasTag(
        self, TagContainer: GameplayTagContainer, Tag: GameplayTag, bExactMatch: bool
    ) -> bool: ...
    def HasAnyTags(
        self,
        TagContainer: GameplayTagContainer,
        OtherContainer: GameplayTagContainer,
        bExactMatch: bool,
    ) -> bool: ...
    def HasAllTags(
        self,
        TagContainer: GameplayTagContainer,
        OtherContainer: GameplayTagContainer,
        bExactMatch: bool,
    ) -> bool: ...
    def HasAllMatchingGameplayTags(
        self, TagContainerInterface: Any, OtherContainer: GameplayTagContainer
    ) -> bool: ...
    def GetTagName(self, GameplayTag: GameplayTag) -> str: ...
    def GetNumGameplayTagsInContainer(
        self, TagContainer: GameplayTagContainer
    ) -> int: ...
    def GetDebugStringFromGameplayTagContainer(
        self, TagContainer: GameplayTagContainer
    ) -> str: ...
    def GetDebugStringFromGameplayTag(self, GameplayTag: GameplayTag) -> str: ...
    def GetAllActorsOfClassMatchingTagQuery(
        self,
        WorldContextObject: unreal.UObject,
        ActorClass: unreal.UClass,
        GameplayTagQuery: GameplayTagQuery,
        OutActors: unreal.WrappedArray[engine.Actor],
    ): ...
    def EqualEqual_GameplayTagContainer(
        self, A: GameplayTagContainer, B: GameplayTagContainer
    ) -> bool: ...
    def EqualEqual_GameplayTag(self, A: GameplayTag, B: GameplayTag) -> bool: ...
    def DoesTagAssetInterfaceHaveTag(
        self, TagContainerInterface: Any, Tag: GameplayTag
    ) -> bool: ...
    def DoesContainerMatchTagQuery(
        self, TagContainer: GameplayTagContainer, TagQuery: GameplayTagQuery
    ) -> bool: ...
    def BreakGameplayTagContainer(
        self,
        GameplayTagContainer: GameplayTagContainer,
        GameplayTags: unreal.WrappedArray[GameplayTag],
    ): ...
    def AppendGameplayTagContainers(
        self,
        InOutTagContainer: GameplayTagContainer,
        InTagContainer: GameplayTagContainer,
    ): ...
    def AddGameplayTag(self, TagContainer: GameplayTagContainer, Tag: GameplayTag): ...


class GameplayTagAssetInterface(core_uobject.Interface):

    def HasMatchingGameplayTag(self, TagToCheck: GameplayTag) -> bool: ...
    def HasAnyMatchingGameplayTags(
        self, TagContainer: GameplayTagContainer
    ) -> bool: ...
    def HasAllMatchingGameplayTags(
        self, TagContainer: GameplayTagContainer
    ) -> bool: ...
    def GetOwnedGameplayTags(self, TagContainer: GameplayTagContainer): ...


class EditableGameplayTagQuery(unreal.UObject):
    UserDescription: str
    RootExpression: EditableGameplayTagQueryExpression
    TagQueryExportText_Helper: GameplayTagQuery


class EditableGameplayTagQueryExpression(unreal.UObject): ...


class EditableGameplayTagQueryExpression_AnyTagsMatch(
    EditableGameplayTagQueryExpression
):
    Tags: GameplayTagContainer


class EditableGameplayTagQueryExpression_AllTagsMatch(
    EditableGameplayTagQueryExpression
):
    Tags: GameplayTagContainer


class EditableGameplayTagQueryExpression_NoTagsMatch(
    EditableGameplayTagQueryExpression
):
    Tags: GameplayTagContainer


class EditableGameplayTagQueryExpression_AnyExprMatch(
    EditableGameplayTagQueryExpression
):
    Expressions: unreal.WrappedArray[EditableGameplayTagQueryExpression]


class EditableGameplayTagQueryExpression_AllExprMatch(
    EditableGameplayTagQueryExpression
):
    Expressions: unreal.WrappedArray[EditableGameplayTagQueryExpression]


class EditableGameplayTagQueryExpression_NoExprMatch(
    EditableGameplayTagQueryExpression
):
    Expressions: unreal.WrappedArray[EditableGameplayTagQueryExpression]


class GameplayTagsManager(unreal.UObject):
    TagSources: unreal.WrappedArray[GameplayTagSource]
    RestrictedGameplayTagTables: unreal.WrappedArray[engine.DataTable]
    GameplayTagTables: unreal.WrappedArray[engine.DataTable]


class GameplayTagsList(unreal.UObject):
    ConfigFileName: str
    GameplayTagList: unreal.WrappedArray[GameplayTagTableRow]


class RestrictedGameplayTagsList(unreal.UObject):
    ConfigFileName: str
    RestrictedGameplayTagList: unreal.WrappedArray[RestrictedGameplayTagTableRow]


class GameplayTagsSettings(GameplayTagsList):
    ImportTagsFromConfig: bool
    WarnOnInvalidTags: bool
    CategoryRemapping: unreal.WrappedArray[GameplayTagCategoryRemap]
    FastReplication: bool
    GameplayTagTableList: unreal.WrappedArray[core_uobject.SoftObjectPath]
    GameplayTagRedirects: unreal.WrappedArray[GameplayTagRedirect]
    CommonlyReplicatedTags: unreal.WrappedArray[str]
    NumBitsForContainerSize: int
    NetIndexFirstBitSegment: int
    RestrictedConfigFiles: unreal.WrappedArray[RestrictedConfigInfo]


class GameplayTagsDeveloperSettings(unreal.UObject):
    DeveloperConfigName: str


class GameplayTag:
    TagName: str


class GameplayTagContainer:
    GameplayTags: unreal.WrappedArray[GameplayTag]
    ParentTags: unreal.WrappedArray[GameplayTag]


class GameplayTagQuery:
    TokenStreamVersion: int
    TagDictionary: unreal.WrappedArray[GameplayTag]
    QueryTokenStream: unreal.WrappedArray[int]
    UserDescription: str
    AutoDescription: str


class GameplayTagCreationWidgetHelper: ...


class GameplayTagReferenceHelper: ...


class GameplayTagNode: ...


class GameplayTagSource:
    SourceName: str
    SourceType: EGameplayTagSourceType
    SourceTagList: GameplayTagsList
    SourceRestrictedTagList: RestrictedGameplayTagsList


class GameplayTagTableRow(engine.TableRowBase):
    Tag: str
    DevComment: str


class RestrictedGameplayTagTableRow(GameplayTagTableRow):
    bAllowNonRestrictedChildren: bool


class RestrictedConfigInfo:
    RestrictedConfigName: str
    Owners: unreal.WrappedArray[str]


class GameplayTagCategoryRemap:
    BaseCategory: str
    RemapCategories: unreal.WrappedArray[str]


class GameplayTagRedirect:
    OldTagName: str
    NewTagName: str


class EGameplayTagQueryExprType(enum.Enum):
    AllTagsMatch = 0
    AnyTagsMatch = 1
    AnyExprMatch = 2


class EGameplayContainerMatchType(enum.Enum):
    EGameplayContainerMatchType_MAX = 0
    All = 1


class EGameplayTagMatchType(enum.Enum):
    IncludeParentTags = 0
    EGameplayTagMatchType_MAX = 1


class EGameplayTagSourceType(enum.Enum):
    DefaultTagList = 0
    TagList = 1
    DataTable = 2
