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

def zeroDict(tdict):
	tmpDict = tdict
	for x in range(len(tdict)):
		tmpDict[x] = 0
	return tmpDict


def sumGrps(myGroups):
	gsum = 0
	for x in range(len(myGroups)):
		gsum = gsum + myGroups[x]
	return gsum

groups = []
groupCount = 0
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
				answersDict[tmpWork[s]] = answersDict[tmpWork[s]] + 1
				groupCount = groupCount + 1
		else:
			print(answersDict)
			groups.append(mysum(answersDict))
			answersDict = zeroDict(answersDict)
			groupCount = 0
			continue
	else:
		print(answersDict)
		groups.append(mysum(answersDict))
		answersDict = initDict()
		groupCount = 0

print(groups)
g = sumGrps(groups)
print (g)






