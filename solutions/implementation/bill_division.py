#https://www.hackerrank.com/challenges/bon-appetit/problem
def bonAppetit(bill, k, b): #bill is list of price of items,k is the index of item anna declined,b is amount brian calculated
    summed=0       #amount anna have to pay is set to zero
    for i in range(len(bill)): #looping through items in bill
        if i==k:               #if the item is same as declined item its passed
            pass
        else:                  #else the item's amount is added to amount anna have to pay
            summed+=bill[i]
    summed=summed//2          #divided by 2 to divide the amount between anna and brian
    if b==summed:             #if amount brian calculated is same as original amount then bon appetit is displayed
        print('Bon Appetit')
    if b>summed:             #else we calculate the difference and display it.
        print(b-summed)
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)