import sys
from random import randint
import random
from collections import deque
import math
from itertools import permutations
from itertools import combinations

def isValidForSequence(s1, s2):
    """
    This module is used to check if s2 is a validate candiate for adding it to the current sequence.

    It checks if s2 (a new string) can be sequenced with s1 (a previous string)
    """

    print(s1, s2)

def findNextWordRecurse(currentWord, dict):
    """
    This module finds the next word that is valid for a sequence
    """
    # print("Find next word")
    # print(currentWord)
    nextKey = currentWord[-3:-1]
    if(nextKey not in dict):
        print("Recursive case")
        newWord = dict[nextKey].popleft()
        nextWord = findNextWordRecurse(newWord, dict)
        if nextWord is not None:
                return nextWord
    else:
        print("Base Case")
        return currentWord


def findNextWordNorm(currentWord, dict):
    """
    This module finds the next word that is valid for a sequence
    """
    # print("Find next word")
    # print(currentWord)
    nextKey = currentWord[-3:-1]
    # print(dict.keys())
    if(nextKey in dict):
        try:
            nextWord = dict[nextKey].popleft()
            return nextWord
        except:
            print("No more")
            return None
    else:
        print("No key")
        return None

def findHighestSequence(dict):

    sequence = []
    sequenceLength = 0

    #Choose a random starting key
    startingKey = random.choice(list(dict))
    # print(startingKey)

    #Get the starting word and add it to the sequence
    startingWord = dict[startingKey].popleft()
    sequence.append(startingWord)

    nextWord = findNextWordRecurse(startingWord, dict);
    print("Hey next word")
    print(nextWord)
    sequence.append(nextWord)

    while(nextWord):
        nextWord = findNextWordRecurse(nextWord,dict)
        sequence.append(nextWord)
        sequenceLength += 1;

    print(sequence)
    print(sequenceLength)

def findHighestSequence2(dict):
    sequence = []
    sequenceLength = 0
    biggestSequenceLength = 0;
    biggestSequence = []

    for key, value in dict.items():

        dictCpy = dict.copy()
        currentKey = key

        while 1:

            # print(keys1)
            # print(keys2)

            #Get the intersection of the base dictionary and the nested dict
            if dictCpy and dictCpy.get(currentKey):
                keys1 = set(dictCpy.keys())
                keys2 = set(dictCpy.get(currentKey).keys())
            else:
                break;

            potentialKeys = list(keys1.intersection(keys2))
            print("Potential Keys", potentialKeys)

            if potentialKeys:
                keyPicked = potentialKeys[0];
                # print(dictCpy[currentKey][keyPicked])
                # print(keyPicked)
            else:
                break;

            #For each key, try each word




            #Check if value len is not equal to 0, popleft() if popping makes it go to zero, then clear
            words = dictCpy[currentKey][keyPicked];
            if(words):
                newWord = str(words.pop())

                #Check if that made the words length 0
                if(not words):
                    # print("Delete")
                    del dictCpy[currentKey][keyPicked]

                    #Check if that reduced the size of the sub dictionary to 0
                    if(not dictCpy[currentKey].keys()):
                        del dictCpy[currentKey]

            else:
                print("Words length 0, something went wrong!")

            currentKey = keyPicked

            #Add to sequence
            sequence.append(newWord)
            sequenceLength += 1

        print(sequence)
        print(sequenceLength)

        if(sequenceLength>biggestSequenceLength):
            biggestSequenceLength = sequenceLength
            biggestSequence = sequence

        sequence = []
        sequenceLength = 0

    print(biggestSequence)
    print(biggestSequenceLength)

def recursiveFuntion(seq,words):
    if(len(words)==0):
        return seq
    else:
        for word in words:
            seq.append(words.pop())
            recursiveFuntion(seq,words)
            return seq
            #for each word,
def checkSolution(solution):
    count = 0;
    highestCount = 0
    for i in range(1,len(solution)-1):
        if(solution[i][1:3]==solution[i-1][-3:-1]):
            print("valid")
            count += 1
        else:
            print("invalid")
            count = 0
        if(count>highestCount):
            highestCount = count
    print(highestCount)

# def findBook(string book, point coords):
#
#     if (shelves.shelfAt(coords).contains(book)):
#         return true;
#     else:
#
#         while (shelves.hasExit()):
#
#             # nextExit returns the coordinates of where the next exit
#             # leads to and marks that exit as used up
#             if (findBook(book, shelves.nextExit())):
#                 // found it!
#                 return true;
#
#     # ran out of places to go.  this is a dead end.
#     return false;

def findHighestSequence3(dict):
    sequence = []
    sequenceLength = 0
    biggestSequenceLength = 0;
    biggestSequence = []

    for key, value in dict.items():

        dictCpy = dict.copy()
        currentKey = key

        print("Current Key ", currentKey)

        for nestedKey in dictCpy[currentKey]:

            print("Nested Key ", nestedKey)

            for word in dictCpy[currentKey][nestedKey]:

                #Find the sequence
                print(word)

def myprint(d):
  for k, v in d.items():

    if isinstance(v, dict):
      print("Outer", k)
      myprint(v)
    else:
      print("{0} : {1}".format(k, v))

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
        words = file.read().split()

        #Get the word length from the command line args
        wordLength = int(sys.argv[1])

        #Ensure that input is between 4 and 15.
        if(not(wordLength <=15 and wordLength >=4)):
            raise ValueError("You must input an integer between 4 and 15 inclusive.")

        newWords = []

        for i in range(len(words)):
            if(len(words[i])==wordLength):
                newWords.append(words[i])

        print(len(newWords))

        #Create empty dictionary
        dict = {}
        dictLength = 0;

        #For each word check if its startKey (2nd and third letters of the word) for that word exists,
        # - If it does then check if the words endKey exists in the value (2ND DICT), if it does then add it to that values deque. If if it doesn't then add a new entry to 2ND Dict (key = word[-3:-1], value = deque([word])).
        # - If it doesn't then add a new entry to 1St DICT (key=word[1:3], value = {key=word[-3:-1], value= deque([word])})
        for i in range(len(newWords)):

            word = str(newWords[i])
            key = str(word)[1:3]
            key2 = str(word)[-3:-1]

            if(key in dict):
                if(key2 in dict[key]):
                    dict[key][key2].append(str(word))
                else:
                    dict[key][key2] = [str(word)]
            else:
                dict[key] = {key2: [str(word)]}

        # print(str(dict))
        # findHighestSequence3(dict)
        # print(dict)

        # l = dict.items()
        # print(l)
        # for k,v in l:
        #     print(k)
        #     for i,x in v:
        #         print(x)

        myprint(dict)
    except ValueError as err:
        print("Sorry,", err.args[0])





    file.close();

__init__()
