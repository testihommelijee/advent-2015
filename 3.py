directions = open("inputs/input3", "r").read()

x = 0
y = 0
coordinates = [str(x)+':'+str(y)]

for direction in directions:
	if direction == "<":
		x -= 1
	elif direction == ">":
		x += 1
	elif direction == "v":
		y += 1
	else:
		y -= 1
	coordinates.append(str(x)+':'+str(y))

print len(set(coordinates))