
# executing system command
# method1 :  os.system()
# method2 :  using subprocess library


import subprocess

output = subprocess.getoutput("dir")
print(output)
