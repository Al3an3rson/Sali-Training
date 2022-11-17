from random import shuffle
import pandas
from numpy.random import seed

# Imports dictionary of alphabet in form of csv
# csv delimited by '~', uses python to parse, does not take quotes into account
df1 = pandas.read_csv("C:\\Users\\alex\\Dokumente\\VisualStudioCode\\Python\\CodeTeacher\\data.csv", sep = "~", engine='python', quoting=3)

# Establishes array of indexes to loop through csv
sequence = [i for i in range(len(df1.index))]
# Randomly shuffles the array
shuffle(sequence)

# Establishes variables and signals start of program
print("Begin!")
print("Please enter a character or \"quit\"")
print()

message = ""
index = 0


while(message != "quit" and index < len(sequence)):
    question = ""

    # Gets code of a letter from data.csv
    # Copies code into question with more readable format
    for i in str(df1.iloc[sequence[index], 0]):
        question = question + i
        question = question + "  "

    # Displays code of char
    print(question)

    # Asks user for what they think code means
    message = input("This letter is: ")

    # Reveals char the code was pointing to and if user was correct
    if(message == df1.iloc[sequence[index], 1]):
        print("Correct! Answer is: ", end = "")
        print(df1.iloc[sequence[index], 1])
    else:
        print("Wrong! Answer is: ", end = "")
        print(df1.iloc[sequence[index], 1])
    
    # Increases index to move sequence onto next character
    index = index + 1

    print()

print("Thank you for training!")