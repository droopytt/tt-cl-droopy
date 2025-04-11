import random

def progress_value_cashbot_static(boss_damage, max_damage=500, from_value=0.5, to_value=1.5):
    damage_ratio = float(boss_damage) / float(max_damage)
    progress_value = from_value + (to_value - from_value) * min(damage_ratio, 1)
    return progress_value

def progress_random_value(boss_damage, from_value, to_value, radius=0.2):
    t = progress_value_cashbot_static(boss_damage, from_value=0, to_value=1)
    radius = radius * (1.0 - abs(t - 0.5) * 2.0)
    t += radius * random.uniform(-1, 1)
    t = max(min(t, 1.0), 0.0)
    return from_value + (to_value - from_value) * t


MAX_GOON_RANGE = 466
MIN_GOON_RANGE = 452
STUN_GOON_SCALE = 0.60
ITERATIONS = 2_000_000

def probability_of_stun_with_hp(hp_remaining):
    values = list()
    max = 0
    min = 20
    for i in range(ITERATIONS):
        damage = 500 - hp_remaining
        goon_scale = progress_random_value(damage, 0.5, 1.5)
        if goon_scale > max:
            max = goon_scale
        if goon_scale < min:
            min = goon_scale
        if goon_scale >= STUN_GOON_SCALE:
            values.append(goon_scale)
    probability = "{:.2f}".format((len(values) / ITERATIONS) * 100)
    print(f"Probability of stun goon as 5th goon given {hp_remaining} after first 4 goons health is ~{probability}% (min,max with this HP left is {min},{max})")

for health in range (MIN_GOON_RANGE, MAX_GOON_RANGE+1):
    probability_of_stun_with_hp(health)
