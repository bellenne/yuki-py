from math import floor
import numpy as np 
import time
def goRight(row, columnStart, columnEnd):
    global resultArr
    global currentElem

    lastI = 0
    for i in range(columnStart,columnEnd):
        resultArr.append(matrix[row][i])
        currentElem = matrix[row][i]
        lastI = i
    return {"row":row+1, "column":lastI, "sliced":row}

def goDown(column, rowStart, rowEnd):
    global resultArr
    global currentElem
    global columnAdd

    lastI = 0    
    for i in range(rowStart, rowEnd+1):
        resultArr.append(matrix[i][column])
        currentElem = matrix[i][column]
        lastI = i

    return {"row":lastI, "column":column-1, "sliced":column}

def goUp(column, rowStart, rowEnd):
    global resultArr
    global currentElem

    lastI = 0
    for i in range(rowStart, rowEnd, -1):
        resultArr.append(matrix[i][column])
        currentElem = matrix[i][column]
        lastI = i
    return {"row":lastI, "column":column+1, "sliced": column}

def goLeft(row, columnStart, columnEnd):
    global resultArr
    global currentElem

    lastI = 0
    for i in range(columnStart,columnEnd,-1):
        resultArr.append(matrix[row][i])
        currentElem = matrix[row][i]
        lastI = i

    return {"row":row-1, "column":lastI, "sliced":row}

matrixLen = int(input("Matrix length: "))
matrix = np.random.randint(10, size=(matrixLen, matrixLen))
print(matrix)

global resultArr
resultArr = []

elemCount = matrixLen*matrixLen

global currentElem
currentElem= None

dataU = {"row":0, "column":0, "sliced":matrixLen}
dataD={"sliced":matrixLen}

while len(resultArr) < elemCount:
        dataR = goRight(dataU["row"], dataU["column"], dataD["sliced"])
        dataD = goDown(dataR["column"], dataR["row"], dataR["column"])
        dataL = goLeft(dataD["row"], dataD["column"], dataU["column"]-1)
        dataU = goUp(dataL["column"], dataL["row"], dataR["sliced"])

for i in range(0, len(resultArr)):
    resultArr[i] = int(resultArr[i])
    
print(resultArr) 