def swapfileData():
    filename1 = input("Enter file1 name: ")
    filename2 = input("Enter file2 name: ")
    file1 = open(filename1,'r')
    dataA = file1.read()
    file2 = open(filename2,'r')
    dataB = file2.read()
    file1 = open(filename1,'w')
    file1.write(dataB)
    file2 = open(filename2,'w')
    file2.write(dataA)
    print("Data Swapped")

swapfileData()
