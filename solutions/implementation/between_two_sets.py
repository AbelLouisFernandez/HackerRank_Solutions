#https://www.hackerrank.com/challenges/between-two-sets/problem
import os
def getTotalX(a, b):
    max_a = max(a)   #to get max value and min value of a and b array to find range of factors  
    min_b = min(b)
    count = 0

    for i in range(max_a, min_b + 1): #loop through the range of potential factors 
        if all(i % num == 0 for num in a) and all(num % i == 0 for num in b):  #first condition of if checks if the number is muliptle of all in a second condition checks if the number factor or all in b 
            count += 1      #if both condtions are true no of factors is incremented by 1

    return count #no of factors returned
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()