from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import engine
from . import gbx_runtime
from . import wwise_audio
from . import gbx_game_system_core
from . import level_sequence
from . import gbx_level_sequence
from . import oak_game
from . import gbx_ui
from . import gbx_inventory



class CSAction(unreal.UObject): ...


class CSActionInsertToken(CSAction): ...


class CSActionRemoveToken(CSAction): ...


class CSActionSwapTileAndToken(CSAction): ...


class CSCheatManager(unreal.UObject): ...


class CSCondition(gbx_runtime.GbxCondition): ...


class CSConsole(oak_game.AdvancedInteractiveObject):
    CSMenuData: gbx_ui.GbxMenuData



class CSConsoleProxy(oak_game.AdvancedInteractiveObjectProxy):
    CurrentOpponent: str
    def OnUnderParScoreReached(self): ...
    def OnSumbitPuzzleSolution(self, bIsOptimal: bool): ...
    def OnQuitCitizenScienceArcade(self): ...
    def OnParScoreReached(self): ...
    def OnOptimalScoreReached(self): ...
    def OnFirstPuzzleOfCurrentDifficulty(self): ...
    def OnEnterPuzzle(self): ...
    def OnDifficultyLevelCompleted(self): ...


class CSLevelData(gbx_runtime.GbxDataAsset):
    LevelInfos: unreal.WrappedArray[CSLevelInfo]



class CSPuzzleFeedbackManager(unreal.UObject):
    Settings: CSPuzzleFeedbackSettings
    Puzzle: GFxCSPuzzle
    TokenPool: GFxCSTokenPool
    ProgressBar: GFxCSProgressBar
    ProgressBarContainer: gbx_ui.GbxGFxObject
    PuzzleSession: CSPuzzleSession
    ParScoreTextFeedback: gbx_ui.GbxGFxObject
    ParScoreContainer: gbx_ui.GbxGFxObject
    ParScoreText: gbx_ui.GbxTextField
    CurrentScoreContainer: gbx_ui.GbxGFxObject
    CurrentScoreText: gbx_ui.GbxTextField
    HighScoreContainer: gbx_ui.GbxGFxObject
    HighScoreText: gbx_ui.GbxTextField
    ProgressBarBonusScoreContainer: gbx_ui.GbxGFxObject
    ProgressBarBonusScoreText: gbx_ui.GbxTextField
    BonusScoreContainer: gbx_ui.GbxGFxObject
    BonusScoreText: gbx_ui.GbxTextField
    NumTokensContainer: gbx_ui.GbxGFxObject
    NumTokensText: gbx_ui.GbxTextField
    OwningMenu: GFxCSPuzzleMenu
    TweeningTiles: unreal.WrappedArray[GFxCSPuzzleTile]



class CSPuzzleIntroManager(unreal.UObject):
    Settings: CSPuzzleIntroSettings



class CSPuzzleSession(unreal.UObject):
    PuzzleActions: unreal.WrappedArray[CSAction]
    TutorialPuzzle: TutorialPuzzle



class CSTutorialBPLib(engine.BlueprintFunctionLibrary):

    def UnblockCSPuzzleIntro(self): ...
    def UnblockCSPuzzleInputs(self): ...
    def StopHighlightCSTutorialElement(self, TutorialElement: ECSTutorialElement): ...
    def ShowCSTutorialTooltip(self, Tooltip: str): ...
    def ShowCSTutorialElement(self, TutorialElement: ECSTutorialElement): ...
    def HighlightCSTutorialElement(self, TutorialElement: ECSTutorialElement): ...
    def HideCSTutorialTooltip(self, Tooltip: str): ...
    def HideCSTutorialElement(self, TutorialElement: ECSTutorialElement): ...
    def CSWaitForScore(self, World: engine.World, ScoreCondition: ECSScoreCondition, LatentInfo: engine.LatentActionInfo): ...
    def BlockCSPuzzleIntro(self): ...
    def BlockCSPuzzleInputs(self): ...


class GFxCSButton(gbx_ui.GbxGFxListCell):
    HintText: gbx_ui.GbxTextField
    def OnInputDeviceChanged(self, NewInputDevice: gbx_ui.EGbxMenuInputDevice): ...


