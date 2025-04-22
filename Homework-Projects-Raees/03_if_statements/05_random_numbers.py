import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    numbers = []  # Create an empty list to hold the numbers
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)
        numbers.append(num)
    
    print("Generated numbers:", numbers)

if __name__ == '__main__':
    main()
