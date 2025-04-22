inches:int = 12
def feet_to_inches ():
    feet:int = int(input("Enter the number of feet: "))
    print(f"{feet} feet is {feet * inches} inches")

def main():
    feet_to_inches()

if __name__ == "__main__":
    main()
