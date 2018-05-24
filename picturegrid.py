
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# because we are basically rotating it we can just take the first col and print it as a row and
# repeat

# iterate in a range of the length of the first line
for j in range(len(grid[0])):
    # ex) we are at col 0 then we print out everything in this col
    for i in range(len(grid)):
        print(grid[i][j], end='')
    #once we finished printing out the col as a row we move on to the next col
    print()
