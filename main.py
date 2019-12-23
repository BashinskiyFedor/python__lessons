from Bilinear import Bilinear
from Neighbor import Neighbor
from ReadFile import readFile
from WriteFile import writeFile

image = readFile("Image\lena.pgm")
writeFile(image, "Image\original.pgm")
neigh = Neighbor(image, 1024, 1024)
biline = Bilinear(image, 1024, 1024)
writeFile(neigh, "Image\\neigh.pgm")
writeFile(biline, "Image\\biline.pgm")
print("Выполшненно")