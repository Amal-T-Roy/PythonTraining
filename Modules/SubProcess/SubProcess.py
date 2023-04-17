import subprocess

subprocess.run('ls') #List contents of curr directory->Here,Uses linux cmd
print() #Just print  blank line 
subprocess.run('dir') #Windows command

"""
If we get file not found error when running in  windowspas shell = True as an arg.
,As the dir cmd is built into the shell.
It also allows to pass more than 1 arg as a string(eg: ls -la)
)
"""
subprocess.run(['ls','-la']) #Without enabling shell ->Pass args as a list
print()
subprocess.run('ls -la',shell=True) #With shell we can all args as a single string

#To capture output instead of directly printing on console
x = subprocess.run('ls',capture_output=True)
# print(x)
print(x.stdout)
#print(x.stdout.decode()) #Decodes->Above line,\n is printed as string->This line rectifies it
"""The above can be achieved by passing text = True as an arg in subprocess.run()"""
x = subprocess.run('ls',capture_output = True,text = True)
print(x.stdout)
# x = subprocess.run('ls',stdout =subprocess.PIPE,text = True) #Same as line 18,but atderr is also piped


print(x.args) #Prints the arguments passed

#Pipe into a file   
with open('Output.txt','w') as f:
    x = subprocess.run('ls',stdout = f,text = True)
    print(x.stderr)