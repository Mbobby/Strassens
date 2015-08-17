#!/usr/bin/python
def baseMultiply(mat1, mat2):
	result = [[0,0],[0,0]]
	result[0][0] = (mat1[0][0] * mat2[0][0]) + (mat1[0][1] * mat2[1][0])
	result[0][1] = (mat1[0][0] * mat2[0][1]) + (mat1[0][1] * mat2[1][1])
	result[1][0] = (mat1[1][0] * mat2[0][0]) + (mat1[1][1] * mat2[1][0])
	result[1][1] = (mat1[1][0] * mat2[0][1]) + (mat1[1][1] * mat2[1][1])
	return result

def baseAdd(mat1, mat2):
	result = []
	for i in range(0, len(mat1)):
		l = []
		for j in range(0, len(mat1[0])):
			l.append((mat1[i][j] + mat2[i][j]))
		result.append(l)
	return result

def baseSubtract(mat1, mat2):
	result = []
	for i in range(0, len(mat1)):
		l = []
		for j in range(0, len(mat1[0])):
			l.append((mat1[i][j] - mat2[i][j]))
		result.append(l)
	return result


def check(mat):
	for i in range(1, 100):
		p = 2**i
		if(p == len(mat)):
			return True, 0
		elif(p > len(mat)):
			return False, p
	return False, -1


def pad(mat, num):
	newMatlen =  num
	newMat = []
	for i in range(0, num):
		newMat.append([0 for j in range(0, num)])

	for i in range(0, len(mat)):
		for j in range(0, len(mat[i])):
			newMat[i][j] = mat[i][j]
	return newMat


def divide(mat):
	x = len(mat)
	y = x/2
	a = []
	b = []
	c = []
	d = []

	for i in range(0, y):
		a.append(mat[i][0:y])
		b.append(mat[i][y:x])
	for i in range(y, x):
		c.append(mat[i][0:y])
		d.append(mat[i][y:x])
	return a, b, c, d

def join(a, b, c, d):
	result = []
	l = len(a) + len(c)
	k = 0
	for i in range(0, l/2):
		result.append(a[k] + b[k])
		k+= 1
	k = 0
	for i in range(l/2, l):
		result.append(c[k] + d[k])
		k+= 1
	return result

def multiply(mat1, mat2):
	if(len(mat1) == 2 and len(mat2) == 2):
		return baseMultiply(mat1, mat2)
	a11, a12, a21, a22 = divide(mat1)
	b11, b12, b21, b22 = divide(mat2)

	m1 = multiply(baseAdd(a11, a22), baseAdd(b11, b22))
	m2 = multiply(baseAdd(a21, a22), b11)
	m3 = multiply(a11, baseSubtract(b12, b22))
	m4 = multiply(a22, baseSubtract(b21, b11))
	m5 = multiply(baseAdd(a11, a12), b22)
	m6 = multiply(baseSubtract(a21, a11), baseAdd(b11, b12))
	m7 = multiply(baseSubtract(a12, a22), baseAdd(b21, b22))

	a = baseAdd(baseSubtract(baseAdd(m1, m4), m5), m7)
	b = baseAdd(m3, m5)
	c = baseAdd(m2, m4)
	d = baseAdd(baseSubtract(m1, m2), baseAdd(m3, m6))

	return join(a,b,c,d)


def strassens(mat1, mat2):
	fin = len(mat1)
	l1 = 0
	l2 = 0
	b, y = check(mat1)
	if(b == False and y != -1):
		mat1 = pad(mat1, y)
		l1 = len(mat1)
	elif(b == False and y == -1):
		print "The matrix you put in is too large:\nPlease try again with a smaller matrix"
		return

	b, y = check(mat2)
	if(b == False and y != -1):
		mat2 = pad(mat2, y)
		l2 = len(mat2)
	elif(b == False and y == -1):
		print "The matrix you put in is too large:\nPlease try again with a smaller matrix"
		return

	semi = multiply(mat1, mat2)

	final = []
	for i in range(0, fin):
		l = []
		for j in range(0, fin):
			l.append(semi[i][j])
		final.append(l)
	return final

def printMat(mat):
	for line in mat:
		print line

#Testing the program.
if __name__ == '__main__':
	print "####################################Test Cases#####################################"
	a = [[1,0,2], [4,1,1], [0,1,3]]
	b = [[0,1,0], [2,1,0], [2,0,1]]

	print "The Matrix for A: "
	printMat(a)
	print "The Matrix for B: "
	printMat(b)
	print "The multiplication of a and b: "
	y = strassens(a, b)
	printMat(y)

	a = [[1,0,2,1],[4,1,1,0],[0,1,3,0],[5,0,2,1]]
	b = [[0,1,0,1],[2,1,0,4],[2,0,1,1],[1,3,5,0]]

	print "The Matrix for A: "
	printMat(a)
	print "The Matrix for B: "
	printMat(b)
	print "The multiplication of a and b: "
	y = strassens(a, b)
	printMat(y)
