def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
sel=int(input("Enter choice(1/2/3/4):"))
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
if sel==1:
    print(x,"+",y,"=",add(x,y))
elif sel==2:
    print(x,"-",y,"=",subtract(x,y))
elif sel==3:
    print(x,"*",y,"=",multiply(x,y))
elif sel==4:
    try:
        print(x,"/",y,"=",divide(x,y))
    except ValueError as e:
        print(e)
else:
    print("Invalid input")