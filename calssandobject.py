class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print("the car informaton is: ")
        print(f"Make: {self.make}\n Model:{self.model}\n Year:{self.year}")

    def update(self,new_year):
        self.year=new_year
        print("the new year is updated for a car : ")


car1=car("lamborgini","camry",2005)
car1.display()
car1.update(2010)
car1.display()