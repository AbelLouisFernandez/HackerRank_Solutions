# HackerRank_Solutions
Solutions have been done using python programming language.
All the solutions contain code given  
~~~
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
~~~
This code is used to run the our code automatically when the script is ran.It also opens a file to write the output to ,take inputs in this case it takes input and convert it to array in some cases 
its kept as a string or integer and calls the function where we have defined solution and pass the arguments.Solution have been explained using comments inside the programs.Each solution has question name as filename and question link is also provided as comment.Soltuions have categorised into seprate folder using the name of their subdomains.
