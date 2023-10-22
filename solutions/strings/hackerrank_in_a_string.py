#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
import os
def hackerrankInString(s):
    target = "hackerrank"
    i = 0                    # Index in the target string

    for char in s:             #iterating thorugh the given string 
        if char == target[i]:  #checking if charcter in string matches to 1st element of target string
            i += 1             #if true index of target string is incremented
            if i == len(target): #if index of target reaches the length of the target it means the target present in the given string
                return "YES"     #yes is returned

    return "NO" #if index doesnt match no is returned

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()