from random import randint


def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r,g,b)
    return color

