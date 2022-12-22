#from config import *


#inputs_file = (base_path+'"../day06.txt')

with open('inputs\day06.txt', 'r') as inputs:
    full_input = inputs.read().splitlines()


# Part 1

# Turn on lights in set of coordinates
def turn_on(light_matrix, coordinates_from, coordinates_to):
    for x in range (coordinates_from[0], coordinates_to[0]+1):
        for y in range (coordinates_from[1], coordinates_to[1]+1):
            #print(x, y)
            if (x, y) not in light_matrix:
                light_matrix.add((x, y))
    return light_matrix


# Turn off lights in set of coordinates
def turn_off(light_matrix, coordinates_from, coordinates_to):
    for x in range(coordinates_from[0], coordinates_to[0] + 1):
        for y in range(coordinates_from[1], coordinates_to[1] + 1):
            # print(x, y)
            if (x, y) in light_matrix:
                light_matrix.remove((x, y))
    return light_matrix


# Toggle lights in set of coordinates
def toggle(light_matrix, coordinates_from, coordinates_to):
    for x in range(coordinates_from[0], coordinates_to[0] + 1):
        for y in range(coordinates_from[1], coordinates_to[1] + 1):
            # print(x, y)
            if (x, y) in light_matrix:
                light_matrix.remove((x, y))
            else:
                light_matrix.add((x, y))
    return light_matrix




# Part 2
# Increase by 1
def increase_lightness(light_matrix, coordinates_from, coordinates_to):
    for x in range (coordinates_from[0], coordinates_to[0]+1):
        for y in range (coordinates_from[1], coordinates_to[1]+1):
            if (x,y) in light_matrix.keys():
                light_matrix[(x,y)] = light_matrix[(x,y)] + 1
            else:
                light_matrix.update({(x, y): 1})
    return light_matrix

# Increase by two
def increase_lightness_by_two(light_matrix, coordinates_from, coordinates_to):
    for x in range (coordinates_from[0], coordinates_to[0]+1):
        for y in range (coordinates_from[1], coordinates_to[1]+1):
            if (x,y) in light_matrix.keys():
                light_matrix[(x,y)] = light_matrix[(x,y)] + 2
            else:
                light_matrix.update({(x, y): 2})
    return light_matrix


# Decrease lightness by 1
def decrease_lightness(light_matrix, coordinates_from, coordinates_to):
    for x in range(coordinates_from[0], coordinates_to[0] + 1):
        for y in range(coordinates_from[1], coordinates_to[1] + 1):
            if (x,y) in light_matrix.keys():
                if light_matrix[(x,y)] > 0:
                    light_matrix[(x,y)] = light_matrix[(x,y)] -1
    return light_matrix


light_matrix = set()
light_brightness = {}
for line in full_input:

    split_line = line.replace(',', ' ').replace('toggle', 'two toggle').split(' ')
    action = split_line[1]
    lights_from = (int(split_line[2]), int(split_line[3]))
    lights_to = (int(split_line[5]), int(split_line[6]))

    print(split_line)
    if action == 'on':
        light_matrix = turn_on(light_matrix, lights_from, lights_to)
        light_brightness = increase_lightness(light_brightness, lights_from, lights_to)
    if action == 'off':
        light_matrix = turn_off(light_matrix, lights_from, lights_to)
        light_brightness = decrease_lightness(light_brightness, lights_from, lights_to)
    if action == 'toggle':
        light_matrix = toggle(light_matrix, lights_from, lights_to)
        light_brightness = increase_lightness_by_two(light_brightness, lights_from, lights_to)


print(f' Total ammount of turned on lights: {len(light_matrix)}')
print(f' Total ammount of brightness: {sum(light_brightness.values())}')
