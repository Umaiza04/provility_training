#defining a function
def func():
    print("hello world")
func() # calling through a function

#passing values in function
def oddeven(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
print(oddeven(2))

#lambda function
square=lambda x: x*x
print(square(2))

#finding sum and product using lambda functions
SumProd=lambda x,y : (x+y,x*y)
print(SumProd(2,3))
