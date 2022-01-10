# My take on pigLatin from "Automate the Boring Stuff"

# Obs.: watch the referencing: 'word' and 'firstLetter' sure 
# improve readability, but are different containers, i.e. in
# order to affect the contents of a list, its elements must be
# directly referenced to, as in the last line of this snippet:
#       word = strList[i]   
#       firstLetter = strList[i][0]
#       (...)
#       if firstLetter.isalpha():
#           for p in word:
#               if p in ['.',',',';']:
# Here ---------->  strList[i] = word.replace(p,'',1)

# Instead, word = word.replace(p,'',1) would change the content
# of 'word', not strList[i] 


def pigLatin(string):
    vowels = [65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121]
    consonants = [66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78,
    80, 81, 82, 83, 84, 86, 87, 88, 
    90, 91, 92, 93, 94, 95, 96, 98, 99, 
    100, 102, 103, 104, 106, 107, 108, 
    109, 110, 111, 112, 113, 114, 115, 
    116, 118, 119, 120, 122]

    strList = string.split()
    
    for i in range(len(strList)):
        punct = ''
        word = strList[i]
        firstLetter = strList[i][0]
        if len(word) > 1:
            secondLetter = strList[i][1]
            cluster = strList[i][0]+strList[i][1]
        if firstLetter.isalpha():
            for p in word:
                if p in ['.',',',';']:
                    strList[i] = word.replace(p,'',1)
                    punct += p
            if ord(firstLetter) in vowels:
                if firstLetter.isupper() and len(word) > 1:
                    strList[i] += 'YAY' + punct
                else:
                    strList[i] += 'yay' + punct
            elif ord(firstLetter) and ord(secondLetter) in consonants:
                if word.istitle():
                    strList[i] = (word.replace(cluster,'') + cluster+'ay'+ punct).title()
                elif word.isupper():
                    strList[i] = (word.replace(cluster,'') + cluster+'ay'+ punct).upper()
                else:
                    strList[i] = word.replace(cluster,'') + cluster+'ay'+ punct
            else:
                if word.istitle():
                    strList[i] = (word.replace(firstLetter,'') + firstLetter + 'ay'+ punct).title()
                elif word.isupper():
                    strList[i] = (strList[i].replace(firstLetter,'') + firstLetter + 'ay'+ punct).upper()
                else:
                    strList[i] = strList[i].replace(firstLetter,'') + firstLetter + 'ay'+ punct
    
    for i in strList:
        print(i,end=' ')

# Example:
pigLatin('My name is AL SWEIGART and I am 4,000 years old.')