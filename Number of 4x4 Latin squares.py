from itertools import permutations

def check_valid_grid(grid):
    # Check if each column is invalid, if not then is valid
    for col in range(4):
        column = []
        for row in range(4):
            column.append(grid[row][col])
        if len(set(column)) != 4: # set removes duplicates, so if length less than 4 means there is duplicate and therfore invalid grid
            return False
    return True

number_of_solutions = 0
all_permutations = list(permutations(range(1, 5)))  #lists all permutations of the numbers 1-4
for row1 in all_permutations:  #goes through each possible permutation of the 4 numbers in each row, inneficient but brute force to check absolute validity
    for row2 in all_permutations:
        for row3 in all_permutations:
            for row4 in all_permutations:
                grid = (row1, row2, row3, row4) # 
                if check_valid_grid(grid): 
                    number_of_solutions += 1 # counts each valid grid

print("Number of 4x4 Sudoku solutions: " + str(number_of_solutions))  #should result in 576