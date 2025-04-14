def triangle_perimeter():
    print("To sum of triangle")
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))
    total: float = (side1 + side2 + side3)
   
    print("The perimeter of the triangle is " + str(total))

if __name__ == "__main__":
    triangle_perimeter()
