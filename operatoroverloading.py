class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__  (self,other):
        return vector(self.x + other.x, self.y+other.y)

    def __sub__(self,other):
        return vector(self.x - other.x , self.y-other.y) 

    def __mul__(self,scalar):
        return vector(self.x * scalar.x ,self.y *scalar.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

       

v1=vector(10,20)
v2=vector(3,4)
result= v1+v2
print("the additon two value: ",result)

result=v1-v2
print("the subtraction is two value: ",result)

