def get_user_numbers():
    """
    Prompt the user to enter numbers and store them in a list.
    Stops when the user enters a blank line. Handles invalid input gracefully.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        
        if user_input == "":
            break
        
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
    return user_numbers


def count_nums(num_lst):
    """
    Counts the frequency of each number in the list and returns a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict


def print_counts(num_dict):
    """
    Prints how many times each number appears, sorted in ascending order.
    """
    print("\n📊 Number Frequencies:")
    for num in sorted(num_dict):
        print(f"{num} appears {num_dict[num]} time(s).")


def main():
    print("📥 Number Counter\n")
    user_numbers = get_user_numbers()

    if not user_numbers:
        print("⚠️ No numbers were entered.")
    else:
        num_dict = count_nums(user_numbers)
        print_counts(num_dict)


# Python boilerplate
if __name__ == '__main__':
    main()
