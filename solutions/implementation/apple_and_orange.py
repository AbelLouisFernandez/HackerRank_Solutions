#https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges): #s,t are start and end location of house,a and b are location of apple and orange tree respectively
    applecount=0                                    
    orangecount=0
    for apple in apples:    #each distance of fallen apple is looped 
        apple=apple+a       #distance is added with location of apple tree
        if apple>=s and apple<=t: #checking if the distance with location added is in location of house
            applecount+=1         #if true fallen apple is counted
    for orange in oranges:   #same process like apple is done for orange distances
        orange=orange+b
        if orange<=t and orange>=s:
            orangecount+=1
    print(applecount)                 #count of fallen apple and orange in house location is displayed in differnt lines
    print(orangecount)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
