numbers = [1, 4, 3, 5, 3]


def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]


# print(get_median_font_size(numbers))
