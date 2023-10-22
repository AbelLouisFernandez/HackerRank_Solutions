#https://www.hackerrank.com/challenges/mars-exploration/problem
import os
def marsExploration(s):          
    lasti=0       #no of altered charcters is set to zero
    lizt=[]
    for i in range(3,len(s)+1,3): #iterating through the string ,starting from 3 because to extract the substrings of each sos,jumping 3 in range
        lizt.append(s[lasti:i]) #substring is obtained and appended to a list 
        lasti=i        #last index is made a copy to use as starting index of substring in next iteration
    countz=0
    for i in lizt:    #Each substring is checked for missing character in thier SOS order
        if i[0]!='S':
            countz+=1
        if i[1]!='O':
            countz+=1
        if i[2]!='S':
            countz+=1
    return countz   #count of missing characters is returned
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()