#https://www.hackerrank.com/challenges/diagonal-difference/problem
import os

def diagonalDifference(arr):                       #This function accepts a nested array to simulate matrix
    diagonalsum=0                                  #Sum of both diagonal are set to zero 
    leftdiagonalsum=0                               
    n=len(arr)
    for i in range(n):                            # Looped through the array arr[i][i] get the elements of major diagonal
        diagonalsum+=arr[i][i]
        leftdiagonalsum+=arr[i][n-1-i]            #arr[i][n-i-1] indexing is used to get the elements of left diagonal  
    return abs(diagonalsum-leftdiagonalsum)       #Absolute difference of sum of diagonals is returned
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
