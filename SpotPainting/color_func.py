import colorgram


def color_extract(file_name, num_of_colors):
    colors = colorgram.extract(file_name, num_of_colors)
    l = list()
    for j in range(len(colors)):
        first_colour = colors[j].rgb
        l1 = list()
        for i in first_colour:
            l1.append(i)
        l.append(tuple(l1))
    return l

