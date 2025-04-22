def reminder ():
    num1 = int(input("Enter a number to be divided: "))
    num2 = int(input("Enter the divisor: "))
    result = num1 % num2
    quotient = num1 // num2
    print(f"The remainder of {num1} and {num2} is {result}")

if __name__ == "__main__":
    reminder()
