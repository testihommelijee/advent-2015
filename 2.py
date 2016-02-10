total = 0
for box in open("inputs/input2", "r").read().split("\n"):
	dimensions = sorted(map(int, box.split("x")))
	total += dimensions[0]*dimensions[1]*3+dimensions[1]*dimensions[2]*2+dimensions[0]*dimensions[2]*2
print total