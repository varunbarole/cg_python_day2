# using dictionary
citydict = dict()
with open("realestate.csv","r") as fobj:
    dummy = fobj.readline()
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        city = output[1]
        # dict[key]  = somevalue
        citydict[city] = 1

for item in citydict:
    print(item)
