class calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divided(self,x,y):
        return x/y


cal=calculator()
print("the addition is: ",cal.add(10,20))
print("the  subtraction is : ",cal.sub(20,4))
print("the multiplicaton is : ",cal.multiply(5,5))
print("the divisiln is : ",cal.divided(15,3))