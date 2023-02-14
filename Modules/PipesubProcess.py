import subprocess
import os

print(os.getcwd())
p1 = subprocess.run(['cat','Test.txt'],capture_output = True, text = True)

#stdout of 1st process is passed as i/p to p2
#-n flag gives the line in which the parameter we are searching is found
p2 = subprocess.run(['grep','-n','Test'],capture_output = True , input = p1.stdout,text = True)
print(p2.stdout)
# print(p2.stderr)