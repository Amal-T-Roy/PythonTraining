class TopTen:
    def __init__(self) :
        self.num = 1 #init with 1 as value

    def __iter__(self) :
        return self
    
    def __next__(self) :
        
        if self.num <= 10 :
            val = self.num
            self.num += 1
            return val
        else :
            raise StopIteration
        
values = TopTen()

print(next(values)) #print 1st value

for i in values :
    print(i) #prints the rest