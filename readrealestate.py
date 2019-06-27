
# C:\\Users\\data\\realestat.csv
# C:/Users/data/realestate.csv


# fobj can be called as pointer or file variable or file reference
rcount = 0
ncount = 0
with open("realestate.csv","r", buffering = 1000) as fobj:
    for line in fobj:
        line = line.strip()
        output = line.split(",")
    
        if output[7] == "Residential":
            rcount= rcount + 1
        else:
            ncount = ncount + 1

print("Residential flats     :",  rcount)
print("Non residential flats :",  ncount)
