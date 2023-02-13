import sys

print(dir(sys)) #shows all attributes&methods associated with the module

sys.stderr.write('Test\n')
sys.stderr.flush()
#To print current file path
print(sys.argv)