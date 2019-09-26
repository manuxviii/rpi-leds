def color_to_dict(color):
    """Convert a RGB hex color to an array in base 10"""

    ret = {
        "red": int(color[1:3], 16),
        "green": int(color[3:5], 16),
        "blue": int(color[5:7], 16)
    }

    return ret
