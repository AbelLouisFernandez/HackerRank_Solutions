#https://www.hackerrank.com/challenges/tutorial-intro/problem
import os 
def introTutorial(V, arr):
    return arr.index(V)   #Using Index function V is passed an argument and index of V is returned


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()