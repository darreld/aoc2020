def initDict():
	tmpDict = {}
	for x in range(97, 123):
		letter = chr(x)
		tmpDict[letter] = 0

	return tmpDict

def mysum(myDict):
   sum_ = 0
   for i in myDict:
      sum_ = sum_ + myDict[i]
   return sum_

def sumGrps(myGroups):
	gsum = 0
	for x in range(len(myGroups)):
		gsum = gsum + myGroups[x]
	return gsum

groups = []
answersDict = initDict()

with open('adventd6p1data.txt') as input:
	for line in input:
		tmpWork = []
		#read lines until empty line
		if line[0] != '\n':
			tmpWork = list(line)
			print(tmpWork)
			if tmpWork[len(tmpWork)-1] == '\n':
				tmpWork.pop()
			for s in range(len(tmpWork)):
				print(f"char {s} = {tmpWork[s]}")
				answersDict[tmpWork[s]] = 1
		else:
			print(answersDict)
			groups.append(mysum(answersDict))
			answersDict = initDict()
			continue
	else:
		print(answersDict)
		groups.append(mysum(answersDict))
		answersDict = initDict()

print(groups)
g = sumGrps(groups)
print (g)






