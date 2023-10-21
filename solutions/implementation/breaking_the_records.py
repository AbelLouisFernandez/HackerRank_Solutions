#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
import os
def breakingRecords(scores):             
    bestscore=scores[0]        #first score is intialized as bestscore               
    bestscore1=scores[0]       #Copy of the bestscore
    bestscorecount=0           #Count of better scores and worse score
    worstscorecount=0          
    worstscore=-1             #worsescore is intialized as -1 as zero can be a score in scores
    for score in scores:      
        if bestscore<score:   #looping can comparing scores with bestscore if the score is more 
            bestscore=score   #then bestscore is changed to present score and count is incremented
            bestscorecount+=1
        if bestscore>score and worstscore==-1: #Setting the worstscore
            if bestscore1>score:               #Checking if worstscore is less than first bestscore if not its not taken as worstscore
                worstscore=score
                worstscorecount+=1
        if worstscore!=-1:         #after the worstscore is set its compare with upcoming scores in array to count worstscores
            if worstscore>score:
                worstscorecount+=1
                worstscore=score
    lizt=[bestscorecount, worstscorecount]  #bestscorecount and worstscorecount is returned as an array
    return lizt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()