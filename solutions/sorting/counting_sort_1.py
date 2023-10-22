#https://www.hackerrank.com/challenges/countingsort1/problem
import os

def countingSort(arr):
    frequencyarray=[]
    for i in range(100):        #Creating a frequency array of size 100 by appending zeros        
        frequencyarray.append(0)
    for value in arr:          #Iterating through the values in arr list
        frequencyarray[value]=frequencyarray[value]+1    #for each value the value at that index is incremented
    return frequencyarray  #frequencyarray is returned
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()