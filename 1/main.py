import numpy
import scipy.misc
import scipy.integrate

#1
def splitInterval(start, end, n):
    return numpy.arange(start, end, (end - start) / n)

#2
def generate123Array(n):
    array = numpy.empty(3 * n)
    for i in range(len(array)):
        array[i] = i % 3 + 1
    return array

#3
def generateArrayOfOddNumbers(n):
    array = numpy.empty(n)
    for i in range(len(array)):
        array[i] = i * 2 + 1
    return array

#4
def generateFrammedArray(n):
    array = numpy.empty([n, n])
    rows = len(array)
    cols = len(array[0])
    for i in range(rows):
        for j in range(cols):
            if (i == 0) or (i == rows - 1) or (j == 0) or (j == cols - 1):
                array[i][j] = 1
            else:
                array[i][j] = 0
    return array

#5
def generateChessBoard(n):
    array = numpy.empty([n, n])
    for i in range(n):
        for j in range(n):
            array[i][j] = (i + j) % 2
    return array

#6
def generateIPlusJArray(n):
    array = numpy.empty([n, n])
    for i in range(n):
        for j in range(n):
            array[i][j] = i + j
    return array

#7
def getArraySums(array):
    dictOfSums = dict()
    dictOfSums["array"] = array
    dictOfSums["sumAll"] = numpy.sum(array)
    dictOfSums["sumRows"] = numpy.sum(array, axis=1)
    dictOfSums["sumCols"] = numpy.sum(array, axis=0)
    return dictOfSums

#8
def sortByCol(array, n):
    return array[numpy.argsort(array[:, n])]

#9
def inverseMatrix(matrix):
    return numpy.linalg.inv(matrix)

#10
def getEigenValuesAndVector(matrix):
    return numpy.linalg.eig(matrix)

#11
def calculateDerivative(f, x0, dx):
    return scipy.misc.derivative(f, x0, dx)

#12
def calculateDefinitiveIntegral(f, x0, x1):
    return scipy.integrate.quad(f, x0, x1)

#12*
def calculateIndefinitiveIntegral(polynomial):
    return numpy.polyint(polynomial)


def f(x):
    return x**2 + 1

def main():
    print("1: ")
    print(numpy.arange(start=-1.3, stop=2.5, step=((2.5 - (-1.3)) / 64)))

    print("2: ")
    print(generate123Array(3))

    print("3: ")
    print(generateArrayOfOddNumbers(10))

    print("4: ")
    print(generateFrammedArray(10))

    print("5: ")
    print(generateChessBoard(8))

    print("6: ")
    print(generateIPlusJArray(10))

    print("7: ")
    print(getArraySums(numpy.random.rand(3, 5)))

    print("8: ")
    print(sortByCol(numpy.random.rand(5, 5), 1))

    print("9: ")
    print(inverseMatrix(numpy.random.rand(5, 5)))

    print("10: ")
    print(getEigenValuesAndVector(numpy.random.rand(5, 5)))

    print("11: ")
    print(calculateDerivative(f, 1, 1e-6))

    print("12: ")
    print(calculateDefinitiveIntegral(f, 0, 1))

    print("12*: ")
    print(calculateIndefinitiveIntegral([1, 1]))

main()
