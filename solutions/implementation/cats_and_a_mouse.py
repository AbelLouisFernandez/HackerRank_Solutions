#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
import os
def catAndMouse(x, y, z): #x and y is location of cat A and B ,z is location of mouse C
    if abs(z-y)<abs(z-x):    #checking if the distance of cat b is less than a using abs() to get absolute value 
        return('Cat B')      #if true displayed cat b
    if abs(z-y)>abs(z-x):    #checking if a is closer than b
        return('Cat A')      #if true displayed cat a
    if abs(z-y)==abs(z-y):   #checking if both are of same distance
        return('Mouse C')    #if true displayed mouse c
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()