import random

def dice_simulator():
    die1: int = random.randint(1, 6)  # fixed typo: ranint -> randint
    die2: int = random.randint(1, 6)
    total: int = die1 + die2
    print(f"Total of two dice: {total}")

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    dice_simulator()
    dice_simulator()
    dice_simulator()
    print("die1 in main() is: " + str(die1))

if __name__ == "__main__":  
    main()  
