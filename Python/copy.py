inname = raw_input("Input:  ")
outname= raw_input("Output: ")

outwrite = open(outname, "w+")
outread = open(outname)
outwrite.write(open(inname).read())
outwrite.close() 
#Removing close() results in empty output. File not written until close()!
print outread.read()

