from typing import Type


chessDict = {}

# len(chessDict) <= 32

pieceNames = ['pawn','rook','knight','bishop','queen','king']
allPieces = []
table = []

# chess piece name generator
for i in pieceNames:
    allPieces.append(''.join(['w',i]))
    allPieces.append(''.join(['b',i]))

# chess piece position generator
chars = (chr(i) for i in range(97,105))
for i in chars:
    for j in range(1,9):
        str_j = str(j)
        position = ''.join([i,str_j])
        table.append(position)

# convoluted version
# for i in (chr(i) for i in range(97,105)):
#     for j in range(1,9):
#         table.append(''.join([i,str(j)]))

table

def isValidChessPosition(x):
    piece = ['pawn','rook','knight','bishop','queen','king']       
    pieces = ['wpawn', 'bpawn', 'wrook', 'brook', 'wknight',\
              'bknight', 'wbishop', 'bbishop', 'wqueen',\
              'bqueen','wking', 'bking']
    table = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',\
             'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',\
             'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',\
             'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',\
             'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',\
             'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',\
             'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',\
             'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
    invalidSyntax = "Invalid syntax."

    try:
        if len(x) > 32:
            print("Invalid position set: maximum number of pieces is 32")
            return None
        else:
            for k,v in x.items():
                if k not in pieces:
                    if k in table:
                        print(f"""{invalidSyntax}
                            The piece comes first. E.g.: 'brook':'h1')""")
                        return None
                    elif k in piece:
                        print(f"""{invalidSyntax} 
You must attach 'w' (for white) or 'b' (for black)
to the first letter of a piece's name. E.g.: 'brook : h1'""")
                        return None
                    else:
                        print('Invalid piece name.')
                        print('Valid piece names: ', end='')
                        for i in pieces:
                            print(i, end=', ')
                        return None

                elif v not in table:
                    if len(v) == 2 and v[0].isnumeric() and v[1].isalpha():
                        print(f"""{invalidSyntax} The letter comes first. E.g.: 'h1'""")
                        return None
                    elif v in pieces:
                        print("""Invalid syntax.
The position comes second. E.g.: 'wpawn':'a2')""")
                        return None
                    else:
                        print('Invalid position.')
                        print('Valid positions: ', end='')
                        for i in table:
                            print(i, end=', ')
                        return None
                
                else:
                    print('Valid')

    except:
        print("isValidChessPosition takes one dictionary as argument")
        return None