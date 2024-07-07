
from mods_base import SliderOption, options, settings


minimum_damage = options.SliderOption(
    'ItemPool Samples',
    value=100,
    min_value=10,
    max_value=1000,
    description='The number of samples to take from the item pool.',
)