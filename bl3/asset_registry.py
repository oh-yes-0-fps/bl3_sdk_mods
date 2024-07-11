from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class AssetRegistryImpl(unreal.UObject): ...


class AssetRegistryHelpers(unreal.UObject):

    def ToSoftObjectPath(
        self, InAssetData: AssetData
    ) -> core_uobject.SoftObjectPath: ...
    def SetFilterTagsAndValues(
        self, InFilter: ARFilter, InTagsAndValues: unreal.WrappedArray[TagAndValue]
    ) -> ARFilter: ...
    def IsValid(self, InAssetData: AssetData) -> bool: ...
    def IsUAsset(self, InAssetData: AssetData) -> bool: ...
    def IsRedirector(self, InAssetData: AssetData) -> bool: ...
    def IsAssetLoaded(self, InAssetData: AssetData) -> bool: ...
    def GetTagValue(
        self, InAssetData: AssetData, InTagName: str, OutTagValue: str
    ) -> bool: ...
    def GetFullName(self, InAssetData: AssetData) -> str: ...
    def GetExportTextName(self, InAssetData: AssetData) -> str: ...
    def GetClass(self, InAssetData: AssetData) -> unreal.UClass: ...
    def GetAssetRegistry(self) -> Any: ...
    def GetAsset(self, InAssetData: AssetData) -> unreal.UObject: ...
    def CreateAssetData(
        self, InAsset: unreal.UObject, bAllowBlueprintClass: bool
    ) -> AssetData: ...


class AssetRegistry(core_uobject.Interface):

    def SearchAllAssets(self, bSynchronousSearch: bool): ...
    def ScanPathsSynchronous(
        self, InPaths: unreal.WrappedArray[str], bForceRescan: bool
    ): ...
    def ScanModifiedAssetFiles(self, InFilePaths: unreal.WrappedArray[str]): ...
    def ScanFilesSynchronous(
        self, InFilePaths: unreal.WrappedArray[str], bForceRescan: bool
    ): ...
    def RunAssetsThroughFilter(
        self, AssetDataList: unreal.WrappedArray[AssetData], Filter: ARFilter
    ): ...
    def PrioritizeSearchPath(self, PathToPrioritize: str): ...
    def IsLoadingAssets(self) -> bool: ...
    def HasAssets(self, PackagePath: str, bRecursive: bool) -> bool: ...
    def GetSubPaths(
        self, InBasePath: str, OutPathList: unreal.WrappedArray[str], bInRecurse: bool
    ): ...
    def GetAssetsByPath(
        self,
        PackagePath: str,
        OutAssetData: unreal.WrappedArray[AssetData],
        bRecursive: bool,
        bIncludeOnlyOnDiskAssets: bool,
    ) -> bool: ...
    def GetAssetsByPackageName(
        self,
        PackageName: str,
        OutAssetData: unreal.WrappedArray[AssetData],
        bIncludeOnlyOnDiskAssets: bool,
    ) -> bool: ...
    def GetAssetsByClass(
        self,
        ClassName: str,
        OutAssetData: unreal.WrappedArray[AssetData],
        bSearchSubClasses: bool,
    ) -> bool: ...
    def GetAssets(
        self, Filter: ARFilter, OutAssetData: unreal.WrappedArray[AssetData]
    ) -> bool: ...
    def GetAssetByObjectPath(
        self, ObjectPath: str, bIncludeOnlyOnDiskAssets: bool
    ) -> AssetData: ...
    def GetAllCachedPaths(self, OutPathList: unreal.WrappedArray[str]): ...
    def GetAllAssets(
        self,
        OutAssetData: unreal.WrappedArray[AssetData],
        bIncludeOnlyOnDiskAssets: bool,
    ) -> bool: ...


class ARFilter:
    PackageNames: unreal.WrappedArray[str]
    PackagePaths: unreal.WrappedArray[str]
    ObjectPaths: unreal.WrappedArray[str]
    ClassNames: unreal.WrappedArray[str]
    RecursiveClassesExclusionSet: Any
    bRecursivePaths: bool
    bRecursiveClasses: bool
    bIncludeOnlyOnDiskAssets: bool
    bExcludeLocalizedAssets: bool


class AssetBundleData:
    Bundles: unreal.WrappedArray[AssetBundleEntry]


class AssetBundleEntry:
    BundleScope: core_uobject.PrimaryAssetId
    BundleName: str
    BundleAssets: unreal.WrappedArray[core_uobject.SoftObjectPath]


class AssetData:
    ObjectPath: str
    PackageName: str
    PackagePath: str
    AssetName: str
    AssetClass: str
    AssetDateModified: core_uobject.DateTime


class TagAndValue:
    Tag: str
    Value: str
