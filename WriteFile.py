def writeFile(matrix, directory):
   with open(directory, "w") as file:
       file.writelines("P2\n")
       file.writelines(str(len(matrix[1])) + " " + str(len(matrix)) + "\n")
       file.writelines("245\n")
       print(len(matrix))
       for i in range(len(matrix)):
           print("i = " + str(i))
           file.write('\t'.join(matrix[i]))
           file.write("\t")