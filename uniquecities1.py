
try:
    city = []
    with open("realestate111.csv","r") as fobj:
        for line in fobj:
            line = line.strip()
            output = line.split(",")
            city.append(output[1])

    for item in city:
        print(item)
except:
    print("Error occured")
    print("file not found")

    

