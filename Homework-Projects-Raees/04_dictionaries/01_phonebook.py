def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}
    print("\n📖 Phonebook Entry Mode (press Enter on name to finish)\n")

    while True:
        name = input("Name: ").strip()
        if name == "":
            break

        if name in phonebook:
            overwrite = input(f"'{name}' already exists. Overwrite? (y/n): ").strip().lower()
            if overwrite != 'y':
                continue

        number = input("Number: ").strip()
        if number == "":
            print("⚠️  Number cannot be empty. Skipping entry.\n")
            continue

        phonebook[name] = number
        print(f"✅ Added: {name} -> {number}\n")

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\n📇 Your Phonebook:\n")
    if not phonebook:
        print("📭 Phonebook is empty.\n")
    else:
        for name in sorted(phonebook):
            print(f"{name} ➡️  {phonebook[name]}")
        print()


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers by name.
    """
    print("\n🔎 Lookup Mode (press Enter to exit)\n")
    while True:
        name = input("Enter name to lookup: ").strip()
        if name == "":
            break
        if name not in phonebook:
            print(f"❌ '{name}' is not in the phonebook.\n")
        else:
            print(f"📞 {name}'s number is {phonebook[name]}\n")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()
