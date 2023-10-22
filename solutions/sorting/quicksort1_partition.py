#https://www.hackerrank.com/challenges/quicksort1/problem
import os

def quickSort(arr):
    rigth=[]      #three emppty list to store left,right and equal elements after comparing with pivot element
    left=[]
    equal=[]
    for i in range(0, len(arr)): #looping through the list of elements and comparing it with pivot element
        if arr[i]<arr[0]:         #arr[0] is chosen as pivot element
            left.append(arr[i])   #if element is less than pivot element its appended to left list
        if arr[i]>arr[0]:
            rigth.append(arr[i])   #if element is greater than pivot element its appended to right list
        if arr[i]==arr[0]:
            equal.append(arr[i])   #if element is equal to pivot element its appended to equal list
    return left+equal+rigth     #three list are merged in order and returned
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()