# characterCount is supposed to count all types of characters
# This is a 'letterCount' version

# Lower the sentence so a letter is checked just once;
# Loop over the lowered sentence to check its characters;
    # dimiss non-alphabetical charaters 
    # Count instances of a letter;
    # Generate pair 'letter:amount of instances';
    # Insert pair in dictionary;
    # After checking a character remove all instances of it
    # from the string, to avoid double checking;
        # string method remove();
            # this method has a 'count' parameter which won't be used
            # since we want all instances of a character removed
    # Rebuild string;
# Loop until string is out of letters;

# Obs 1.: setdefault(), which is the method suggested by the book
#       outputs the value of each key, which here is uncalled for.
#       Best not to use it here.

# Obs 2.: A Python loop follows the original version of an iterable.
#       This means that altering an iterable whilst looping over it
#       will not change the instance's indexes that are being looped 
#       over. So e.g. changing the length of a string inside a loop 
#       might as well get confusing because the loop will still iterate 
#       through the unaltered version of that string.

sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
d = {}

for i in sentence:
    if i.isalpha():
        d[i.lower()] = sentence.count(i.lower())
        # d.setdefault(i,sentence.count(i))

final = dict(sorted(d.items()))

# A more didatic approach:
lowered = sentence.lower()

for i in lowered:
    if i.isalpha():
        count = sentence.count(i)
        d[i] = count

sorted_dict = sorted(d.items())
final = dict(sorted_dict)