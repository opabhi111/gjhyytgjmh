try:
    
    A = int(input("enter number :"))
    B = int(input("enter number :"))
    print("what kind of operation you want to perform : 1. addition(+)\n 2. subtraction(-)\n 3. multiplication(*)\n 4. division(/)")

    o = input("enter operation :")
except Exception as e:

    print("invalid input")
    exit()

if o == "+":
    print("the sum is", A + B)
elif o == "-":
    print("the difference is", A - B)
elif o == "*":
    print("the product is", A * B)
elif o == "/":
    print("the quotient is", A / B)  