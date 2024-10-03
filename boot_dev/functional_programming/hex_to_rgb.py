def hex_to_rgb(hex_color):
    return int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
    # from the start to position 2, from 2 to position 4 and from position 4 till
    # the end.


def is_hexadecimal(hex_string):
    try:
        int(hex_string)
        return True
    except Exception:
        return False


hex = "000000"
# This should return 0, 0, 0

print(len(hex))
print(hex_to_rgb(hex))
