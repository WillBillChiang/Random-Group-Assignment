import random

# Accepts Input
print("Enter List of Names, Enter FINISH when finished")
names = []
inp = input()
while inp != "FINISH":
    # Formats Name Output
    inpF = inp.split(",")
    inpF2 = inpF[0] + " " + inpF[1]
    names.append(inpF2)
    inp = input()

print("Enter Group Size")
groupSize = int(input())

# Creates Output File
outputFile = open("out.txt", "w")

# Random Selection and Output
uneven = False
excessGroup = 0

groupNum = 1
while len(names) > 0:
    outputFile.write("----\n")
    outputFile.write("Group Number: " + str(groupNum) + "\n")
    randomGroup = []
    if len(names) < groupSize:
        uneven = True
        excessGroup = len(names)
        randomGroup = names
        names = []
    else:
        randomGroup = random.sample(names, groupSize)
        for name in randomGroup:
            names.remove(name)
    outputFile.write("\n")
    outputFile.write('\n'.join(randomGroup))
    outputFile.write("\n")
    outputFile.write("----\n\n")
    groupNum += 1

if uneven:
    outputFile.write("Cannot divide evenly, final group is size " + str(excessGroup))

outputFile.close()