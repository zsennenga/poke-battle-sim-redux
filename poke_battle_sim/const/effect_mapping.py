from poke_battle_sim.const.move_effects import MoveEffect
# Import all effect functions
from poke_battle_sim.util.move_logic._effect_no_effect import _effect_no_effect
from poke_battle_sim.util.move_logic._effect_no_secondary_effect import _effect_no_secondary_effect
from poke_battle_sim.util.move_logic._effect_attacker_stat_stage_change_chance import _effect_attacker_stat_stage_change_chance
from poke_battle_sim.util.move_logic._effect_defender_stat_stage_change_chance import _effect_defender_stat_stage_change_chance
from poke_battle_sim.util.move_logic._effect_attacker_non_volatile_status_chance import _effect_attacker_non_volatile_status_chance
from poke_battle_sim.util.move_logic._effect_defender_non_volatile_status_chance import _effect_defender_non_volatile_status_chance
from poke_battle_sim.util.move_logic._effect_defender_confuse_chance import _effect_defender_confuse_chance
from poke_battle_sim.util.move_logic._effect_defender_flinch_chance import _effect_defender_flinch_chance
from poke_battle_sim.util.move_logic._effect_high_crit_rate import _effect_high_crit_rate
from poke_battle_sim.util.move_logic._effect_guaranteed_flinch import _effect_guaranteed_flinch
from poke_battle_sim.util.move_logic._effect_multi_hit_2_5 import _effect_multi_hit_2_5
from poke_battle_sim.util.move_logic._effect_multi_hit_2 import _effect_multi_hit_2
from poke_battle_sim.util.move_logic._effect_defender_non_volatile_status import _effect_defender_non_volatile_status
from poke_battle_sim.util.move_logic._effect_defender_confuse import _effect_defender_confuse
from poke_battle_sim.util.move_logic._effect_attacker_stat_stage_change import _effect_attacker_stat_stage_change
from poke_battle_sim.util.move_logic._effect_defender_stat_stage_change import _effect_defender_stat_stage_change
from poke_battle_sim.util.move_logic._effect_surf import _effect_surf
from poke_battle_sim.util.move_logic._effect_stomp import _effect_stomp
from poke_battle_sim.util.move_logic._effect_ohko import _effect_ohko
from poke_battle_sim.util.move_logic._effect_razor_wind import _effect_razor_wind
from poke_battle_sim.util.move_logic._effect_gust import _effect_gust
from poke_battle_sim.util.move_logic._effect_fly import _effect_fly
from poke_battle_sim.util.move_logic._effect_bind import _effect_bind
from poke_battle_sim.util.move_logic._effect_jump_kick import _effect_jump_kick
from poke_battle_sim.util.move_logic._effect_earthquake import _effect_earthquake
from poke_battle_sim.util.move_logic._effect_take_down import _effect_take_down
from poke_battle_sim.util.move_logic._effect_thrash import _effect_thrash
from poke_battle_sim.util.move_logic._effect_double_edge import _effect_double_edge
from poke_battle_sim.util.move_logic._effect_twineedle import _effect_twineedle
from poke_battle_sim.util.move_logic._effect_sonic_boom import _effect_sonic_boom
from poke_battle_sim.util.move_logic._effect_disable import _effect_disable
from poke_battle_sim.util.move_logic._effect_mist import _effect_mist
from poke_battle_sim.util.move_logic._effect_hyper_beam import _effect_hyper_beam
from poke_battle_sim.util.move_logic._effect_low_kick import _effect_low_kick
from poke_battle_sim.util.move_logic._effect_counter import _effect_counter
from poke_battle_sim.util.move_logic._effect_seismic_toss import _effect_seismic_toss
from poke_battle_sim.util.move_logic._effect_absorb import _effect_absorb
from poke_battle_sim.util.move_logic._effect_leech_seed import _effect_leech_seed
from poke_battle_sim.util.move_logic._effect_solar_beam import _effect_solar_beam
from poke_battle_sim.util.move_logic._effect_thunder import _effect_thunder
from poke_battle_sim.util.move_logic._effect_rage import _effect_rage
from poke_battle_sim.util.move_logic._effect_mimic import _effect_mimic
from poke_battle_sim.util.move_logic._effect_recover import _effect_recover
from poke_battle_sim.util.move_logic._effect_minimize import _effect_minimize
from poke_battle_sim.util.move_logic._effect_defense_curl import _effect_defense_curl
from poke_battle_sim.util.move_logic._effect_light_screen import _effect_light_screen
from poke_battle_sim.util.move_logic._effect_haze import _effect_haze
from poke_battle_sim.util.move_logic._effect_focus_energy import _effect_focus_energy
from poke_battle_sim.util.move_logic._effect_bide import _effect_bide
from poke_battle_sim.util.move_logic._effect_metronome import _effect_metronome
from poke_battle_sim.util.move_logic._effect_mirror_move import _effect_mirror_move
from poke_battle_sim.util.move_logic._effect_self_destruct import _effect_self_destruct
from poke_battle_sim.util.move_logic._effect_skull_bash import _effect_skull_bash
from poke_battle_sim.util.move_logic._effect_dream_eater import _effect_dream_eater
from poke_battle_sim.util.move_logic._effect_sky_attack import _effect_sky_attack
from poke_battle_sim.util.move_logic._effect_transform import _effect_transform
from poke_battle_sim.util.move_logic._effect_psywave import _effect_psywave
from poke_battle_sim.util.move_logic._effect_splash import _effect_splash
from poke_battle_sim.util.move_logic._effect_explosion import _effect_explosion
from poke_battle_sim.util.move_logic._effect_rest import _effect_rest
from poke_battle_sim.util.move_logic._effect_conversion import _effect_conversion
from poke_battle_sim.util.move_logic._effect_tri_attack import _effect_tri_attack
from poke_battle_sim.util.move_logic._effect_super_fang import _effect_super_fang
from poke_battle_sim.util.move_logic._effect_substitute import _effect_substitute
from poke_battle_sim.util.move_logic._effect_struggle import _effect_struggle
from poke_battle_sim.util.move_logic._effect_sketch import _effect_sketch
from poke_battle_sim.util.move_logic._effect_triple_kick import _effect_triple_kick
from poke_battle_sim.util.move_logic._effect_thief import _effect_thief
from poke_battle_sim.util.move_logic._effect_spider_web import _effect_spider_web
from poke_battle_sim.util.move_logic._effect_mind_reader import _effect_mind_reader
from poke_battle_sim.util.move_logic._effect_nightmare import _effect_nightmare
from poke_battle_sim.util.move_logic._effect_flame_wheel import _effect_flame_wheel
from poke_battle_sim.util.move_logic._effect_snore import _effect_snore
from poke_battle_sim.util.move_logic._effect_curse import _effect_curse
from poke_battle_sim.util.move_logic._effect_flail import _effect_flail
from poke_battle_sim.util.move_logic._effect_conversion_2 import _effect_conversion_2
from poke_battle_sim.util.move_logic._effect_spite import _effect_spite
from poke_battle_sim.util.move_logic._effect_protect import _effect_protect
from poke_battle_sim.util.move_logic._effect_belly_drum import _effect_belly_drum
from poke_battle_sim.util.move_logic._effect_spikes import _effect_spikes
from poke_battle_sim.util.move_logic._effect_foresight import _effect_foresight
from poke_battle_sim.util.move_logic._effect_destiny_bond import _effect_destiny_bond
from poke_battle_sim.util.move_logic._effect_perish_song import _effect_perish_song
from poke_battle_sim.util.move_logic._effect_sandstorm import _effect_sandstorm
from poke_battle_sim.util.move_logic._effect_endure import _effect_endure
from poke_battle_sim.util.move_logic._effect_rollout import _effect_rollout
from poke_battle_sim.util.move_logic._effect_false_swipe import _effect_false_swipe
from poke_battle_sim.util.move_logic._effect_swagger import _effect_swagger
from poke_battle_sim.util.move_logic._effect_fury_cutter import _effect_fury_cutter
from poke_battle_sim.util.move_logic._effect_attract import _effect_attract
from poke_battle_sim.util.move_logic._effect_sleep_talk import _effect_sleep_talk
from poke_battle_sim.util.move_logic._effect_heal_bell import _effect_heal_bell
from poke_battle_sim.util.move_logic._effect_return import _effect_return
from poke_battle_sim.util.move_logic._effect_present import _effect_present
from poke_battle_sim.util.move_logic._effect_frustration import _effect_frustration
from poke_battle_sim.util.move_logic._effect_safeguard import _effect_safeguard
from poke_battle_sim.util.move_logic._effect_pain_split import _effect_pain_split
from poke_battle_sim.util.move_logic._effect_magnitude import _effect_magnitude
from poke_battle_sim.util.move_logic._effect_baton_pass import _effect_baton_pass
from poke_battle_sim.util.move_logic._effect_encore import _effect_encore
from poke_battle_sim.util.move_logic._effect_rapid_spin import _effect_rapid_spin
from poke_battle_sim.util.move_logic._effect_morning_sun import _effect_morning_sun
from poke_battle_sim.util.move_logic._effect_hidden_power import _effect_hidden_power
from poke_battle_sim.util.move_logic._effect_twister import _effect_twister
from poke_battle_sim.util.move_logic._effect_rain_dance import _effect_rain_dance
from poke_battle_sim.util.move_logic._effect_sunny_day import _effect_sunny_day
from poke_battle_sim.util.move_logic._effect_mirror_coat import _effect_mirror_coat
from poke_battle_sim.util.move_logic._effect_psych_up import _effect_psych_up
from poke_battle_sim.util.move_logic._effect_ancient_power import _effect_ancient_power
from poke_battle_sim.util.move_logic._effect_future_sight import _effect_future_sight
from poke_battle_sim.util.move_logic._effect_beat_up import _effect_beat_up
from poke_battle_sim.util.move_logic._effect_uproar import _effect_uproar
from poke_battle_sim.util.move_logic._effect_stockpile import _effect_stockpile
from poke_battle_sim.util.move_logic._effect_spit_up import _effect_spit_up
from poke_battle_sim.util.move_logic._effect_swallow import _effect_swallow
from poke_battle_sim.util.move_logic._effect_hail import _effect_hail
from poke_battle_sim.util.move_logic._effect_torment import _effect_torment
from poke_battle_sim.util.move_logic._effect_flatter import _effect_flatter
from poke_battle_sim.util.move_logic._effect_memento import _effect_memento
from poke_battle_sim.util.move_logic._effect_facade import _effect_facade
from poke_battle_sim.util.move_logic._effect_focus_punch import _effect_focus_punch
from poke_battle_sim.util.move_logic._effect_smelling_salts import _effect_smelling_salts
from poke_battle_sim.util.move_logic._effect_nature_power import _effect_nature_power
from poke_battle_sim.util.move_logic._effect_charge import _effect_charge
from poke_battle_sim.util.move_logic._effect_taunt import _effect_taunt
from poke_battle_sim.util.move_logic._effect_helping_hand import _effect_helping_hand
from poke_battle_sim.util.move_logic._effect_trick import _effect_trick
from poke_battle_sim.util.move_logic._effect_role_play import _effect_role_play
from poke_battle_sim.util.move_logic._effect_wish import _effect_wish
from poke_battle_sim.util.move_logic._effect_assist import _effect_assist
from poke_battle_sim.util.move_logic._effect_ingrain import _effect_ingrain
from poke_battle_sim.util.move_logic._effect_superpower import _effect_superpower
from poke_battle_sim.util.move_logic._effect_magic_coat import _effect_magic_coat
from poke_battle_sim.util.move_logic._effect_recycle import _effect_recycle
from poke_battle_sim.util.move_logic._effect_revenge import _effect_revenge
from poke_battle_sim.util.move_logic._effect_brick_break import _effect_brick_break
from poke_battle_sim.util.move_logic._effect_yawn import _effect_yawn
from poke_battle_sim.util.move_logic._effect_knock_off import _effect_knock_off
from poke_battle_sim.util.move_logic._effect_endeavor import _effect_endeavor
from poke_battle_sim.util.move_logic._effect_eruption import _effect_eruption
from poke_battle_sim.util.move_logic._effect_skill_swap import _effect_skill_swap
from poke_battle_sim.util.move_logic._effect_imprison import _effect_imprison
from poke_battle_sim.util.move_logic._effect_refresh import _effect_refresh
from poke_battle_sim.util.move_logic._effect_grudge import _effect_grudge
from poke_battle_sim.util.move_logic._effect_snatch import _effect_snatch
from poke_battle_sim.util.move_logic._effect_secret_power import _effect_secret_power
from poke_battle_sim.util.move_logic._effect_dive import _effect_dive
from poke_battle_sim.util.move_logic._effect_camouflage import _effect_camouflage
from poke_battle_sim.util.move_logic._effect_blaze_kick import _effect_blaze_kick
from poke_battle_sim.util.move_logic._effect_mud_sport import _effect_mud_sport
from poke_battle_sim.util.move_logic._effect_weather_ball import _effect_weather_ball
from poke_battle_sim.util.move_logic._effect_grass_whistle import _effect_grass_whistle
from poke_battle_sim.util.move_logic._effect_tickle import _effect_tickle
from poke_battle_sim.util.move_logic._effect_cosmic_power import _effect_cosmic_power
from poke_battle_sim.util.move_logic._effect_sky_uppercut import _effect_sky_uppercut
from poke_battle_sim.util.move_logic._effect_bulk_up import _effect_bulk_up
from poke_battle_sim.util.move_logic._effect_bounce import _effect_bounce
from poke_battle_sim.util.move_logic._effect_poison_tail import _effect_poison_tail
from poke_battle_sim.util.move_logic._effect_volt_tackle import _effect_volt_tackle
from poke_battle_sim.util.move_logic._effect_water_sport import _effect_water_sport
from poke_battle_sim.util.move_logic._effect_calm_mind import _effect_calm_mind
from poke_battle_sim.util.move_logic._effect_dragon_dance import _effect_dragon_dance
from poke_battle_sim.util.move_logic._effect_doom_desire import _effect_doom_desire
from poke_battle_sim.util.move_logic._effect_roost import _effect_roost
from poke_battle_sim.util.move_logic._effect_gravity import _effect_gravity
from poke_battle_sim.util.move_logic._effect_miracle_eye import _effect_miracle_eye
from poke_battle_sim.util.move_logic._effect_wake_up_slap import _effect_wake_up_slap
from poke_battle_sim.util.move_logic._effect_gyro_ball import _effect_gyro_ball
from poke_battle_sim.util.move_logic._effect_healing_wish import _effect_healing_wish
from poke_battle_sim.util.move_logic._effect_brine import _effect_brine
from poke_battle_sim.util.move_logic._effect_natural_gift import _effect_natural_gift
from poke_battle_sim.util.move_logic._effect_feint import _effect_feint
from poke_battle_sim.util.move_logic._effect_pluck import _effect_pluck
from poke_battle_sim.util.move_logic._effect_tailwind import _effect_tailwind
from poke_battle_sim.util.move_logic._effect_acupressure import _effect_acupressure
from poke_battle_sim.util.move_logic._effect_metal_burst import _effect_metal_burst
from poke_battle_sim.util.move_logic._effect_u_turn import _effect_u_turn
from poke_battle_sim.util.move_logic._effect_close_combat import _effect_close_combat
from poke_battle_sim.util.move_logic._effect_payback import _effect_payback
from poke_battle_sim.util.move_logic._effect_assurance import _effect_assurance
from poke_battle_sim.util.move_logic._effect_embargo import _effect_embargo
from poke_battle_sim.util.move_logic._effect_fling import _effect_fling
from poke_battle_sim.util.move_logic._effect_psycho_shift import _effect_psycho_shift
from poke_battle_sim.util.move_logic._effect_trump_card import _effect_trump_card
from poke_battle_sim.util.move_logic._effect_heal_block import _effect_heal_block
from poke_battle_sim.util.move_logic._effect_wring_out import _effect_wring_out
from poke_battle_sim.util.move_logic._effect_power_trick import _effect_power_trick
from poke_battle_sim.util.move_logic._effect_gastro_acid import _effect_gastro_acid
from poke_battle_sim.util.move_logic._effect_lucky_chant import _effect_lucky_chant
from poke_battle_sim.util.move_logic._effect_me_first import _effect_me_first
from poke_battle_sim.util.move_logic._effect_copycat import _effect_copycat
from poke_battle_sim.util.move_logic._effect_power_swap import _effect_power_swap
from poke_battle_sim.util.move_logic._effect_guard_swap import _effect_guard_swap
from poke_battle_sim.util.move_logic._effect_punishment import _effect_punishment
from poke_battle_sim.util.move_logic._effect_last_resort import _effect_last_resort
from poke_battle_sim.util.move_logic._effect_worry_seed import _effect_worry_seed
from poke_battle_sim.util.move_logic._effect_sucker_punch import _effect_sucker_punch
from poke_battle_sim.util.move_logic._effect_toxic_spikes import _effect_toxic_spikes
from poke_battle_sim.util.move_logic._effect_heart_swap import _effect_heart_swap
from poke_battle_sim.util.move_logic._effect_aqua_ring import _effect_aqua_ring
from poke_battle_sim.util.move_logic._effect_magnet_rise import _effect_magnet_rise
from poke_battle_sim.util.move_logic._effect_flare_blitz import _effect_flare_blitz
from poke_battle_sim.util.move_logic._effect_brave_bird import _effect_brave_bird
from poke_battle_sim.util.move_logic._effect_thunder_fang import _effect_thunder_fang
from poke_battle_sim.util.move_logic._effect_ice_fang import _effect_ice_fang
from poke_battle_sim.util.move_logic._effect_fire_fang import _effect_fire_fang
from poke_battle_sim.util.move_logic._effect_defog import _effect_defog
from poke_battle_sim.util.move_logic._effect_trick_room import _effect_trick_room
from poke_battle_sim.util.move_logic._effect_captivate import _effect_captivate
from poke_battle_sim.util.move_logic._effect_stealth_rock import _effect_stealth_rock
from poke_battle_sim.util.move_logic._effect_chatter import _effect_chatter
from poke_battle_sim.util.move_logic._effect_judgment import _effect_judgment
from poke_battle_sim.util.move_logic._effect_head_smash import _effect_head_smash
from poke_battle_sim.util.move_logic._effect_lunar_dance import _effect_lunar_dance
from poke_battle_sim.util.move_logic._effect_shadow_force import _effect_shadow_force

