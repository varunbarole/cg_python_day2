import sys
try:
    city = []
    with open("realestate111.csv","r") as fobj:
        for line in fobj:
            line = line.strip()
            output = line.split(",")
            city.append(output[1])
    for item in city:
        print(item)
    ## logic2
    ## logic3
except ValueError as err:
    print("Invalid operation")
    print("System error :", err)
except TypeError as error:
    print("Invalid input")
    print("System error :", error)
except FileNotFoundError as error:
    print("File doesn't exist")
    print("System error :", error)    
except Exception as error:
    print("Some other different exception")
    print("System error :", error)
    print(sys.exc_info())
