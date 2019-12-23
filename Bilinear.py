def Bilinear(matrix, width, height):
    newMatrix = []
    kWidth = 2
    kHeight = 2
    for i in range(510):
        bufferTop = []
        bufferDown = []
        bufferMiddle = []
        for j in range(len(matrix)-2):
            topNumber = int(int(matrix[i][j])+(int(matrix[i][j + kWidth]) - int(matrix[i][j]))/kWidth)
            downNumber = int(int(matrix[i + 1][j])+(int(matrix[i][j+1]) - int(matrix[i][j]))/kHeight)
            bufferTop.extend([matrix[i][j], str(topNumber), matrix[i][j+1]])
            bufferDown.extend([matrix[i+1][j], str(downNumber), matrix[i + 1][j + 1]])
        for l in range(len(bufferTop)):
            middleNumber = int(bufferTop[l]) + int(int(int(bufferDown[l]) - int(bufferTop[l]))/kWidth)
            bufferMiddle.append(str(middleNumber))
        newMatrix.extend([bufferTop, bufferMiddle, bufferDown])
    return newMatrix

