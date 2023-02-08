class student :
    def __init__(self,m1,m2) :
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other) :
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3
    
    def __gt__(self,other) :
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if(r1 > r2) :
            return True
        else :
            return False

s1 = student(49,48)
s2 = student(47,50)

#To add members of <class student>,we overload '+' operator(i.e __add__ method)
s3 = s1 + s2

print(s3.m1)
print(s3.m2)

#check who has more marks by overloading '>' operator(i.e __gt__ method)
if s1 > s2 :
    print('S1 is better')
else :
    print('S2 is better')