class shape:
    def area(self):
        pass
    def perimeter(self):
        pass


class Rectangle(shape):
    def __init__(self,w,h):   
        self.w=w
        self.h=h
    def  area(self):
        return self.w *self.h

    def perimeter(self):
        return  2 * (self.w + self.h)
    

class circle(shape):
    def __init__(self,radis):
        self.radis=radis
    def area(self):
        return 3.1416 * self.radis**2
    
    def perimeter(self):
        return 2 *3.1416*self.radis

rect=Rectangle(8,9)
print("the area  of rectandle : ",rect.area())
print("the  peremeter of rectangle is: ",rect.perimeter())


circlee=circle(5)
print("the area of circles : ",circlee.area())
print("the rectangle of circle is : ",circlee.perimeter())
