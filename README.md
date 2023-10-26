# HackerRank_Solutions
>  The repository contains the solutions to HackerRank problems.Solutions have been done using python programming language.All the soltuions are grouped under their specific domain folders.

## appleandorange
- [solution](./solutions/implementation/apple_and_orange.py)

 ### Explanation:
>The function takes arguments s,t which are the start and end location of house.a,b which are the location of apple and orange tree respectively.It then intialize two variables applecount,orangecount to count the number of apple which feel inside the location of house.It the uses a for loop to iterate through the distance of apples in apples array.Each time distance of apple is added with location of apple tree and its then compared with location of house and sees if its greater than start location of house and less than end location of house if condition is true the applecount is incremented by 1.The same is done for location of orange in oranges array.After both loop have completed the applecount and orangecount are printed in seprate lines.

### billdivision
- [solution](./)

 ### Explanation:
 >The function takes three agruments bill which is the list of price of item, k is the index of item anna declined,b is amount brian calculated.A variable summed is intialized to store the amount anna has to pay.Bill list is looped through using index if the index matches with index of item that anna has not eaten its passed less the price is added to summed variable.after the for loop the summed is floor divided by 2 to divide the amount among anna and brain,its then compared with the amount brian has calculated if its same the Bon Appetit is printed if its greater then the difference between amount brian calculated and original amount anna has to pay is printed.

### breaking the records
- [solution](./)

### Explanation:
>The function takes a argument scores which is a list of scores.Objective is to find the noofbestscores and noofworstscores.First score is taken has bestscore a copy of it is created in a variable bestscore1.Bestscorecount and worstscorecount variable is intialzed.Worstscore is set to -1 as a flag to start the count of worstscore and intialize first worstscore.for loop is used to iterate thorugh the scores list.every score is compared with bestscore if the score is greater the bestscorescount is incremented by 1 and bestscore is set to current score.if score is not greater and worstscore is -1 the  score is comapred with firstbestscore if its lower than that worstscore it intialized with current score and worstscorecount is incremeneted by -1.In next iteration the second statement will not be checked and it goes to third statement where current score is comapred with the worstscore if its less then worstscorecount is incremeneted by 1 and worstscore is set to current score.After the for loop is list is created with the first element as bestscorecount and second element as worstscorecount and list is returned.

### cats and a mouse
- [solution](./)

  ### Explanation:
  >The function takes x which is location of cat A y which is the location of cat B and z which is the location of mouse C.It then compares the absolute differnence between the location of mouse and Cat A and location of mouse and Cat B.It compares absolute differnce to know the distance.If the distance of cat a is less than cat b Cat A is printed if cat b's distance is less than cat a's then Cat B is printed.If both cats distance is same the mouse is allowed to escape as per given in question and Mouse C is printed.


### counting valleys
-[solution](./)

  ### Explanation:
  >The function takes steps which is the number of step the hiker took and path is a string that containing U for up and D for down after one cycle of D and U its counted as hiker as gone to valley and returned to the plain.Variable valleys is declared to count no of valleys hiker went to and level variable is declared which is indicating the current postion of hiker and currently set to zero,in_valley variable is declared as a flag to know whether the hiker is has entered the valley.Each character in the path string is looped through and its compared with U if they are equal the level is incremeneted by 1 else its decremeneted by 1.if the level is less than 0 and and in_valley is set to false its set to true to know hiker has entered the valley the next statement checks whether the level is greater or equal to zero and in_valley is set to true then if both statment are true this indicates the hiker has traversed a valley and came back to plain so valleys is incrmeneted by 1 and flag is set to false.After the loop is completed the no of valleys traversed is returned.


 ### day of programmer
 -[solution](./)

 ### Explanation:
 >

