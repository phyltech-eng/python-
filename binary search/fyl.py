#python has functions for creating ,reading ,updating,and deleting files
#opening a file
myfile = open("myfile.txt", "w")
#writing to a file
myfile.write("Hello, this is a test file.\n")

#reading a file
myfile = open("myfile.txt", "r")
#reading the contents of the file
contents = myfile.read()
#closing the file
myfile.close()
#appending to a file
