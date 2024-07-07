
from mods_base import SliderOption, options, settings

only_crits = options.BoolOption(
    'Only Crits',
    False,
    true_text='Only log crits',
    false_text='Log all damage'
)

allow_self_damage = options.BoolOption(
    'Allow Self Damage',
    False,
    true_text='Log self damage',
    false_text='Ignore self damage'
)

minimum_damage = options.SliderOption(
    'Minimum Damage',
    value=27,
    min_value=1,
    max_value=128,
    description='Minimum damage to log, in units of 2 raised to the power of the value',
)