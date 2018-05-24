# Create a program that will take a text file that will have the keywords: ADJECTIVE, NOUN, ADVERB, or ADVERB
# The program must search for these words and replace them with words given by the user
# The text might contain multiple instances of the same keywords


def getMadLib(file, list):

    with open(file,'r') as f:
        for line in f:
            for word in line.split():
                list.append(word)
        return(list)
    file.close()


def fillInBlanks(madLib):
    # variable t used to keep track of location in the list
    t = 0

    # iterate for each word in the list
    for i in madLib:

        # convert the list item to a string for comparison and set up variables
        str(i)
        tempword = ""
        p = ""

        # check for punctuations before doing comparisons
        for char in i:
            if ',' == char or '.' == char:
                p = char
                break;
            tempword += char

        # if statements for keywords
        if tempword == 'NOUN':
            print("Please insert a NOUN: ")
            tempNoun = input()
            madLib[t] = tempNoun.lower()
        elif tempword == 'ADJECTIVE':
            print("Please insert a ADJECTIVE: ")
            tempADJ = input()
            madLib[t] = tempADJ.lower()
        elif tempword == 'VERB':
            print("Please insert a VERB: ")
            tempVerb = input()
            madLib[t] = tempVerb.lower()
        elif tempword == 'ADVERB':
            print("Please insert a ADVERB: ")
            tempADV = input()
            madLib[t] = tempADV.lower()

        # if there was a punctuation for this word, add it to the end of it
        madLib[t] += p

        # iterate to next location in list
        t += 1

    print(' '.join(madLib))

print('Please input the mad lib file.')
madLibInput = input()
madLibSentence = []
madLibSentence = getMadLib(madLibInput, madLibSentence)
fillInBlanks(madLibSentence)
