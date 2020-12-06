with open('entries.txt') as input:
	lines = input.read().split('\n')

del lines[-1]

print(f"Number of inputs: {len(lines)}")

for myx in range(len(lines)):
	for myy in range(len(lines)):
		val1 = int(lines[myx])
		val2 = int(lines[myy])
		tmpVal = val1 + val2
		#print(f"Left: {lines[myx]} -> right {lines[myy]}")
		if (tmpVal == 2020):
			print(f"left = {val1}, right = {val2}")
			print(f"Total = {val1 * val2}")


print ("Done!")