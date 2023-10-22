#https://www.hackerrank.com/challenges/countingsort2/problem
import os

def countingSort(arr):
    frequencyarray=[]
    for i in range(100):     #frequencyarray like  counting_sort_1.py
        frequencyarray.append(0)
    for value in arr:
        frequencyarray[value]=frequencyarray[value]+1
    sortedarray=[]          #Using that frequencyarray we are going to sort the list
    for frequency in range(len(frequencyarray)): #we iterate through the frequencyarray
        if frequencyarray[frequency]!=0:         #if the value is not zero,
            for j in range(frequencyarray[frequency]): #elements value is used as range limit and index of the element is appended to the sortedlist
                sortedarray.append(frequency)
    return sortedarray        #return the sorted array
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
