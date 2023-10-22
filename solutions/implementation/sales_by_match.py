#https://www.hackerrank.com/challenges/sock-merchant/problem
import os
def sockMerchant(n, ar):
    summed=0          #no of pair is set to zero 
    arr=set(ar)      #using set function to get unique values
    for i in arr:      #looping through unique values and calculating the count in original list
        count=ar.count(i)  
        summed+=count//2  #dividing by to find the no of pairs and its added to total no of pairs
    return summed #total no of pairs of socks returned

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()