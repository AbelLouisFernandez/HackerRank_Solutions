#https://www.hackerrank.com/challenges/migratory-birds/problem
import os
def migratoryBirds(arr):
    lst=max(set(arr), key=arr.count) #set function converts array into array of distinct elements only
    #key finds the no of occurence of each element in original array and max function finds the elements which has most occurences 
    return lst   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()