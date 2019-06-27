

try: 
    city = [] 
    with open("realestate.csv","r") as fobj:
        for line in fobj: 
            line = line.strip() 
            output = line.split(",") 
            city.append(output[1]) 
        for item in city: 
            print(item)
except FileNotFoundError as error: 
    print("File doesn't exist") 
    print("System error :", error)  
except Exception as error: 
    print("Some other different exception") 
    print("System error :", error)


