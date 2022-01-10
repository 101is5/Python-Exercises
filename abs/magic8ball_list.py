from random import choice, randint

def getAnswer():
    
    answers = [
    'It is decidedly so',
    'Yes',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

    return choice(answers)
    # return answers[randint(0,len(answers)-1)]