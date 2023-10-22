#https://www.hackerrank.com/challenges/insertionsort2/problem

def insertionSort2(n, arr):
    for i in range(1, n):       #each value is iterated 
        key = arr[i]            #value is stored that is to be compared with the left ones
        j = i - 1               #j is store index of left value
        while j >= 0 and key < arr[j]: #value is compared 
            arr[j + 1] = arr[j]        #if left value is greater than right value its changed 
            j -= 1                     #j is decremented to compare next value
        arr[j + 1] = key               #after while loop when left value is less than right value,right value is changed to value store in key variable
        print(*arr)                    #arr is printed as string after each iteration 



    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)