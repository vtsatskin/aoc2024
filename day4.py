import re
from typing import List, Literal, Tuple, Union


def parse_input(file_path) -> List[str]:
    with open(file_path, 'r') as file:
        contents = file.read()
        return contents.splitlines()

# An incorrect solution where I misunderstood the problem as looking for a chain
# of "xmas" where each subsequent letter can be in any direction.
def search(grid: List[str], terms: str, i: int, j: int) -> int:
    if i < 0 or i >= len(grid[0]) or j < 0 or j >= len(grid):
        return 0
    
    if len(terms) == 0:
        return 0
    
    c = terms[0]
    if grid[j][i] != c:
        return 0
    elif grid[j][i] == c and len(terms) == 1:
        return 1
    
    terms_next = terms[1:]
    return sum([
        search(grid, terms_next, i-1, j-1),
        search(grid, terms_next, i, j-1),
        search(grid, terms_next, i+1, j-1),
        search(grid, terms_next, i-1, j),
        search(grid, terms_next, i+1, j),
        search(grid, terms_next, i-1, j+1),
        search(grid, terms_next, i, j+1),
        search(grid, terms_next, i+1, j+1),
    ])

def search_line(grid: List[str], i: int, j: int) -> int:
    if i < 0 or i >= len(grid[0]) or j < 0 or j >= len(grid):
        return 0

    clear_left = i >= 3
    clear_right = i <= len(grid[0]) - 4
    clear_up = j >= 3
    clear_down = j <= len(grid) - 4
    
    idx_path = []

    if clear_right:
        idx_path.append([[i, j], [i+1, j], [i+2, j], [i+3, j]]) # right
    if clear_left:
        idx_path.append([[i, j], [i-1, j], [i-2, j], [i-3, j]]) # left
    if clear_down:
        idx_path.append([[i, j], [i, j+1], [i, j+2], [i, j+3]]) # down
    if clear_up:
        idx_path.append([[i, j], [i, j-1], [i, j-2], [i, j-3]]) # up
    if clear_down and clear_right:
        idx_path.append([[i, j], [i+1, j+1], [i+2, j+2], [i+3, j+3]]) # down-right
    if clear_up and clear_right:
        idx_path.append([[i, j], [i+1, j-1], [i+2, j-2], [i+3, j-3]]) # up-right
    if clear_down and clear_left:
        idx_path.append([[i, j], [i-1, j+1], [i-2, j+2], [i-3, j+3]]) # down-left
    if clear_up and clear_left:
        idx_path.append([[i, j], [i-1, j-1], [i-2, j-2], [i-3, j-3]]) # up-left

    result = 0
    for path in idx_path:
        s = ''.join([grid[j][i] for (i, j) in path])
        if s == 'XMAS':
            result += 1
    return result

def search_x(grid: List[str], i: int, j: int) -> int:
    if i < 0 or i >= len(grid[0]) or j < 0 or j >= len(grid):
        return 0
    
    if i < 1 or i >= len(grid[0]) - 1 or j < 1 or j >= len(grid) - 1:
        return 0

    if grid[j][i] != 'A':
        return 0

    top_left = grid[j-1][i-1] == 'M' and grid[j+1][i+1] == 'S'
    top_right = grid[j-1][i+1] == 'M' and grid[j+1][i-1] == 'S'
    bottom_left = grid[j+1][i-1] == 'M' and grid[j-1][i+1] == 'S'
    bottom_right = grid[j+1][i+1] == 'M' and grid[j-1][i-1] == 'S'
    
    if (top_left or bottom_right) and (top_right or bottom_left):
        return 1
    else:
        return 0

    
        

def count_xmas(grid: List[str], func) -> int:
    result = 0
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            result += func(grid, i, j)
    return result

if __name__ == '__main__':
    grid = parse_input("./inputs/day4.txt")

    total = count_xmas(grid, search_line)    
    print("Total XMAS:", total)

    total2 = count_xmas(grid, search_x)    
    print("Total X-MAS:", total2)
