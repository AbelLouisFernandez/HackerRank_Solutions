#https://www.hackerrank.com/challenges/runningtime/problem
import os 
def runningTime(l):
    rotate=0           #same logic as insertion sort 2 only extra variable roatate that counts how many times list is rearranged 
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            rotate+=1
            j -= 1
            l[j+1] = key
    return rotate
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()