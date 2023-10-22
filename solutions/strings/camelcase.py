#https://www.hackerrank.com/challenges/camelcase/problem
import os
def camelcase(s):               
    summed=0            #No of capital letter is set to zero
    for i in s:         #iterating through the string 
        if i.isupper(): #checking if the character is uppercase using .isupper() function
            summed+=1   #if true count of captial letters is incremented
    return summed+1  #Captial letters denote starting of words but the first letter of sentence is small letter so no of capital letters+1 is returned
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()