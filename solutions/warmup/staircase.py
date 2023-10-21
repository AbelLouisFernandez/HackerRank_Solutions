#https://www.hackerrank.com/challenges/staircase/problem
def staircase(n):
    for i in range(1,n+1):         #for loop to print the pattern
        space=n-i                  #space is calculated to print empty space before # using n-i so that it changes in each iteration
        print(space*' '+'#'*i)     #pattern is printed with emptyspace with space no of times and # with i no of times and its concatenated 
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)