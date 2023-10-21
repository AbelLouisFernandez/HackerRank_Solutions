#https://www.hackerrank.com/challenges/compare-the-triplets/problem
import os
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
def compareTriplets(a, b):
    ascore=0                     #Score of alice and bob are initialized as ascore and bscore respectively(set to 0) 
    bscore=0
    index = len(a)                     
    for ind in range(index):             #loop through each score of a and b and comparing it with each other
        if a[ind]>b[ind]:                #if score of a is greater a is rewarded a point
            ascore+=1
        elif a[ind]==b[ind]:             #if both are equal its passed
            pass
        else:                            #if score of b is greater b is rewarded a point 
            bscore+=1
    listscore=[ascore, bscore]
    return listscore                     #Both scores are returned as a array
            
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()