# fobj can be called as pointer or file variable or file reference
fobj = open("C:/Users/vb1017665/PycharmProjects/learning/languages.txt","r")
fobj = open("C:/Users/vb1017665/PycharmProjects/learning/languages.txt","r", buffering= 1000) ## here 1000 means bytes data will be displayed

for line in fobj:
    line = line.strip()
    line = line.strip()
    print(line)

fobj.close()


########################

# fobj can be called as pointer or file variable or file reference
with open("C:/Users/vb1017665/PycharmProjects/learning/languages.txt","r") as fobj:
    for line in fobj:
        line = line.strip()
        line = line.strip()
        print(line)

## fobj.close() -- no need to close the file as we are using context manager
## file will be close automatically once the operation is done