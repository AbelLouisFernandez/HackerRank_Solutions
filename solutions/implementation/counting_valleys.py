#https://www.hackerrank.com/challenges/counting-valleys/problem
import os
def countingValleys(steps, path):    #path is string containing U for up and D for down after one cycle its counted
    valleys=0             #no of valleys set to zero and level indicating the current postion of hiker set to zero 
    level=0
    in_valley=False       #flag indicating if the hiker has entered a valley or not
    for step in path:     #Iterating through the string
        if step=='U':     #if character is U level is incremented
            level+=1
        else:              #if its D level is decremented
            level-=1
        if level<0 and not in_valley: #Checking if the position is less than 0 or ground level and flag state
            in_valley=True            #if flag state is flase its set to true
        if level>=0 and in_valley:    #if the level is over ground level and flag is set to true
            valleys+=1                #no of valleys is incremented and flag is set to false
            in_valley=False
    return valleys              #return the no of valleys
            
        
                
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
