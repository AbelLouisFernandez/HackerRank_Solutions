#https://www.hackerrank.com/challenges/the-birthday-bar/problem
import os
def birthday(s, d, m):
    summed=0                #the no of chcocolatebar combination is set to zero                     
    for i in range(len(s)):
        isum=s[i]            #looping through each element and assigning it to sum of bars 
        for z in range(1, m): #m is the no of bars that can be combined
            if i+z>=(len(s)): #if combination is out of the index of array the loop is break
                break
            else:             #else the sum is added with adjacent element
                isum+=s[i+z]
        if isum==d: #after getting the sum of combination if sum is equal to day of birthday count of combination is incremented
            summed+=1
    return summed #no of combinations is returned
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()