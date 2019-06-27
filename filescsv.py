#write a program to list ONLY .csv files of the current directory with proper exception handling
import os
for file in os.listdir():
    if file.endswith(".py"):
        print(file)

## get the file size
print(os.path.getsize("realestate.csv") , "bytes")

## display all files where size > 0
for file in os.listdir():
    if os.path.getsize(file) >  0 :
        print(file)
