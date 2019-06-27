# fobj can be called as pointer or file variable or file reference
with open("C:/Users/vb1017665/PycharmProjects/learning/python_training_day-2/Sacramentorealestatetransactions.csv","r") as fobj:
    for line in fobj:
        line = line.strip()
        line = line.split(',')
#        print(line)
        print("Street Name is:",line[0],'\n',"City Name is:",line[1],'\n',"============  ",end='\n')
