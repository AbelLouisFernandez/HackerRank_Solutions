#https://www.hackerrank.com/challenges/kangaroo/problem
import os
def kangaroo(x1, v1, x2, v2):    #x1,x2 are starting location of kangaroo 1 and 2 ,v1 and v2 are jump of kangaroo 1 and 2
    for i in range(10000):       #Brute force method of loop to calculate the distances upto 10000 jumps 
        x1+=v1
        x2+=v2
        if x1==x2:              #After each jump they are checked to be of same distance 
            passed=True         #if true passed flag is set to True and loop is breaked
            break
        else:                   #else passed flag is set to False
            passed=False
    if passed is True:          #After the loop flag is checked if true its displayed YES else its displayed NO
        return('YES')
    else:
        return('NO')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()