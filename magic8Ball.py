import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif  answerNumber == 4:
        return 'Reply haze try again'
    elif answerNumber == 5:
        return 'dick'
    elif answerNumber == 6:
        return 'fuck you'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
