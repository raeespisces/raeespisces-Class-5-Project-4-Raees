def energy():  
    c: int = 299_792_458  # speed of light in m/s
    m: float = float(input("Enter the mass in kilograms: "))
    print("E = m * c^2")
    print("Mass = " + str(m) + " kg")  # fixed: convert m (float) to str
    print("c = " + str(c) + " m/s")    # fixed: convert c (int) to str
    print("E = " + str(m * c**2) + " J ")

def main():
    energy()

if __name__ == "__main__":
    main()
