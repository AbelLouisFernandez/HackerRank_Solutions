#https://www.hackerrank.com/challenges/time-conversion/problem
import os
def timeConversion(s):
    if 'AM' in s:                           #First checks if the time is in AM 
        s=s.split(':')                      #Its then splited to get number in str
        if s[0]=='12':                      #Checks if the hour is 12
            s[0]='00'                       #if true it converts it into 00
            result = "{}:{}:{}".format(*s)  #Its converted to string 
            result=result.replace('AM', '') #AM is removed from string and returned
            return result
        else:
            result = "{}:{}:{}".format(*s)   #if s[0]!=12 it just removes AM part of the time as first 12 hours are same for both clocks(except for 12)
            result=result.replace('AM', '')
            return result
    else:                                  #if its in PM
        s=s.split(':')
        if s[0]=='12':                   #Check if the hour is 12    
            result = "{}:{}:{}".format(*s) #If yes then only PM part is removed
            result=result.replace('PM', '')
            return result
        else:
            hour=int(s[0])+12           #if hour is not 12, 12 is added to hour to make it into 24 hour clock and PM is removed
            hour=str(hour)
            s[0]=hour
            result = "{}:{}:{}".format(*s)
            result=result.replace('PM', '')
            return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()