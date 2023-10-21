#https://www.hackerrank.com/challenges/simple-array-sum/problem
import os
def simpleArraySum(ar):
    summed = 0                                #This function loops through each element in array and add it to return the sum of the elements of array 
    for number in ar:
        summed+=number
    return summed
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()