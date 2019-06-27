#readfile=open("Sacramentorealestatetransactions.csv","r")

rcount = 0
ncount = 0

with open("C:/Users/vb1017665/PycharmProjects/learning/python_training_day-2/Sacramentorealestatetransactions.csv","r") as readfile:
    for line in readfile:
        line=line.strip()
        datalist=line.split(",")
        if datalist[7] == "Residential":
            rcount=rcount+1
        else:
            ncount=ncount+1

print("Residential   :", rcount)
print("NonResidential:", ncount)