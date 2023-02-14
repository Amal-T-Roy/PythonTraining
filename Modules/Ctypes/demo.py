import ctypes
#Cmd to create *.so file from source file:gcc -fPIC -shared -o clibrary.so Clib.c

#create an object for c library->Absolute path reccommended
clibrary = ctypes.CDLL("/home/amalr/Desktop/PythonTraining/Modules/Ctypes/clibrary.so") #Dynamic linked library
clibrary.Display('Dude',18) #Calling function in c file
#Above function call result will have only 1 char in string part as we cant pass string array to c file

#To pass string array,we should pass it as binary string(add a b infront of the string)
clibrary.Display(b'Dude',18) #Calling function in c file



#Another method
func = clibrary.Display #Map the function to a variable

func.argtypes = [ctypes.c_char_p,ctypes.c_int] #pass as character pointer and int

func(b'Bruh',20)