def Check_if_Prime(Num) :
    if Num >= 1:
        for i in range(2,Num,) :
            if((Num%i)==0) :
                return False
                break
            else :
                return True
                break
    else :  
        print('Invalid Input')

#Test input
Inputs = [1,2,3,4,5,6]

#map iteraqtes the list and apply the func to each element
print(list(map(Check_if_Prime,Inputs)))

#Filter function return the values which return true for the function
print(list(filter(Check_if_Prime,Inputs)))