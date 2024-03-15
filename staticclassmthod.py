class mathutils:
    def factorial(num):
        if num==0:
            return 1
        else:
            return num * mathutils.factorial(num-1)

    def square(n):
        return n**2



print("factorial of 7 is : ",mathutils.factorial(7))
print("square of 6 is : ",mathutils.square(6))