class GFxCSBoosterItem(GFxCSButton):
    DisplayName: gbx_ui.GbxTextField
    Description: gbx_ui.GbxTextField
    UnlockDescription: gbx_ui.GbxTextField
    Price: gbx_ui.GbxTextField
    Picture: gbx_ui.GbxGFxObject
    BoosterTimer: gbx_ui.GbxTextField



class GFxCSSubMenu(gbx_ui.GbxGFxMenuSwitcherSubmenu):
    Buttons: unreal.WrappedArray[GFxCSButton]



class GFxCSBoosterShopMenu(GFxCSSubMenu):
    BuyBoosterMessageHeader: str
    BuyBoosterMessage: str
    NumBoosterItemByRow: int
    BoosterData: oak_game.BoosterData
    BoosterList: gbx_ui.GbxGFxGridScrollingList
    ClickedBoosterItem: GFxCSBoosterItem
    def OnCSBucksAmountChanged(self, NewAmount: int): ...
    def OnConfirmPurchase(self, SourceDialog: oak_game.GbxGFxDialogBox, ChoiceNameId: str, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnBoosterItemClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...


class GFxCSHelpMenu(gbx_ui.GbxGFxMenu):
    RulesTab: GFxCSButton
    ControllerTab: GFxCSButton
    RulesContainer: gbx_ui.GbxGFxObject
    HelpContainer: gbx_ui.GbxGFxObject
    ControlsContainer: gbx_ui.GbxGFxObject
    CloseButton: GFxCSButton
    def OnCloseClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...


class GFxCSHUD(gbx_ui.GbxGFxMenuSwitcher):
    CitizenScienceGlobals: CSGlobals
    EchoWidget: oak_game.GFxEchologWidgetBase
    SubtitlesWidget: GFxCSSubtitles
    CSBucksAmountTextField: gbx_ui.GbxTextField
    MenuTitle: gbx_ui.GbxTextField
    BackButton: GFxCSButton
    HelpButton: GFxCSButton
    CSBucksObject: gbx_ui.GbxGFxObject
    PlayerIdPanel: gbx_ui.GbxGFxObject
    PlayerIdText: gbx_ui.GbxTextField
    def OnHelpClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnCSBucksAmountChanged(self, NewAmount: int): ...
    def OnBackClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...


class GFxCSLevelButton(GFxCSButton):
    NumLevel: gbx_ui.GbxTextField
    CharacterName: gbx_ui.GbxTextField
    LevelDifficulty: gbx_ui.GbxTextField
    PuzzleCompletedNum: gbx_ui.GbxTextField
    CharacterPicture: gbx_ui.GbxGFxObject
    ProgressBar: GFxCSProgressBar
    RewardPanel: gbx_ui.GbxGFxObject
    RewardText: gbx_ui.GbxTextField
    RewardPicture: gbx_ui.GbxGFxObject



class GFxCSLevelList(gbx_ui.GbxGFxGridScrollingList): ...


class GFxCSLevelSelectorMenu(GFxCSSubMenu):
    LevelData: CSLevelData
    DelayBeforeLoadingPuzzleMenu: float
    LevelList: GFxCSLevelList
    def OnLevelItemClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...


class GFxCSMainMenu(GFxCSSubMenu):
    PlayButton: GFxCSButton
    BuyBoosterButton: GFxCSButton
    WhatsThisButton: GFxCSButton
    QuitButton: GFxCSButton
    HelpButton: gbx_ui.GbxGFxButton
    DidYouKnowTitle: gbx_ui.GbxTextField
    DidYouKnowText: gbx_ui.GbxTextField
    SparkAuthenticatingDialog: oak_game.GbxGFxDialogBox
    def OnWhatsThisClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnPlayClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnErrorDialogClicked(self, SourceDialog: oak_game.GbxGFxDialogBox, ChoiceNameId: str, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnBuyBoosterClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...


class GFxCSProgressBar(gbx_ui.GbxGFxObject):
    MaskObj: gbx_ui.GbxGFxObject
    Marker: gbx_ui.GbxGFxObject



class GFxCSPuzzle(gbx_ui.GbxGFxObject):
    PuzzleGrid: GFxCSPuzzleGrid
    PuzzleGuide: GFxCSPuzzleGuide
    TokenPool: GFxCSTokenPool



class GFxCSPuzzleGrid(gbx_ui.GbxGFxObject):
    PuzzleTiles: unreal.WrappedArray[GFxCSTileArray]
    GridTiles: unreal.WrappedArray[GFxCSTileArray]
    GridMask: gbx_ui.GbxGFxObject
    LooseToken: GFxCSTokenTile



class GFxCSPuzzleGuide(gbx_ui.GbxGFxObject):
    GuideTiles: unreal.WrappedArray[GFxCSTileArray]



class GFxCSPuzzleMenu(GFxCSSubMenu):
    RequestingPuzzleDialog: oak_game.GbxGFxDialogBox
    PuzzleFeedbackManager: CSPuzzleFeedbackManager
    PuzzleIntroManager: CSPuzzleIntroManager
    Puzzle: GFxCSPuzzle
    ParScoreContainer: gbx_ui.GbxGFxObject
    ParScoreText: gbx_ui.GbxTextField
    CurrentScoreContainer: gbx_ui.GbxGFxObject
    CurrentScoreText: gbx_ui.GbxTextField
    HighScoreContainer: gbx_ui.GbxGFxObject
    HighScoreText: gbx_ui.GbxTextField
    DebugContainer: gbx_ui.GbxGFxObject
    DebugCurrentScoreText: gbx_ui.GbxTextField
    DebugRealCurrentScoreText: gbx_ui.GbxTextField
    DebugParScoreText: gbx_ui.GbxTextField
    DebugRealParScoreText: gbx_ui.GbxTextField
    DebugHighestScoreText: gbx_ui.GbxTextField
    DebugRealHighestScoreText: gbx_ui.GbxTextField
    DebugNbTokenLeftText: gbx_ui.GbxTextField
    DebugMatchingTileValueText: gbx_ui.GbxTextField
    DebugPerfectAlignmentModifierText: gbx_ui.GbxTextField
    DebugPuzzleId: gbx_ui.GbxTextField
    DebugTokenPos: gbx_ui.GbxTextField
    ParScoreTextFeedback: gbx_ui.GbxGFxObject
    ProgressBar: GFxCSProgressBar
    ProgressBarBonusScoreContainer: gbx_ui.GbxGFxObject
    ProgressBarBonusScoreText: gbx_ui.GbxTextField
    QuitButton: gbx_ui.GbxGFxButton
    QuickPassButton: gbx_ui.GbxGFxButton
    QuickPassButtonTxt: gbx_ui.GbxTextField
    SubmitButton: gbx_ui.GbxGFxButton
    SubmitButtonContainer: gbx_ui.GbxGFxObject
    ProgressBarContainer: gbx_ui.GbxGFxObject
    NotificationContainer: gbx_ui.GbxGFxObject
    NotificationText: gbx_ui.GbxTextField
    BonusScoreContainer: gbx_ui.GbxGFxObject
    BonusScoreText: gbx_ui.GbxTextField
    NumTokensPanel: gbx_ui.GbxGFxObject
    NumTokensContainer: gbx_ui.GbxGFxObject
    NumTokensText: gbx_ui.GbxTextField
    NumTotalTokensText: gbx_ui.GbxTextField
    def OnSubmitClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnQuitConfirmed(self, SourceDialog: oak_game.GbxGFxDialogBox, ChoiceNameId: str, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnQuickPassClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnErrorDialogClicked(self, SourceDialog: oak_game.GbxGFxDialogBox, ChoiceNameId: str, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnConfirmQuickPass(self, SourceDialog: oak_game.GbxGFxDialogBox, ChoiceNameId: str, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def GoToRewardScreenMenu(self): ...
    def GoToMainMenu(self): ...
    def extTokenTileTurnedOn(self): ...
    def extTokenTileTurnedOff(self): ...


class GFxCSPuzzleTile(gbx_ui.GbxGFxObject):
    AnimObject: gbx_ui.GbxGFxObject
    FocusedFeedback: gbx_ui.GbxGFxObject
    PlayerIds: unreal.WrappedArray[gbx_ui.GbxTextField]



class GFxCSGridTile(GFxCSPuzzleTile): ...


class GFxCSGuideTile(GFxCSPuzzleTile): ...


class GFxCSTokenTile(GFxCSPuzzleTile): ...


class GFxCSRewardScreenItem(gbx_ui.GbxGFxObject):
    ItemLabel: gbx_ui.GbxTextField
    ItemValue: gbx_ui.GbxTextField



class GFxCSRewardScreenMenu(GFxCSSubMenu):
    ProgressBarAnimSpeed: float
    DelayBetweenBonuses: float
    TextAnimationTime: float
    BaseRewardText: str
    ExtraPointText: str
    HighScoreMatchedText: str
    HighScoreBeatText: str
    PioneerText: str
    LevelData: CSLevelData
    PlayerCSBucksAmountText: gbx_ui.GbxTextField
    PuzzleCompletedTextPanel: gbx_ui.GbxGFxObject
    MainContentPanel: gbx_ui.GbxGFxObject
    ProgressTextPanel: gbx_ui.GbxGFxObject
    NumCompletedPuzzleTextPanel: gbx_ui.GbxGFxObject
    NumCompletedPuzzleText: gbx_ui.GbxTextField
    NumTargetPuzzleText: gbx_ui.GbxTextField
    ProgressBar: GFxCSProgressBar
    NewCustomizationAnimText: gbx_ui.GbxGFxObject
    AnimRewardPanel: gbx_ui.GbxGFxObject
    CharacterPicture: gbx_ui.GbxGFxObject
    CustomizationPicture: gbx_ui.GbxGFxObject
    PuzzleRewardItem: GFxCSRewardScreenItem
    TotalPuzzleRewardItem: GFxCSRewardScreenItem
    BonusItems: unreal.WrappedArray[GFxCSRewardScreenItem]
    ButtonList: gbx_ui.GbxGFxGridScrollingList
    def OnPlayNextCharacterClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnPlayAgainClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def OnMainMenuButtonClicked(self, PressedButton: gbx_ui.GbxGFxButton, InputInfo: gbx_ui.GbxMenuInputEvent): ...
    def GoToPuzzleMenu(self): ...
    def GoToMainMenu(self): ...
    def extRefreshNumCompletedPuzzle(self): ...
    def extPuzzleCompletedTextAnimDone(self): ...
    def extOnShowPuzzleRewardDone(self): ...
    def extOnShowBonusDone(self): ...
    def extNumCompletedPuzzleAnimDone(self): ...


class GFxCSStartScreen(gbx_ui.GbxGFxMenu): ...


class GFxCSSubtitles(gbx_ui.GbxGFxObject):
    ClosedCaptionLifetime: float
    MaxTextScalingForLargestBackground: float
    SubtitleBackgroundSizeMapping: unreal.WrappedArray[float]
    SubtitleField: gbx_ui.GbxTextField
    SubtitleBackground: gbx_ui.GbxGFxObject
    CurrentSubtitleLayoutType: oak_game.ESubtitleLayoutType
    ClosedCaptioningContainer: gbx_ui.GbxGFxObject
    ClosedCaptioningLines: unreal.WrappedArray[oak_game.ClosedCaptionEntry]
    SubtitleLines: unreal.WrappedArray[oak_game.SubtitleLine]
    CurrentSubtitleID: int
    bStopAfterCurrentSubtitle: bool
    bSubtitleChangePending: bool
    SubtitleLifetime: float
    CachedSubtitle: str



class GFxCSTokenPool(gbx_ui.GbxGFxObject):
    TokenPoolMask: gbx_ui.GbxGFxObject
    TokenTiles: unreal.WrappedArray[GFxCSTokenTile]
    GridTiles: unreal.WrappedArray[GFxCSGridTile]



class GFxCSWhatsThisMenu(GFxCSSubMenu):
    MovieSequencer: gbx_level_sequence.GbxLevelSequence
    MediaMaterial: engine.MaterialInterface
    MaterialName: str
    FadeName: str
    ParticleSystemName: str
    ScreenParticle: engine.ParticleSystem
    ParticleDepth: float
    FadeTime: float
    StartAudioSetupForMovieEvent: wwise_audio.WwiseEvent
    StopAudioSetupForMovieEvent: wwise_audio.WwiseEvent
    ScreenParticleManagerComponent: gbx_game_system_core.ScreenParticleManagerComponent
    MovieSequencePlayer: level_sequence.LevelSequencePlayer
    MovieSequenceActor: level_sequence.LevelSequenceActor
    def OnMovieMediaOpenFailed(self, FailedUrl: str): ...
    def OnMovieMediaOpened(self): ...
    def OnMovieEndReached(self): ...


class OakCitizenScienceManager(unreal.UObject):
    CurrentPuzzleSession: CSPuzzleSession
    CSGlobals: CSGlobals
    def GetCitizenScienceManager(self, ReturnValue: OakCitizenScienceManager) -> OakCitizenScienceManager: ...


class TutorialPuzzle(unreal.UObject):
    PuzzleLines: str
    PuzzleGuides: str
    NumberOfTokens: int
    ScoringMatchingTile: int
    ScoringPerfectAlignment: float
    ScoringParScore: int
    ScoringBestScore: int
    def OnTutorialStart(self): ...
    def OnTutorialEnd(self): ...
    def GetTutorialWorld(self, ReturnValue: engine.World) -> engine.World: ...


class CSGlobals(gbx_runtime.GbxDataAsset):
    CSBucksInventoryType: gbx_inventory.InventoryCategoryData
    SkinRewards: unreal.WrappedArray[oak_game.OakCustomizationData]
    HeadRewards: unreal.WrappedArray[oak_game.OakCustomizationData]
    HighScoreMatchedModifier: int
    HighScoreBeatenModifier: int
    DebugPuzzles: unreal.WrappedArray[DebugPuzzle]
    TutorialPuzzle: unreal.WrappedArray[unreal.UClass]
    LevelData: CSLevelData
    BoosterData: oak_game.BoosterData
    ShiftAccountRequiredTitle: str
    ShiftAccountRequiredText: str
    SubmitPuzzleErrorTitle: str
    SubmitPuzzleErrorText: str
    GetPuzzleErrorTitle: str
    GetPuzzleErrorText: str
    BuyBoosterMessageTitle: str
    BuyBoosterMessageText: str
    OverrideBoosterMessageTitle: str
    OverrideBoosterMessageText: str
    QuitPuzzleMessageTitle: str
    QuitPuzzleMessageBody: str
    QuickPassMessageTitle: str
    QuickPassMessageText: str
    DidYouKnowMessages: unreal.WrappedArray[str]



class CSLevelInfo:
    NameId: str
    RewardTextureName: str
    CharaterTextureName: str
    CustomizationTextureName: str
    CharacterAnimName: str
    CharacterName: str
    DifficultyLevel: str
    Target: int
    Reward: int
    HighestScoreMatchedModifier: int
    HighestScoreBeatenModifier: int
    PuzzleGridHeight: int
    PuzzleGridWidth: int
    CosmeticRewardCongratulationMessageTitle: str
    CosmeticRewardCongratulationMessageBody: str



class CSPuzzleFeedbackSettings:
    DelayBeforeFirstFeedback: float
    DelayBeforeProgressBarFeedback: float
    TimeToUpdateProgressBar: float
    TileSpeed: float
    TileMovementEasingFunction: ECSTweenEasingFunc
    DelayBetweenEachTileFlipped: float
    DelaytBetweenTileFlippingAndPerferctAlignmentAnim: float
    DelayBetweenEachTilePerfectAlignmentAnim: float



class CSPuzzleIntroSettings:
    DelayBeforeStartingIntro: float
    DelayBetweenEachPuzzleColumn: float
    DelayBetweenEachPuzzleTile: float
    EasingFunction: ECSTweenEasingFunc
    FallingSpeed: float



class GFxCSTileArray:
    Tiles: unreal.WrappedArray[GFxCSPuzzleTile]



class DebugPuzzle:
    PuzzleLines: str
    PuzzleGuides: str
    NumberOfTokens: int
    ScoringMatchingTile: int
    ScoringPerfectAlignment: float
    ScoringParScore: int
    ScoringBestScore: int



class EDialogEventEnum(enum.Enum):
    DE_SubmittedPuzzle = 0
    DE_MAX = 1
    DE_IdleLine = 2


class ECSScoreCondition(enum.Enum):
    UnderParScore = 0
    HighestScore = 1


class ECSTweenEasingFunc(enum.Enum):
    EaseInBack = 0
    SmoothStep = 1
    EaseInSine = 2


class ECitizenScienceManagerState(enum.Enum):
    StreamingManager_Initialized = 0
    StreamingManager_MAX = 1


class ECSTutorialElement(enum.Enum):
    SubmitButton = 0
    ScoreBar = 1
    ScoreDisplay = 2
