def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    if len(lst) == 0:
        print("The list is empty. No last element to display.")
    else:
        print("Last element:", lst[-1])

def get_last():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_last()
    get_last_element(lst)

if __name__ == '__main__':
    main()
