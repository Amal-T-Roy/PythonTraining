Calender = [0,31,28,31,30,31,30,31,31,30,31,30,31]
print(len(Calender))

def If_Leap_Year(year) :
    '''return true for leap year'''
    if(year > 0) :
        if((year % 4 == 0) or ((year % 400 == 0) and  (year % 100 == 0))): 
            return True
        else :
            return False
    else :
        return 'Invalid year input'

print(If_Leap_Year(2001))
print(If_Leap_Year(2000))
print(If_Leap_Year(2024))

def days_in_month(month) :
    if(month < 0 or month >12) :
        print('Invalid month')
        return 'Invalid input for month'
    else :
        if (If_Leap_Year(year) == True and month == 2) :
            return 29
        else :
            return Calender[month]


year = int(input('Enter the year'))

print('Leap Year = ',If_Leap_Year(year))

Month = int(input('Enter the month as digit'))

print('No.of days = ',days_in_month(Month))