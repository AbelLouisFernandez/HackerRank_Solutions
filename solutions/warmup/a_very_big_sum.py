#https://www.hackerrank.com/challenges/a-very-big-sum/problem
import os

def aVeryBigSum(ar):
    summed=0
    for number in ar:                        #  This is same as simple_array_sum.py because python manages big array easily no extra code is needed
        summed+=number
    return summed
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
