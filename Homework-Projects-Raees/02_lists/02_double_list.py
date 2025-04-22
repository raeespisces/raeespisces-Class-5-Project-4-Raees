def double_list():
    numbers: list[int] = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
        element_index= numbers[i]
        numbers[i] = element_index * 2
    print(numbers)

if __name__ == "__main__":
    double_list()
    
