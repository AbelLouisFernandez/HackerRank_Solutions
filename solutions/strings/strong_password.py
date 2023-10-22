#https://www.hackerrank.com/challenges/strong-password/problem
import os
def minimumNumber(n, password):                                          
    numbers = "0123456789"                         # Predefine character types
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    missing_digits = True                      # flags to track missing character types
    missing_lower = True
    missing_upper = True
    missing_special = True

    for char in password:                   #iterating through password and setting each flag to flase state if the character specified is present
        if char in numbers:
            missing_digits = False
        elif char in lower_case:
            missing_lower = False
        elif char in upper_case:
            missing_upper = False
        elif char in special_characters:
            missing_special = False

    needed_chars = (missing_digits + missing_lower + missing_upper + missing_special) #calculate the missing character by summing up the flags

    if n < 6:               #checking if the length of password is less than 6
        diff = 6 - n        #if true the no of characters to be added to is calculated
        if diff > needed_chars:  #checking if no of characters to be added is greater than missing characters 
            return diff           #if true return no of charcters to be added
        else:
            return needed_chars #else return no of special charcters to be added
    else:                    #even if the password length is more than required if its missing a type of character ,no of missing types is returned
         return needed_chars

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
