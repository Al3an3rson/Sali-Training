from random import shuffle
import pandas

# Imports dictionary of alphabet in form of csv from Alex's Github website or local csv
# csv delimited by '~', uses python to parse, does not take quotes into account
# df1 = pandas.read_csv("https://raw.githubusercontent.com/Al3an3rson/Sali-Training/main/SeptimalData.csv", sep = "~", engine = 'python', quoting = 3)
df1 = pandas.read_csv(
    "C:\\Users\\Alex\\Documents\\VisualStudioCode\\Python\\PyZeroWCode\\data.csv",
    sep="~",
    engine="python",
    quoting=3,
)


# Allows user to choose which characters they want to learn
question = input(
    "Would you like to train the alphabet, integers, symbols, or all?: "
).lower()

boo = False

while boo == False:
    # Defines boolean to break while statement
    boo1 = False

    # Establishes array of indexes to loop through csv
    # Depending on user input, either only gets indexes for certain groups of characters or for all of them
    while boo1 == False:
        if question == "alphabet":
            question1 = input('Which level (1-9) or "all"?: ').lower()
            if question1 == "1":
                sequence = [4, 19, 0]
                boo1 = True
            if question1 == "2":
                sequence = [14, 8, 13]
                boo1 = True
            if question1 == "3":
                sequence = [18, 17, 7]
                boo1 = True
            if question1 == "4":
                sequence = [3, 11, 20]
                boo1 = True
            if question1 == "5":
                sequence = [2, 12, 5]
                boo1 = True
            if question1 == "6":
                sequence = [24, 22, 6]
                boo1 = True
            if question1 == "7":
                sequence = [15, 1, 21]
                boo1 = True
            if question1 == "8":
                sequence = [10, 23, 16]
                boo1 = True
            if question1 == "9":
                sequence = [9, 25]
                boo1 = True
            if question1 == "all":
                sequence = [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                ]
                boo1 = True
        elif question == "integers":
            question1 = input("Which level (1-3)?: ").lower()
            if question1 == "1":
                sequence = [26, 27, 28, 29]
                boo1 = True
            if question1 == "2":
                sequence = [30, 31, 32]
                boo1 = True
            if question1 == "3":
                sequence = [33, 34, 35]
                boo1 = True
        elif question == "symbols":
            question1 = input("Which level (1-5)?: ").lower()
            if question1 == "1":
                sequence = [36, 37, 38, 39]
                boo1 = True
            if question1 == "2":
                sequence = [40, 41, 42]
                boo1 = True
            if question1 == "3":
                sequence = [43, 44, 45]
                boo1 = True
            if question1 == "4":
                sequence = [46, 47, 48]
                boo1 = True
            if question1 == "5":
                sequence = [49, 50, 51]
                boo1 = True
        elif question == "all":
            sequence = [i for i in range(len(df1.index))]
            boo1 = True
        else:
            print('Please enter "alphabet", "integers", "symbols", or "all"')
            question = input(
                "Would you like to train the alphabet, integers, symbols, or all?: "
            ).lower()

    # Randomly shuffles the array
    shuffle(sequence)

    # Establishes variables and signals start of program
    print("Begin!")
    print('Please enter a character or "quit"')
    print()

    message = ""
    index = 0

    while message != "quit" and index < len(sequence):
        frage = ""

        # Gets code of a letter from data.csv
        # Copies code into question with more readable format
        for i in str(df1.iloc[sequence[index], 0]):
            frage = frage + i
            frage = frage + "  "

        # Displays code of char
        print(frage)

        # Asks user for what they think code means
        message = input("This letter is: ").lower()

        # Reveals char the code was pointing to and if user was correct
        if message == df1.iloc[sequence[index], 1]:
            print("Correct! Answer is: ", end="")
            print(df1.iloc[sequence[index], 1])
        else:
            print("Wrong! Answer is: ", end="")
            print(df1.iloc[sequence[index], 1])

        # Increases index to move sequence onto next character
        index = index + 1

        print()

    print("Thank you for training!")
    check = input("Would you like to train again (y/n) or repeat?: ").lower()
    boo2 = False

    while boo2 == False:
        if check == "n":
            boo = True
            boo2 = True
        elif check == "y":
            boo = False
            boo2 = True
            question = ""
            question1 = ""
        elif check == "repeat":
            boo = False
            boo2 = True
        else:
            print('Please enter y/n or "repeat"')
            check = input("Would you like to train again (y/n)?: ").lower()


print("Thank you for playing!")
