from pyperclip import copy, paste

# Text must be copied to the clipboard before running this program
text = paste()
bulletText = ''
if text:
    textList = text.split('\r\n')
    for line in textList:
        bulletText += '• '+line+'\r\n'

    copy(bulletText)
    print('Text successfully bullet-formatted')

    print("Show text? ('yes' or 'no')")
    answer = input()
    while answer not in ['yes','no']:
        print("'Answer either 'yes' or 'no'")
        answer = input()
    if answer == 'yes':
        print(bulletText)
else:
    print('Nothing in the clipboard')