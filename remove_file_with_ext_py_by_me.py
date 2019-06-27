import os

#print(os.getlogin())

PYDIR = "C:/Users/vb1017665/Desktop/py/"

#print (os.listdir(PYDIR))

for listd in os.listdir(PYDIR):
#    print (listd)#
#    print (listd.split('.')[1])
    if listd.split('.')[1] == 'py':
#        print(listd)
#        print (PYDIR+listd)
#        fileremove = "PYDIR, "\\" , "listd""
        fileremove = (PYDIR + listd)
        print (fileremove)
        os.remove(fileremove)
os.rmdir(PYDIR)
#        print (PYDIR+listd)