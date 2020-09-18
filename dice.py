import random

class Die:
    def __init__(self):
        self.throw = 0

    def side(self):
        self.throw = random.randint(1,6)

    def Get_Value(self):
        return self.throw

d = Die()
d.side()
d_Value = d.Get_Value()
print(d_Value)
    
