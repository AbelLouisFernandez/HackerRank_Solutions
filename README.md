# HackerRank_Solutions
>  The repository contains the solutions to HackerRank problems.Solutions have been done using python programming language.All the soltuions are grouped under their specific domain folders.

## appleandorange
- [question](https://www.hackerrank.com/challenges/apple-and-orange/problem)
- [solution](./solutions/implementation/apple_and_orange.py)

 ### Explanation:
>The function takes arguments s,t which are the start and end location of house.a,b which are the location of apple and orange tree respectively.It then intialize two variables applecount,orangecount to count the number of apple which feel inside the location of house.It the uses a for loop to iterate through the distance of apples in apples array.Each time distance of apple is added with location of apple tree and its then compared with location of house and sees if its greater than start location of house and less than end location of house if condition is true the applecount is incremented by 1.The same is done for location of orange in oranges array.After both loop have completed the applecount and orangecount are printed in seprate lines.

### billdivision
- [question](https://www.hackerrank.com/challenges/bon-appetit/problem) 
- [solution](./solutions/implementation/bill_division.py)

 ### Explanation:
 >The function takes three agruments bill which is the list of price of item, k is the index of item anna declined,b is amount brian calculated.A variable summed is intialized to store the amount anna has to pay.Bill list is looped through using index if the index matches with index of item that anna has not eaten its passed less the price is added to summed variable.after the for loop the summed is floor divided by 2 to divide the amount among anna and brain,its then compared with the amount brian has calculated if its same the Bon Appetit is printed if its greater then the difference between amount brian calculated and original amount anna has to pay is printed.

### breaking the records
- [question](https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem)
- [solution](./solutions/implementation/breaking_the_records.py)

### Explanation:
>The function takes a argument scores which is a list of scores.Objective is to find the noofbestscores and noofworstscores.First score is taken has bestscore a copy of it is created in a variable bestscore1.Bestscorecount and worstscorecount variable is intialzed.Worstscore is set to -1 as a flag to start the count of worstscore and intialize first worstscore.for loop is used to iterate thorugh the scores list.every score is compared with bestscore if the score is greater the bestscorescount is incremented by 1 and bestscore is set to current score.if score is not greater and worstscore is -1 the  score is comapred with firstbestscore if its lower than that worstscore it intialized with current score and worstscorecount is incremeneted by -1.In next iteration the second statement will not be checked and it goes to third statement where current score is comapred with the worstscore if its less then worstscorecount is incremeneted by 1 and worstscore is set to current score.After the for loop is list is created with the first element as bestscorecount and second element as worstscorecount and list is returned.

### cats and a mouse
- [question](https://www.hackerrank.com/challenges/cats-and-a-mouse/problem)
- [solution](./solutions/implementation/cats_and_a_mouse.py)

  ### Explanation:
  >The function takes x which is location of cat A y which is the location of cat B and z which is the location of mouse C.It then compares the absolute differnence between the location of mouse and Cat A and location of mouse and Cat B.It compares absolute differnce to know the distance.If the distance of cat a is less than cat b Cat A is printed if cat b's distance is less than cat a's then Cat B is printed.If both cats distance is same the mouse is allowed to escape as per given in question and Mouse C is printed.


### counting valleys
- [question](https://www.hackerrank.com/challenges/counting-valleys/problem)
- [solution](./solutions/implementation/counting_valleys.py)

  ### Explanation:
  >The function takes steps which is the number of step the hiker took and path is a string that containing U for up and D for down after one cycle of D and U its counted as hiker as gone to valley and returned to the plain.Variable valleys is declared to count no of valleys hiker went to and level variable is declared which is indicating the current postion of hiker and currently set to zero,in_valley variable is declared as a flag to know whether the hiker is has entered the valley.Each character in the path string is looped through and its compared with U if they are equal the level is incremeneted by 1 else its decremeneted by 1.if the level is less than 0 and and in_valley is set to false its set to true to know hiker has entered the valley the next statement checks whether the level is greater or equal to zero and in_valley is set to true then if both statment are true this indicates the hiker has traversed a valley and came back to plain so valleys is incrmeneted by 1 and flag is set to false.After the loop is completed the no of valleys traversed is returned.


 ### day of programmer
 - [question](https://www.hackerrank.com/challenges/day-of-the-programmer/problem)
 - [solution](./solutions/implementation/day_of_the_programmer.py)

 ### Explanation:
 >The function takes one argument year which is of integer type.First the year is checked to see if its before 1918 if true its divided by 4 to check if its a leap year if true 12/09/year is printed which is 256th day of a leap year if false 13/09/year is printed.if the year is not before 1918 its checked if its 1918 if true 26/09/year is printed as its 256th day of that year which the calendar switch happened and 14th february was start of february month.If the year is not 1918 then its after 1918 and its divided by 400 if its divisble then its leap year if false its divided by 4  if its divisible then its divided by 100 if its not divisble its leap year and 12/09/year is printed.If all the condition are false its not a leap year and 13/09/year is printed.

 ### divisible sum pairs
 - [question](https://www.hackerrank.com/challenges/divisible-sum-pairs/problem)
 - [solution](./solutions/implementation/divisible_sum_pairs.py)

### Explanation:
 >The function has three arguments ar which is list of numbers,n which is length of the list and k which is the with which the sum is to be divisible with.Variable summed is intialized to count no of the pairs.The list is looped thorough using index and j is intilized with 1 added to the index and a nested for loop is made to find the pair of number which starts from j index to prevent previous numbers of index i then summed1 variable is intialized with the element with i index and j index is added if this summed1 is divisble by k the summed is incremented by 1 after the loop is finished, no of pairs whose sum is divisble by k is returned.

### electronics shop
- [question](https://www.hackerrank.com/challenges/electronics-shop/problem)
- [solution](./solutions/implementation/electronics_shop.py)

### Explanation:
>The function has three arguments keyboards which is the list that contain price of keyboards,drives which contain price of drives and b which is the amount which the person has to buy the keyboard and drive.canbuy list is 
 intialized which is where the amount of keyboard and drive combinations she can buy is stored nested loop is used to loop through keyboards and drives to find the combinations of them if the sum of both things are less than or equal to money she has canbuy is append with the sum of amounts of keyboard and drive.After the loop canbuy is checked to see if its empty if true -1 is printed if not empty the maximum amount of the list is printed. 

### grading students
- [question](https://www.hackerrank.com/challenges/grading/problem)
- [solution](./solutions/implementation/grading_students.py)

  ### Explanation:
  >The function takes grades which is a list of marks.A list mutliples is intialized with multiples of 5 starting from 40 to 100.The list is looped through if the mark is less than 38 its passed as its shouldnt be rounded else its checked with each number in the multiples and if the number and mark difference is less than 3 mark is changed to the number after the loop the the rounded of marks is returned.

### number line jumps
- [question](https://www.hackerrank.com/challenges/kangaroo/problem)
- [solution](./solutions/implementation/number_line_jumps.py)

  ### Explanation:
   >The function takes 4 arguments x1 ,x2 which is start locations of kangaroo 1 and 2 ,v1 and v2 which is jump limit of the kangaroo 1 and 2.A for loop is intialized with range of 10000 assuming that they will make that many jumps each time the v1 and v2 are added to x1 and x2 to get thier current position if x1 and x2 matches in any jump the passed flag is set to true and the loop is exited else the flag is set to flase.After the loop flag is checked if its true YES is printed if its false NO is printed.
