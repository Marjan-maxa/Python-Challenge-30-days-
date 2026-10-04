
try:
    def calculate(num1, operator, num2):
        
        
        if operator == "+":
            
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        elif operator == "%":
            return num1 % num2
        elif operator == "**":
            return num1 ** num2
        elif operator == "//":
            return num1 // num2
        else:
            
            raise ValueError("Unsupported operator")


    num1 = float(input("Enter a first number: "))
    operator = input("Enter operator (+, -, *, /, %, **, //): ")
    num2 = float(input("Enter a second number: "))
    print(calculate(num1, operator, num2))
    result=calculate(num1,operator,num2)
    print("Result is :",result)
except ValueError as e:
    print(e)
    















