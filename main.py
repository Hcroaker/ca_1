import sys

def isValidForSequence(s1, s2):
    """
    This module is used to check if s2 is a validate candiate for adding it to the current sequence.

    It checks if s2 (a new string) can be sequenced with s1 (a previous string)
    """

    print(s1, s2)

def findHighestSequence(file, wordLength):
    print("Hey")

def __init__():
    """Inital function

    This module does the intialization of the program.
    This includes:
        - Opening a file
        - Reading a word length as an integer
        - Calling various functions to find a solution
        - Printing the Output
    """

    #This try and expect block ensures that the input is valid and all the code executes without causing a fatal crash.
    try:

        file = open("dictionary.txt", "r")

        #Get the word length from the command line args
        wordLength = int(sys.argv[1])

        #Ensure that input is between 4 and 15.
        if(not(wordLength <=15 and wordLength >=4)):
            raise ValueError("You must input an integer between 4 and 15 inclusive.")

        #Seach through each line and calculate the highest sequence
        for line in file:
            print(len(line))
            
    except ValueError as err:
        print("Sorry,", err.args[0])





    file.close();

__init__()
