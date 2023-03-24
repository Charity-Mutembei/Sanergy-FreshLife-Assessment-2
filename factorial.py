import sys
#imported sys so we can have exit commands at certain points of our
#code. sys.exit(1) == not successfull 

#step 1: define the function factorial, 
#takes in an integer 'n'
#then gives the factorial of 'n'

# return (n * factorial(n - 1))
#the function main(), then handles the interaction with the user of the command line
# #prompt the user to give an input as a positive integer
# #if they give a non-positive, raise the 'not successful' exit message
        #below is the message on a wrong input 
        # print("Error: input must be a positive integer (no less than 0)")
#if a success exit (0); then we can get the input and give results with the function factorial(n);
    #call the input with {n} and give the results with {results}
    #make the program executable with the code below
    # if __name__ = __main__:
    # main()

#  run the script using command - python factorial.py or python3 factorial.py

def factorial(n):
    if (n == 0):
        return (1)
    else:
        result = 1
        for i in range(1, (n + 1)):
            result *= i
        return (result)

def main():
    try:        
        n = int(input("Please Enter a positive integer (a number no less than 0):"))
        if (n < 0):
            raise ValueError
    except ValueError:
        print("Error: input must be a positive integer (no less than 0)")
        sys.exit(1)

    results = factorial(n)
    print(f"The factorial of {n} is {results}")

if __name__ == "__main__":
    main()