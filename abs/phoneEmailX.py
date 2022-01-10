# this app takes what is in the clipboard and pastes only phones
# and emails if they're found

# LOGIC:
# analyze text(string)
# findall phones and emails
# for i in findall list
# try a regex that matches US and BR phone number patterns

# The problem with this approach was that, by not grouping anything and making 
# all spaces, hyphens and parentheses optional, I ended up with the sum of all
# possible amounts of numbers. So '123456789123456789' would be a match.
# By the way, the sum was 17, so it would match up to 17 digits, but the example
# above (1 through 9 twice, so length 18) did match. Why?
# Also, finditer() only required a few more characters of code.
    # DEPRECATED:
    # I will avoid subgrouping because I want to use findall() instead of finditer():
    # findall() outputs a list of matchings right away
    # finditer() will require aditional looping to gather the matchings:
    #   for i in matchings:
    #       print(i.group())

from pyperclip import copy, paste
from re import I,VERBOSE,DOTALL,compile,findall

text = paste()

phoneRe = compile(r'''

    # Obs.: COnsidering phone numbers without spaces in between digits as in '+155577778888',
    # it seems impossible to avoid something like '1234567890', when there's no country code
    # to match.
    # With that in mind, it's probably best to hardcode, not considering too many 
    # variations or typos.
    
    # country code: 
    (
    \+          # country code plus sign
    (\d{1,2}-)? # 1 to 2 digits: country code prefix, as in 1-264, 44-1624
    \d{1,3}     # 1 to 3 digits
    [\s-]*      # if spaces and/or hiphen and/or spaces
    )?

    # area code (state)
    (
    \(?         # if opening parentheses
    \d{1,3}     # none to 3 digits
    \)?
    [\s-]*      # 
    )?
    
    # phone number
    \d?         # if single digit (as in a brazilian number like '9 8765 4321')
    [\s-]*      # if spaces and/or hiphen and/or spaces
    \d{3,5}     # 3 to 5 digits
    [\s-]*      # if spaces and/or hiphen and/or spaces
    \d{4}       # 4 digits
    
    ''',VERBOSE)
emailRe = compile(r'[\w-]+@[\w-]+\.[\w]+\.?[\w]*')
webSiteRe = compile(r'https?://\w[\w.]+')
# dateRe = compile() # matches and formats dates
# typoRe = compile()  
# typoRe matches: 
# multiple spaces between words, 
# multiple exclamation marks and,
# repeated words.


phones = phoneRe.finditer(text)
emails = emailRe.finditer(text)
websites = webSiteRe.finditer(text)
# dates = dateRe.finditer(text)
# typos = typoRe.finditer(text)

print("Phone numbers: ")
for i in phones:
    print(i.group())
print()

print("Emails: ")
for i in emails:
    print(i.group())
print()

print("Websites: ")
for i in websites:
    print(i.group())
print()

# print("Dates: ")
# for i in dates:
#     print(i.group())
# print()