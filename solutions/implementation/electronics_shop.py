#https://www.hackerrank.com/challenges/electronics-shop/problem
import os
def getMoneySpent(keyboards, drives, b): 
    canbuy=[]                  #canbuy is list of amount of keyboard and mouse she can afford to buy
    for keyboard in keyboards: #looping through keyboard and mouse using nested loop to get all combinations
        for drive in drives:
            if b>=(keyboard+drive): #checking if the sum of both is less than or equal to the amount she have
                canbuy.append(keyboard+drive) #if true the amount of combination is appended to canbuy list
    if canbuy==[]: #after loop checking if canbuy is empty means she cant buy any combination
        return -1 #if true -1 is return 
    else:            
        return max(canbuy) #else maximum amount of combination she can buy is returned

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
