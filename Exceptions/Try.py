
a = 10
b = 0

# print(a/b)

try : 
    print(a/b)
except Exception as e:
    print("Invalid Operation : ",e)
finally:
    print("Operation Completed")