# Gift Wrapping Convex Hull Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n log n)
# python convexHull.py "[1,1],[3,7],[9,9],[10,10],[0,0], [2, 2], [10,2], [-10, 1], [-5,6], [1,1]"

# imports
import copy
import math
import sys

# graham scan convex hull algorithm
def convexHull(points):
	points = removeDuplicatePoints(points)
	s = len(points)
	bottomPoint = 0
	for i in range(1, s):
		if (points[i][1] < points[bottomPoint][1]):
			bottomPoint = i
	pointsSorted = copy.deepcopy(points)
	del pointsSorted[bottomPoint]
	pointsSorted = sorted(pointsSorted, key = lambda x: radianAngle(points[bottomPoint], x))
	pointsSorted.insert(0, points[bottomPoint])
	hullPoints = [pointsSorted[0], pointsSorted[1], pointsSorted[2]]
	for i in range(3, s):
		while (isRightTurn(hullPoints[len(hullPoints) - 2], hullPoints[len(hullPoints) - 1], pointsSorted[i])):
			hullPoints.pop()
		hullPoints.append(pointsSorted[i])
	return [hullPoints, points[bottomPoint], pointsSorted]

# gives the angle of the point in radians
def radianAngle(basePoint, point):
	radians90 = math.radians(90)
	alteredPoint = copy.deepcopy(point)
	alteredPoint = [alteredPoint[0] + basePoint[0], alteredPoint[1] + basePoint[1]]
	if (alteredPoint[0] == 0):
		return radians90
	elif (alteredPoint[0] > 0):
		return math.atan(float(alteredPoint[1]) / float(alteredPoint[0]))
	else:
		return (radians90 - math.atan(float(alteredPoint[1]) / float(-1 * alteredPoint[0]))) + radians90

# does the new point cause a right turn?
def isRightTurn(pFrom, pTo, pNext):
	rightTurn = False
	vectorLast = [pTo[0] - pFrom[0], pTo[1] - pFrom[1]]
	vectorNext = [pNext[0] - pTo[0], pNext[1] - pTo[1]]
	if (vectorLast[0] <= 0):
		if (vectorNext[1] > 0):
			rightTurn = True
	else:
		if (vectorNext[1] < 0):
			rightTurn = True
	return rightTurn

# removes duplicate points
def removeDuplicatePoints(points):
	points.sort()
	s = len(points)
	last = points[s - 1]
	for i in xrange(s - 2, -1, -1):
		if ((last[0] == points[i][0]) and (last[1] == points[i][1])):
			del points[i]
		else:
			last = points[i]
	return points

# splits the string into integer points
def stringToPoints(strList):
	output = []
	strList = strList.replace(" ", "")
	splitString = strList.split("],[")
	for tuple in splitString:
		tuple = tuple.replace("[", "")
		tuple = tuple.replace("]", "")
		tupleList = tuple.split(",")
		tupleList[0] = int(tupleList[0])
		tupleList[1] = int(tupleList[1])
		output.append(tupleList)
	return output

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nGift Wrapping Convex Hull Algorithm by William M Mortl")
		print("Usage: python convexHull.py \"{[x coordinate, y coordinate], [x2, y2], ...}\"")
		print("Example: python convexHull.py \"[1,1],[3,7],[9,9],[10,10],[0,0],[2,2],[10,2]\"\r\n")
	else:
		hullPoints = stringToPoints(sys.argv[1])
		if (len(hullPoints) < 4):
			print("\r\nYou must enter at least 5 points!\r\n")
		else:
			print(("\r\nLooking for the convex hull of points:\r\n%s") % str(hullPoints))
			[hullPoints, bottomPoint, sortedPoints] = convexHull(hullPoints)
			print(("Bottom most point:\r\n%s") % str(bottomPoint))
			print(("Counterclockwise radially sorted points:\r\n%s") % str(sortedPoints))
			print(("Convex hull points:\r\n%s\r\n") % str(hullPoints))