# Automate the Boring Stuff With Python
# RegExs Chapter Brief Notes

import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
myPattern = r'\d{3}-\d{3}-\d{4}'
compPattern = re.compile(myPattern) # (compPattern is a "re.Pattern" object)

# you can use re methods with this syntax
# (works with either raw string or compiled pattern):
re.search(myPattern,message)
re.findall(myPattern,message)

# or, this (works ONLY with a compiled pattern):
compPattern.findall(message)
compPattern.search(message)

# ***GROUPING***:
# ===============
# for grouping regexes you use ().
# OBS.: what is left oustide () doesn't become a group
# E.g.:
# (using escape characters '\(' and '\)' )
msg = 'Call me at (415) 555-1011 tomorrow.'
cP = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
x = cP.search(msg) # x is a re.Match object, which has attributes such as 'group()' and 'groups()'
x.group()
# >>> x.group() 
# '(415) 555-1011'
# >>> x.group(0) 
# '(415) 555-1011'
# >>> x.group(1) 
# '(415)'
# >>> x.group(2) 
# '555-1011'
# >>> x.groups()  
# ('(415)', '555-1011')

# If part of the pattern wasn't grouped inside (), e.g. cP = re.compile(r'(\(\d{3}\)) \d{3}-\d{4}'),
# i.e. the '555-1011' part, there wouldn't be a group of index 2 and value '555-1011'

    # ***THE QUESTION MARK***
    # =======================
    # A '?' after a group makes it optional.
    # E.g.: 
    # >>> rgx = re.compile(r'(\d{3}-)?\d{3}-\d{4})
    # the group (\d{3}-) is optional, i.e. a number like '555-1011' would also be detected.

    # ***THE PIPE***:
    # ===============
    # The pipe ('|') allows multiple matching options, e.g.:
    # >>> s = re.search(r'tomor|row|rough|rock|rules',message)
    # >>> s.group()
    # >>> 'tomor'
    # If you group the options, it connects the outer word with each option and searches for them:
    # >>> s = re.search(r'tomor(row|rough|rock|rules',message))
    # >>> s.group()
    # >>> 'tomorrow'
    # >>> s.groups()
    # >>> ('row',) --> only 'row' was in between (), hence grouped.

    # ***THE DOT ('Wild card')***
    # ===========================
    # Matches anything except newline characters(\n)
    # E.g.: r'.at' matches any 3 letter word ending with 'at'
    # Notice the dot followed by the star means 'anything as many times it occurs'

    # ***THE STAR***
    # ==============
    # Same as the pipe but also considering multiple occurances;
    # Match the pattern whether it occurs (regardless of amount) or not;
    # It is an alias for the braces with no values ({ , }), 
    # and like the braces themselves, a '?' next to it makes it non-greedy;

    # E.g.: 
    # r'<.*>' checks the whole string, as if prioritizing '.*', whilst
    # r'<.*?>' stops at the first '>', as if prioritizing the enclosing characters.

    # Instead of specifying the number of times, say {2}, {3}, {15}..., use *
    # >>> batRegex = re.compile(r'Bat(wo)*man')
    # >>> mo1 = batRegex.search('The Adventures of Batman')
    # >>> mo1.group()
    # >>> None

    # >>> mo2 = batRegex.search('The Adventures of Batwoman')
    # >>> mo2.group()
    # >>> 'Batwoman'

    # Here 'wo' appears 4 times, so a regex of "r'Bat(wo){4}man" would also work
    # >>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
    # >>> mo3.group()
    # >>> 'Batwowowowoman'

    # ***THE PLUS***
    # ==============
    # Same as star, but requires the group to exist at least once in the string.

    # ***THE CURLY BRACES WITH NUMBERS INSIDE***
    # ==========================================
    # These match the amount(s) defined inside curly braces, 
    # placed right after a character or a group.
    # {2} --> single number, matches exactly this amount
    # {2,4} --> matches as long as inside this range
    #       --> matches the longest string possible (Greedy)
    # {2,4}? --> same as above, but matches the shortest string (Non-greedy)
    # {,10} --> from 0 to max
    # {10,} --> from min to infinity
    # A star(*) would be the same as { , } and a plus(+) the same as {1, }

    # ***THE CARET(or \A) AND THE DOLLAR SIGN(or \Z)***
    # =================================================
    # ^ or \A - inside a group at the START of a regex matches only the start of a string.
    # E.g.: re.compile(r'^Hi, nice to meet you')
    # $ or \Z - inside a group at the END of a regex matche only the end of a string 
    # E.g.: re.compile(r'this evening$')


# ***findall() method***
# ======================
# Matches all occurances of the regex.
# If grouped: 
# - it returns a list containing each group inside a tuple;
# - this list contains ***ONLY*** the grouped parts: whatever is not grouped 
# doesn't go in the list

# ***THE SQUARE BRACKETS***
# =========================
# Define classes, thus allowing making custom classes;
# The caret(^) at the beginning negate the options;
# The hyphen(-) in between characters define a range;
# Don't require escaping characters.
# The way a class works is that it compares one character to the possibilities
# defined inside the square brackets. That way, in order to apply a class 
# comparison to many characters, you'll have to attach *, +, or {n} to it
# E.g.: 
# [a-z], range from a to z;
# [^12f-i], not (1|2|f|g|h|i)
# [5c-f], 5(c|d|e|f);
# [1-9], range from 1 to 9;
# [1-37-9], ranges from 1 to 3 AND from 7 to 9;
# [aeiouAEIOU.], (a|e|i|o|u|A|E|I|O|U|\.)

# ==============================
# The different roles of ? and ^
# ==============================
# ?
# - When next to a group, makes it optional
# - When next to curly braces, makes it 'non-greedy'
# ^
# - When at the start of a regex, matches only the start of a string
# - When in square brackets, negates the options

# ***THE METHODS: re.IGNORECASE(), re.VERBOSE(), re.DOTALL()***
# =============================================================
# IGNORECASE, or just I, as the name suggests, ignores letter cases;
# VERBOSE allows multiline regex definition, thus also allowing comments;
# DOTALL makes the dot also match newline characters.
    # OBS.: the compile() method takes only two arguments, so in order to
    # use more than one of the methods above, the trick is to use the pipe,
    # since it's the bitwise operator for "OR", as in:
    # re.compile(r'regex string', re.I | re.VERBOSE | re.DOTALL)

