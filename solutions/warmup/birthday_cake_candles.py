#https://www.hackerrank.com/challenges/birthday-cake-candles/problem
import os
def birthdayCakeCandles(candles):                      
    highestcandle=max(candles)                     #Maximum of candles array is calculated using inbuilt max function
    counted=candles.count(highestcandle)           #Count of maximum is calculated using inbuilt count function
    return counted                                 #Count of maximum candles is returned
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()