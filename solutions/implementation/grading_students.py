#https://www.hackerrank.com/challenges/grading/problem
import os
def gradingStudents(grades):
    multiples=[40,45,50,55,60,65,70,75,80,85,90,95,100] #array containing mulitples of 5 from 40 
    length=len(grades)
    for i in range(length):         #looping thorugh each grade in array
        if grades[i]<38:            #if grade is below 38 no need to round so its passed
            pass
        else:
            for multiple in multiples: # if grade is above 38 its compared with elements in mutliples array to find the closet muliptle of 5
                if multiple>grades[i]:
                   if multiple-grades[i]<3: # checking if difference between multiple and grade is less than 3
                       grades[i]=multiple   #if difference is less than 3 its rounded to multiple by changing value of the grades array
                       break
    return grades
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()