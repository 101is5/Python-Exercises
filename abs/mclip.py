from sys import argv
from pyperclip import copy

d = {'agree':'Text for agree keyword','disagree':'Text for disagree keyword'}

if argv[1] in d:
    print(f'Text for {argv[1]} successfully copied to the clipboard')
    copy(d[argv[1]])


