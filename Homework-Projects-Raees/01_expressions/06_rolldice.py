def roldice():
    import random
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)
    total: int = dice1 + dice2  
    print(f"You rolled a {dice1} and a {dice2} for a total of {total}")

if __name__ == "__main__":
    roldice()