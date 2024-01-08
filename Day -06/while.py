x = 6
while x < 15:
	print(x)
	x += 1
while x >= 1:
	print("*" * x)
	x -= 2
while x < 15:
	if x % 2 == 0:
		print("Even:", x)
		break
	print(x)
	x += 1