#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
import os
def divisibleSumPairs(n, k, ar):
    summed=0               #no of pairs is set to zero
    length=len(ar)          
    for i in range(length):#elements are looped 
        j=i+1   #j is set to adjancent element of the selected element
        for z in range(j, length): #range starting from j to prevent the previous elements
            summed1=ar[i]+ar[z] #the elements are summed
            if summed1%k==0: #if the elements sum is divisible by the given number pair count is incremented 
                summed+=1
    return summed #no of pairs is returned
                 
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()