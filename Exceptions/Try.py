
a = 10
b = 0
c = 'k'

# print(a/b)

try : 
    print(a/b)
    # print(a/c)
except ValueError as e:
    print("Value Error")
except ZeroDivisionError as e:
    print("Zero Division Error")
except Exception as e:
    print("Something went wrong: ",e)
finally:
    print("Operation Completed")