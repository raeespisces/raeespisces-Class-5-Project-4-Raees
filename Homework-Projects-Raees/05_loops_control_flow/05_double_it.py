def main():
    # Ask the user for a number
    start = int(input("Enter a number: "))
    
    # Set initial value
    curr_value = start * 2
    print(curr_value)

    # Repeat doubling until value is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
    
