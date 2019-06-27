readfile=open("realestate.csv","r")
rcount = 0
ncount = 0
for line in readfile:

    line=line.strip()

    datalist=line.split(",")

    if datalist[7] == "Residential":

        rcount=rcount+1

    else:

        ncount=ncount+1

print("Residential:", rcount)

print("NonResidential:", ncount) 

