num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")
if operation=='+':
    result=num1+num2
    print("Result:", result)
elif operation=='-':
    result=num1-num2
    print("Result:", result)    
elif operation=='*':
    result=num1*num2
    print("Result:", result)
elif operation=='/':
    if num2!=0:
        result=num1/num2
        print("Result:", result)
    else:
        print("Error: Division by zero")