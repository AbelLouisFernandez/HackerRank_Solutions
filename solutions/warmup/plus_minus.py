#https://www.hackerrank.com/challenges/plus-minus/problem
def plusMinus(arr):
    noofpostive=0                                 #No of postive,negative and zero are set to zero 
    noofnegative=0
    noofzero=0
    for element in arr:                           #Each element is looped through and compared with zero to check postive,negative
        if element<0:
            noofpostive+=1
        if element>0:
            noofnegative+=1
        if element==0:
            noofzero+=1
    length=len(arr)
    noofpostive=noofpostive/length
    noofnegative=noofnegative/length
    noofzero=noofzero/length                   #Display the no of postive, negative and zero in differnt lines
    print(noofnegative)
    print(noofpostive)
    print(noofzero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)