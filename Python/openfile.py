filename = raw_input("File: ")

myfile = open(filename)

string = myfile.read()

print string

#In short: print open(raw_input("File: ")).read()
