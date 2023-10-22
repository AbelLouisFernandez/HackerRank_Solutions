#https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, l):
    value = l[n - 1]           #Rigthmost value of the list is stored in value variable
    j = n - 2                   # Start from the second-to-last element (index n-2)   
    while j >= 0 and l[j] > value:   #checking if the left value is greater than right one
        l[j + 1] = l[j]              #if true right value is changed to that of left one 
        j -= 1                       #j is decremented to compared it to next left value
        print(" ".join(map(str, l)))  #list is printed with right value changed to left one
    l[j + 1] = value                #after while breaks when left value is lesser than right one its swapped with rightmost value which was stored at first
    print(" ".join(map(str, l)))    #list is printed after the swap
            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
