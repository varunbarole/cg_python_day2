

# fobj can be called as pointer or file variable or file reference
fobj = open("languages.txt","r", buffering = 1000)

for line in fobj:
    line = line.strip()
    print(line)

fobj.close()


## context manager
# fobj can be called as pointer or file variable or file reference
with open("languages.txt","r") as fobj:
    for line in fobj:
        line = line.strip()
        print(line)