effect_mapping = {
    MoveEffect.NO_EFFECT: _effect_no_effect,
    MoveEffect.NO_SECONDARY_EFFECT: _effect_no_secondary_effect,
    MoveEffect.ATTACKER_STAT_STAGE_CHANGE_CHANCE: _effect_attacker_stat_stage_change_chance,
    MoveEffect.DEFENDER_STAT_STAGE_CHANGE_CHANCE: _effect_defender_stat_stage_change_chance,
    MoveEffect.ATTACKER_NON_VOLATILE_STATUS_CHANCE: _effect_attacker_non_volatile_status_chance,
    MoveEffect.DEFENDER_NON_VOLATILE_STATUS_CHANCE: _effect_defender_non_volatile_status_chance,
    MoveEffect.DEFENDER_CONFUSE_CHANCE: _effect_defender_confuse_chance,
    MoveEffect.DEFENDER_FLINCH_CHANCE: _effect_defender_flinch_chance,
    MoveEffect.HIGH_CRIT_RATE: _effect_high_crit_rate,
    MoveEffect.GUARANTEED_FLINCH: _effect_guaranteed_flinch,
    MoveEffect.MULTI_HIT_2_5: _effect_multi_hit_2_5,
    MoveEffect.MULTI_HIT_2: _effect_multi_hit_2,
    MoveEffect.DEFENDER_NON_VOLATILE_STATUS: _effect_defender_non_volatile_status,
    MoveEffect.DEFENDER_CONFUSE: _effect_defender_confuse,
    MoveEffect.ATTACKER_STAT_STAGE_CHANGE: _effect_attacker_stat_stage_change,
    MoveEffect.DEFENDER_STAT_STAGE_CHANGE: _effect_defender_stat_stage_change,
    MoveEffect.SURF: _effect_surf,
    MoveEffect.STOMP: _effect_stomp,
    MoveEffect.OHKO: _effect_ohko,
    MoveEffect.RAZOR_WIND: _effect_razor_wind,
    MoveEffect.GUST: _effect_gust,
    MoveEffect.FLY: _effect_fly,
    MoveEffect.BIND: _effect_bind,
    MoveEffect.JUMP_KICK: _effect_jump_kick,
    MoveEffect.EARTHQUAKE: _effect_earthquake,
    MoveEffect.TAKE_DOWN: _effect_take_down,
    MoveEffect.THRASH: _effect_thrash,
    MoveEffect.DOUBLE_EDGE: _effect_double_edge,
    MoveEffect.TWINEEDLE: _effect_twineedle,
    MoveEffect.SONIC_BOOM: _effect_sonic_boom,
    MoveEffect.DISABLE: _effect_disable,
    MoveEffect.MIST: _effect_mist,
    MoveEffect.HYPER_BEAM: _effect_hyper_beam,
    MoveEffect.LOW_KICK: _effect_low_kick,
    MoveEffect.COUNTER: _effect_counter,
    MoveEffect.SEISMIC_TOSS: _effect_seismic_toss,
    MoveEffect.ABSORB: _effect_absorb,
    MoveEffect.LEECH_SEED: _effect_leech_seed,
    MoveEffect.SOLAR_BEAM: _effect_solar_beam,
    MoveEffect.THUNDER: _effect_thunder,
    MoveEffect.RAGE: _effect_rage,
    MoveEffect.MIMIC: _effect_mimic,
    MoveEffect.RECOVER: _effect_recover,
    MoveEffect.MINIMIZE: _effect_minimize,
    MoveEffect.DEFENSE_CURL: _effect_defense_curl,
    MoveEffect.LIGHT_SCREEN: _effect_light_screen,
    MoveEffect.HAZE: _effect_haze,
    MoveEffect.FOCUS_ENERGY: _effect_focus_energy,
    MoveEffect.BIDE: _effect_bide,
    MoveEffect.METRONOME: _effect_metronome,
    MoveEffect.MIRROR_MOVE: _effect_mirror_move,
    MoveEffect.SELF_DESTRUCT: _effect_self_destruct,
    MoveEffect.SKULL_BASH: _effect_skull_bash,
    MoveEffect.DREAM_EATER: _effect_dream_eater,
    MoveEffect.SKY_ATTACK: _effect_sky_attack,
    MoveEffect.TRANSFORM: _effect_transform,
    MoveEffect.PSYWAVE: _effect_psywave,
    MoveEffect.SPLASH: _effect_splash,
    MoveEffect.EXPLOSION: _effect_explosion,
    MoveEffect.REST: _effect_rest,
    MoveEffect.CONVERSION: _effect_conversion,
    MoveEffect.TRI_ATTACK: _effect_tri_attack,
    MoveEffect.SUPER_FANG: _effect_super_fang,
    MoveEffect.SUBSTITUTE: _effect_substitute,
    MoveEffect.STRUGGLE: _effect_struggle,
    MoveEffect.SKETCH: _effect_sketch,
    MoveEffect.TRIPLE_KICK: _effect_triple_kick,
    MoveEffect.THIEF: _effect_thief,
    MoveEffect.SPIDER_WEB: _effect_spider_web,
    MoveEffect.MIND_READER: _effect_mind_reader,
    MoveEffect.NIGHTMARE: _effect_nightmare,
    MoveEffect.FLAME_WHEEL: _effect_flame_wheel,
    MoveEffect.SNORE: _effect_snore,
    MoveEffect.CURSE: _effect_curse,
    MoveEffect.FLAIL: _effect_flail,
    MoveEffect.CONVERSION_2: _effect_conversion_2,
    MoveEffect.SPITE: _effect_spite,
    MoveEffect.PROTECT: _effect_protect,
    MoveEffect.BELLY_DRUM: _effect_belly_drum,
    MoveEffect.SPIKES: _effect_spikes,
    MoveEffect.FORESIGHT: _effect_foresight,
    MoveEffect.DESTINY_BOND: _effect_destiny_bond,
    MoveEffect.PERISH_SONG: _effect_perish_song,
    MoveEffect.SANDSTORM: _effect_sandstorm,
    MoveEffect.ENDURE: _effect_endure,
    MoveEffect.ROLLOUT: _effect_rollout,
    MoveEffect.FALSE_SWIPE: _effect_false_swipe,
    MoveEffect.SWAGGER: _effect_swagger,
    MoveEffect.FURY_CUTTER: _effect_fury_cutter,
    MoveEffect.ATTRACT: _effect_attract,
    MoveEffect.SLEEP_TALK: _effect_sleep_talk,
    MoveEffect.HEAL_BELL: _effect_heal_bell,
    MoveEffect.RETURN: _effect_return,
    MoveEffect.PRESENT: _effect_present,
    MoveEffect.FRUSTRATION: _effect_frustration,
    MoveEffect.SAFEGUARD: _effect_safeguard,
    MoveEffect.PAIN_SPLIT: _effect_pain_split,
    MoveEffect.MAGNITUDE: _effect_magnitude,
    MoveEffect.BATON_PASS: _effect_baton_pass,
    MoveEffect.ENCORE: _effect_encore,
    MoveEffect.RAPID_SPIN: _effect_rapid_spin,
    MoveEffect.MORNING_SUN: _effect_morning_sun,
    MoveEffect.HIDDEN_POWER: _effect_hidden_power,
    MoveEffect.TWISTER: _effect_twister,
    MoveEffect.RAIN_DANCE: _effect_rain_dance,
    MoveEffect.SUNNY_DAY: _effect_sunny_day,
    MoveEffect.MIRROR_COAT: _effect_mirror_coat,
    MoveEffect.PSYCH_UP: _effect_psych_up,
    MoveEffect.ANCIENT_POWER: _effect_ancient_power,
    MoveEffect.FUTURE_SIGHT: _effect_future_sight,
    MoveEffect.BEAT_UP: _effect_beat_up,
    MoveEffect.UPROAR: _effect_uproar,
    MoveEffect.STOCKPILE: _effect_stockpile,
    MoveEffect.SPIT_UP: _effect_spit_up,
    MoveEffect.SWALLOW: _effect_swallow,
    MoveEffect.HAIL: _effect_hail,
    MoveEffect.TORMENT: _effect_torment,
    MoveEffect.FLATTER: _effect_flatter,
    MoveEffect.MEMENTO: _effect_memento,
    MoveEffect.FACADE: _effect_facade,
    MoveEffect.FOCUS_PUNCH: _effect_focus_punch,
    MoveEffect.SMELLING_SALTS: _effect_smelling_salts,
    MoveEffect.NATURE_POWER: _effect_nature_power,
    MoveEffect.CHARGE: _effect_charge,
    MoveEffect.TAUNT: _effect_taunt,
    MoveEffect.HELPING_HAND: _effect_helping_hand,
    MoveEffect.TRICK: _effect_trick,
    MoveEffect.ROLE_PLAY: _effect_role_play,
    MoveEffect.WISH: _effect_wish,
    MoveEffect.ASSIST: _effect_assist,
    MoveEffect.INGRAIN: _effect_ingrain,
    MoveEffect.SUPERPOWER: _effect_superpower,
    MoveEffect.MAGIC_COAT: _effect_magic_coat,
    MoveEffect.RECYCLE: _effect_recycle,
    MoveEffect.REVENGE: _effect_revenge,
    MoveEffect.BRICK_BREAK: _effect_brick_break,
    MoveEffect.YAWN: _effect_yawn,
    MoveEffect.KNOCK_OFF: _effect_knock_off,
    MoveEffect.ENDEAVOR: _effect_endeavor,
    MoveEffect.ERUPTION: _effect_eruption,
    MoveEffect.SKILL_SWAP: _effect_skill_swap,
    MoveEffect.IMPRISON: _effect_imprison,
    MoveEffect.REFRESH: _effect_refresh,
    MoveEffect.GRUDGE: _effect_grudge,
    MoveEffect.SNATCH: _effect_snatch,
    MoveEffect.SECRET_POWER: _effect_secret_power,
    MoveEffect.DIVE: _effect_dive,
    MoveEffect.CAMOUFLAGE: _effect_camouflage,
    MoveEffect.BLAZE_KICK: _effect_blaze_kick,
    MoveEffect.MUD_SPORT: _effect_mud_sport,
    MoveEffect.WEATHER_BALL: _effect_weather_ball,
    MoveEffect.GRASS_WHISTLE: _effect_grass_whistle,
    MoveEffect.TICKLE: _effect_tickle,
    MoveEffect.COSMIC_POWER: _effect_cosmic_power,
    MoveEffect.SKY_UPPERCUT: _effect_sky_uppercut,
    MoveEffect.BULK_UP: _effect_bulk_up,
    MoveEffect.BOUNCE: _effect_bounce,
    MoveEffect.POISON_TAIL: _effect_poison_tail,
    MoveEffect.VOLT_TACKLE: _effect_volt_tackle,
    MoveEffect.WATER_SPORT: _effect_water_sport,
    MoveEffect.CALM_MIND: _effect_calm_mind,
    MoveEffect.DRAGON_DANCE: _effect_dragon_dance,
    MoveEffect.DOOM_DESIRE: _effect_doom_desire,
    MoveEffect.ROOST: _effect_roost,
    MoveEffect.GRAVITY: _effect_gravity,
    MoveEffect.MIRACLE_EYE: _effect_miracle_eye,
    MoveEffect.WAKE_UP_SLAP: _effect_wake_up_slap,
    MoveEffect.GYRO_BALL: _effect_gyro_ball,
    MoveEffect.HEALING_WISH: _effect_healing_wish,
    MoveEffect.BRINE: _effect_brine,
    MoveEffect.NATURAL_GIFT: _effect_natural_gift,
    MoveEffect.FEINT: _effect_feint,
    MoveEffect.PLUCK: _effect_pluck,
    MoveEffect.TAILWIND: _effect_tailwind,
    MoveEffect.ACUPRESSURE: _effect_acupressure,
    MoveEffect.METAL_BURST: _effect_metal_burst,
    MoveEffect.U_TURN: _effect_u_turn,
    MoveEffect.CLOSE_COMBAT: _effect_close_combat,
    MoveEffect.PAYBACK: _effect_payback,
    MoveEffect.ASSURANCE: _effect_assurance,
    MoveEffect.EMBARGO: _effect_embargo,
    MoveEffect.FLING: _effect_fling,
    MoveEffect.PSYCHO_SHIFT: _effect_psycho_shift,
    MoveEffect.TRUMP_CARD: _effect_trump_card,
    MoveEffect.HEAL_BLOCK: _effect_heal_block,
    MoveEffect.WRING_OUT: _effect_wring_out,
    MoveEffect.POWER_TRICK: _effect_power_trick,
    MoveEffect.GASTRO_ACID: _effect_gastro_acid,
    MoveEffect.LUCKY_CHANT: _effect_lucky_chant,
    MoveEffect.ME_FIRST: _effect_me_first,
    MoveEffect.COPYCAT: _effect_copycat,
    MoveEffect.POWER_SWAP: _effect_power_swap,
    MoveEffect.GUARD_SWAP: _effect_guard_swap,
    MoveEffect.PUNISHMENT: _effect_punishment,
    MoveEffect.LAST_RESORT: _effect_last_resort,
    MoveEffect.WORRY_SEED: _effect_worry_seed,
    MoveEffect.SUCKER_PUNCH: _effect_sucker_punch,
    MoveEffect.TOXIC_SPIKES: _effect_toxic_spikes,
    MoveEffect.HEART_SWAP: _effect_heart_swap,
    MoveEffect.AQUA_RING: _effect_aqua_ring,
    MoveEffect.MAGNET_RISE: _effect_magnet_rise,
    MoveEffect.FLARE_BLITZ: _effect_flare_blitz,
    MoveEffect.BRAVE_BIRD: _effect_brave_bird,
    MoveEffect.THUNDER_FANG: _effect_thunder_fang,
    MoveEffect.ICE_FANG: _effect_ice_fang,
    MoveEffect.FIRE_FANG: _effect_fire_fang,
    MoveEffect.DEFOG: _effect_defog,
    MoveEffect.TRICK_ROOM: _effect_trick_room,
    MoveEffect.CAPTIVATE: _effect_captivate,
    MoveEffect.STEALTH_ROCK: _effect_stealth_rock,
    MoveEffect.CHATTER: _effect_chatter,
    MoveEffect.JUDGMENT: _effect_judgment,
    MoveEffect.HEAD_SMASH: _effect_head_smash,
    MoveEffect.LUNAR_DANCE: _effect_lunar_dance,
    MoveEffect.SHADOW_FORCE: _effect_shadow_force,
}
