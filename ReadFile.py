def readFile(directory):
    with open(directory, "r") as file:
        Title = file.readline()
        HeightWidth = file.readline().split(' ')
        Height = file.readline()
        matrix = [[element for element in s.split(' ') if element.isdigit()] for s in file.read().split(" \n", maxsplit=511)]
    return matrix