items = {'sandwiches':'4','apples':'12','cups':'4','cookies':'8000'}

def picnicTable(d,lmargin,rmargin):
    print(' PICNIC TABLE '.center(lmargin+rmargin,'~'))
    for k,v in d.items():
        print(k.title().ljust(lmargin,'_')+v.rjust(rmargin,'_'))
    print()

# picnicTable(items,10,10)
# picnicTable(items,20,10)
# picnicTable(items,10,20)