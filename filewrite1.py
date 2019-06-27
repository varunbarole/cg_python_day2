

fobj = open("customers.txt","a")


for val in range(1,100):
    fobj.write(str(val) + "\n")

fobj.close()


filename ="info.csv"

fobj = open(filename,"w")

name = input("Enter any string :")
fobj.write(name + "\n")

fobj.close()
