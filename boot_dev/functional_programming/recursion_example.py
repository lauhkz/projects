test = {
    "melee_weapons": {
        "stabbies": {
            "spears": 4,
            "knives": 3,
        },
        "bows": 6,
    }
}


def layers_counter(d, deep_so_far):
    current_max = deep_so_far
    if not isinstance(d, dict) or not d:
        return deep_so_far
    for v in d.values():
        depth_of_subdict = layers_counter(v, deep_so_far + 1)
        if depth_of_subdict > current_max:
            current_max = depth_of_subdict

    return current_max


print(layers_counter(test, 1))
