import random

def color_to_dict(color):
    """Convert a RGB hex color to an array in base 10"""

    return {
        "red": int(color[1:3], 16),
        "green": int(color[3:5], 16),
        "blue": int(color[5:7], 16)
    }

def random_color():
    """Return a random color in hex format"""

    return "#" + str(hex(random.randint(0, 16777215)))[2:]


def is_random(color, output="hex"):
    """Replace "random" by a random color.
    Else, return the initial parameter.
    Can output in both hex and decimal (default is hex)"""

    if color == "random":
        if output == "dec":
            return color_to_dict(random_color())
        else:
            return random_color()
    else:
        return color
