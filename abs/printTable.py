# "Table Printer" from "Automate the Boring Stuff",
# modified to accept any inner list length.
# This program is supposed to print column by column, as in:
# tableData[0][0], tableData[1][0], tableData[2][0], 
# tableData[0][1], tableData[1][1], tableData[2][1], etc...


tableData = [['apples', 'oranges', 'cherries'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Define the number of lines
numberOfLines = len(tableData)
numberOfColumns = 0
columnLength = 0
# Define the lenght and number of columns.
#   The column's length is the longest word's length
for l in tableData:
    if len(l) > numberOfColumns:
        numberOfColumns = len(l)
    for w in l:
        if len(w) > columnLength:
            columnLength = len(w)

for column in range(numberOfColumns):
    for line in range(numberOfLines):
        try:
            print(tableData[line][column].rjust(columnLength), end='')
        except:
            print(' '*columnLength, end='')
    print()