

unique = set()
with open("realestate.csv","r", buffering = 1000) as fobj:
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        unique.add(output[1])

for city in unique:
    print(city)
    
