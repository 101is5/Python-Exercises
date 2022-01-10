d = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def fgame(d):
    for k,v in d.items():
        print(f"{v} {k.title()}")