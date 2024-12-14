def hex_to_rgb(hex_color):
    if is_hexadecimal(hex_color) and len(hex_color) == 6:
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)
        return r, g, b

    raise Exception("not a hex color string")


# Don't edit below this line


def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False


red_val, green_val, blue_val = hex_to_rgb("A020F0")
red_val, green_val, blue_val = hex_to_rgb("0")

print(f"red value: {red_val}")
print(f"green value: {green_val}")
print(f"blue value: {blue_val}")
