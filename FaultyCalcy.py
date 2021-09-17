print("Welcome to faulty calculator:This is develop by Kirtika\n")
print(" + for Addition ")
print(" - for Substration")
print(" * for Multiply ")
print(" / for Division")
print(" ** for Power")
print(" % for modulo\n")


num1=int(input("Enter first Number:\n"))
num2=int(input("Enter second Number:\n"))

operation=input("Enter Your Operator:\n")

if num1 == 45 and num2 == 3 and operation  == "*":
    print(f"{num1}+{num2} = 555")

elif num1 == 56 and num2 == 9 and operation == "+":
    print("f{num1}+{num2} = 77")

elif num1 == 56 and num2 == 6 and operation== "/":
    print(f"{num1}+{num2} =4")

elif operation == "%":
    num4=num1%num2
    print(f"{num1}+{num2} = {num4}")

elif operation == "/":
    num4=num1/num2
    print(f"{num1}+{num2} = {num4}")

elif operation == "*":
    num4=num1*num2
    print(f"{num1}+{num2} = {num4}")

elif operation == "**":
    num4=num1**num2
    print(f"{num1}+{num2} = {num4}")

elif operation == "+":
    num4=num1+num2
    print(f"{num1}+{num2} = {num4}") 

elif operation == "-":
    num4=num1-num2
    print(f"{num1}+{num2} = {num4}")
         
else:
    print("Unexpeted Symbol")          