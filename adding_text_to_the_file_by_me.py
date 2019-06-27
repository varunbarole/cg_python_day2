fobj = open("C:/Users/vb1017665/Desktop/customers.txt", "w")
#fobj.write("\nPython / INDIA\n")
fobj.write("Python / INDIA\n")

for val in range(1, 101):
#    print(val)
    fobj.write(str(val) + "\n")

fobj.close()