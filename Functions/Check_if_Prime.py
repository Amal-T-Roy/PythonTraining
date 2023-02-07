def Check_if_Prime(Num) :
    if Num > 1:
        for i in range(2,Num,) :
            if((Num%i)==0) :
                print('Not a prime')
                break
            else :
                print('Prime Number')
                break
    else :  
        print('Not a prime')


Check_if_Prime(7)
Check_if_Prime(8)
Check_if_Prime(0)
