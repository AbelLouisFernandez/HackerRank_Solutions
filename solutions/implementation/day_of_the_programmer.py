#https://www.hackerrank.com/challenges/day-of-the-programmer/problem
import os

def dayOfProgrammer(year):
    if year<1918:               #There are three cases the year before 1918,during 1918 and after 1918
        if year% 4==0:          #if the year is before 1918 we only have check if its divisible by 4
            return "12."+"09."+str(year) #if true we return 12/09 with that year concated
        else:
            return "13."+"09."+str(year) #else 13/09 is returned
    if year==1918:                        #the year 1918 is an exception case we dont have to check leap year
        return "26."+"09."+str(year)      #directly print the date 26/09 beacuse its calender during which switch was made
    else:                                 #after 1918 we check if year is divisible by 400 or by 4  and not by 100 
        if year% 400==0 or year% 4==0 and year% 100 !=0:
            return "12."+"09."+str(year)
        else:
            return "13."+"09."+str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()