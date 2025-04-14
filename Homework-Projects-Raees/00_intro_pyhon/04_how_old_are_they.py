# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

# Anton is 3

# Beth is 4

# Chen is 5

# Drew is 6

# Ethan is 7
# #

print ("04_how_old_are_they")
def ages_name():
    anton_age:int  = 21
    beth_age:int   = 6  + anton_age
    chen_age:int   = 20 + beth_age
    drew_age:int   = chen_age + anton_age
    ehan_age:int   = chen_age


    print("Anton age is " + str(anton_age))
    print("Beth  age is "  + str(beth_age))
    print("Chen  age is "  + str(chen_age))
    print("Drew  age is "  + str(drew_age))
    print("Ehan  age is "  + str(ehan_age))

if __name__ == "__main__":

    ages_name()

