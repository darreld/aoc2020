with open('adventd1p1data.txt') as input:
	lines = input.read().split('\n')

del lines[-1]

print(f"Number of inputs: {len(lines)}")

for myx in range(len(lines)):
	val1 = int(lines[myx])
	for myy in range(len(lines)):
		val2 = int(lines[myy])
		for myz in range(len(lines)):
			val3 = int(lines[myz])
			tmpVal = val1 + val2  + val3
			#print(f"Left: {lines[myx]} -> right {lines[myy]}")
			if (tmpVal == 2020):
				print(f"val1 = {val1}, val2 = {val2}, val3 = {val3}")
				print(f"Total = {val1 * val2 * val3}")


print ("Done!")