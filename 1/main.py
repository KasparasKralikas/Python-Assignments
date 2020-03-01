import numpy

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

def main():
    print(numpy.arange(start=-1.3, stop=2.5, step=((2.5 - (-1.3)) / 64)))
    print(generate123Array(3))
    print(generateArrayOfOddNumbers(10))
    print(generateFrammedArray(10))
    print(generateChessBoard(8))
    print(generateIPlusJArray(10))
main()
