#write a program to count the no.of files and directories in the current directory.
#No. of files       : 33
#No. of directories : 2
import os
files = []
dirs = []
for file in os.listdir():
    if os.path.isfile(file):
        files.append(file)
    elif os.path.isdir(file):
        dirs.append(file)
        
print("****** FILES *******")
for file in files:
    print(file)
print("****** DIRS *********")
if len(dirs) == 0 :
    print("No directories")
else:
    for file in dirs:
        print(file)
