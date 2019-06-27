city = []
with open("C:/Users/vb1017665/PycharmProjects/learning/python_training_day-2/Sacramentorealestatetransactions.csv","r") as fobj:
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        city.append(output[1])

for item in city:
    print(item)