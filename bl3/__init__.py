from . import core_uobject
from . import bifrost
from . import cohtml_plugin
from . import engine
from . import umg
from . import coherent_rendering_plugin
from . import online_subsystem
from . import online_subsystem_utils
from . import gbx_runtime
from . import audio_mixer
from . import socket_subsystem_spark
from . import wwise_audio
from . import movie_scene
from . import gbx_audio
from . import gbx_fluid_simulation
from . import gbx_dialog
from . import face_fx
from . import apex_destruction
from . import logitech_arx
from . import gbx_test
from . import gbx_input
from . import gbx_probes
from . import gbx_jira
from . import significance_manager
from . import gbx_twitch
from . import gbx_mixer
from . import gbx_ai
from . import aimodule
from . import gameplay_tasks
from . import gbx_game_system_core
from . import navigation_system
from . import gbx_nav
from . import gbx_spawn
from . import level_sequence
from . import gbx_level_sequence
from . import triton_runtime
from . import gbx_shift_overlay
from . import socket_subsystem_epic
from . import paper2_d
from . import aclplugin
from . import live_link
from . import light_propagation_volume_runtime
from . import facial_animation
from . import editable_mesh
from . import datasmith_content
from . import geometry_cache
from . import geometry_cache_tracks
from . import apple_image_utils
from . import apple_vision
from . import gbx_blocking_volumes
from . import gbx_blueprint_function_libraries
from . import gbx_level_editor_preview
from . import gbx_perf_scope
from . import gbx_time_of_day
from . import media_assets
from . import img_media
from . import img_media_factory
from . import linear_timecode
from . import media_compositing
from . import wmf_media_factory
from . import tcp_messaging
from . import udp_messaging
from . import actor_sequence
from . import audio_capture
from . import audio_mixer_wwise
from . import cable_component
from . import custom_mesh_component
from . import phys_xvehicles
from . import procedural_mesh_component
from . import va_rest_plugin
from . import oak_game
from . import scaleform_ui
from . import gbx_ui
from . import gbx_inventory
from . import gbx_camera_modes
from . import gbx_dynamic_room
from . import gbx_weapon
from . import gbx_abilities
from . import gbx_mission
from . import gbx_travel_station
from . import replication_graph
from . import gbx_vehicle
from . import oak_cs
from . import input_core
from . import slate_core
from . import slate
from . import material_shader_quality_settings
from . import engine_settings
from . import head_mounted_display
from . import foliage
from . import landscape
from . import time_management
from . import anim_graph_runtime
from . import movie_scene_tracks
from . import movie_player
from . import cinematic_camera
from . import asset_registry
from . import gameplay_tags
from . import packet_handler
from . import mesh_description
from . import clothing_system_runtime_interface
from . import eye_tracker
from . import json_utilities
from . import movie_scene_capture
from . import mrmesh
from . import overlay
from . import clothing_system_runtime
from . import gbx_spark
from . import gbx_feedback
from . import gbx_perf_analytics
from . import gbx_probes_core
from . import gbx_anim_runtime
from . import live_link_interface
from . import gbx_destruction
from . import gbx_fluid_surface
from . import gbx_status_effects
from . import oak_destruction
from . import immediate_physics
from . import renderer
from . import animation_core
from . import property_path
from . import engine_messages
from . import audio_platform_configuration
from . import serialization
from . import session_messages
from . import gbx_anim_runtime_base
from . import gbx_streaming_interaction
from . import live_link_message_bus_framework
from . import bp
from . import vivox_core
__all__: tuple[str, ...] = (
    "core_uobject",
    "bifrost",
    "cohtml_plugin",
    "engine",
    "umg",
    "coherent_rendering_plugin",
    "online_subsystem",
    "online_subsystem_utils",
    "gbx_runtime",
    "audio_mixer",
    "socket_subsystem_spark",
    "wwise_audio",
    "movie_scene",
    "gbx_audio",
    "gbx_fluid_simulation",
    "gbx_dialog",
    "face_fx",
    "apex_destruction",
    "logitech_arx",
    "gbx_test",
    "gbx_input",
    "gbx_probes",
    "gbx_jira",
    "significance_manager",
    "gbx_twitch",
    "gbx_mixer",
    "gbx_ai",
    "aimodule",
    "gameplay_tasks",
    "gbx_game_system_core",
    "navigation_system",
    "gbx_nav",
    "gbx_spawn",
    "level_sequence",
    "gbx_level_sequence",
    "triton_runtime",
    "gbx_shift_overlay",
    "socket_subsystem_epic",
    "paper2_d",
    "aclplugin",
    "live_link",
    "light_propagation_volume_runtime",
    "facial_animation",
    "editable_mesh",
    "datasmith_content",
    "geometry_cache",
    "geometry_cache_tracks",
    "apple_image_utils",
    "apple_vision",
    "gbx_blocking_volumes",
    "gbx_blueprint_function_libraries",
    "gbx_level_editor_preview",
    "gbx_perf_scope",
    "gbx_time_of_day",
    "media_assets",
    "img_media",
    "img_media_factory",
    "linear_timecode",
    "media_compositing",
    "wmf_media_factory",
    "tcp_messaging",
    "udp_messaging",
    "actor_sequence",
    "audio_capture",
    "audio_mixer_wwise",
    "cable_component",
    "custom_mesh_component",
    "phys_xvehicles",
    "procedural_mesh_component",
    "va_rest_plugin",
    "oak_game",
    "scaleform_ui",
    "gbx_ui",
    "gbx_inventory",
    "gbx_camera_modes",
    "gbx_dynamic_room",
    "gbx_weapon",
    "gbx_abilities",
    "gbx_mission",
    "gbx_travel_station",
    "replication_graph",
    "gbx_vehicle",
    "oak_cs",
    "input_core",
    "slate_core",
    "slate",
    "material_shader_quality_settings",
    "engine_settings",
    "head_mounted_display",
    "foliage",
    "landscape",
    "time_management",
    "anim_graph_runtime",
    "movie_scene_tracks",
    "movie_player",
    "cinematic_camera",
    "asset_registry",
    "gameplay_tags",
    "packet_handler",
    "mesh_description",
    "clothing_system_runtime_interface",
    "eye_tracker",
    "json_utilities",
    "movie_scene_capture",
    "mrmesh",
    "overlay",
    "clothing_system_runtime",
    "gbx_spark",
    "gbx_feedback",
    "gbx_perf_analytics",
    "gbx_probes_core",
    "gbx_anim_runtime",
    "live_link_interface",
    "gbx_destruction",
    "gbx_fluid_surface",
    "gbx_status_effects",
    "oak_destruction",
    "immediate_physics",
    "renderer",
    "animation_core",
    "property_path",
    "engine_messages",
    "audio_platform_configuration",
    "serialization",
    "session_messages",
    "gbx_anim_runtime_base",
    "gbx_streaming_interaction",
    "live_link_message_bus_framework",
    "bp",
    "vivox_core",
)

import mods_base
import unrealsdk
import typing

def get_pc() -> oak_game.OakPlayerController:
    return typing.cast(oak_game.OakPlayerController, mods_base.get_pc())

T = typing.TypeVar("T")

def ty_find_class(cls: type[T]) -> unrealsdk.unreal.UClass:
    return unrealsdk.find_class(cls.__qualname__.split(".")[0])

def ty_find_object(cls: type[T], name: str) -> T:
    return typing.cast(T, unrealsdk.find_object(cls.__qualname__.split(".")[0], name))

def ty_find_all(cls: type[T]) -> typing.Iterator[T]:
    return typing.cast(typing.Iterator[T], unrealsdk.find_all(cls.__qualname__.split(".")[0]))

mods_base.build_mod(
    mod_type=mods_base.ModType.Library,
    cls=mods_base.Library,
    auto_enable=True,
)