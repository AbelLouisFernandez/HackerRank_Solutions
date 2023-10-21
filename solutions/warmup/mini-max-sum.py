#https://www.hackerrank.com/challenges/mini-max-sum/problem
def miniMaxSum(arr):
    arr.sort()                 #arr is sorted ascending order to get least element at front and large element as last
    mini=0                     #Max_sum and min_sum is set to zero
    maxi=0
    for i in range(len(arr)-1):    #through loop sum of first four elements taken to get minimum sum
        mini+=arr[i]
    for i in range(1,len(arr)):    #through loop sum of last four elements taken to get maximum sum this works because the input arr has fixed length of 5
        maxi+=arr[i]
    mini=str(mini)
    maxi=str(maxi)
    print(mini+' '+maxi)
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
