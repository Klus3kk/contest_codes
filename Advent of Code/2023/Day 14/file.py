import sys
import re
import collections
import math
from itertools import combinations
from functools import cache
import copy
import time

# Change for part 1/2
PART2 = False

f = open("input.txt").read().strip()
matrix = [[a for a in line]for line in f.split('\n')]

def find_new_slide_y_north(matrix, curr_y, x):
    
    for test_y in range(curr_y, 0-1, -1):
        if matrix[test_y-1][x] == 'O' or matrix[test_y-1][x] == '#':
            return test_y
    
    return 0

def slide_matrix_north(matrix):

    for y in range(1, len(matrix)):
        for x in range(0, len(matrix[0])):
            if (matrix[y][x] == 'O'):
                new_y = find_new_slide_y_north(matrix, y, x)
                if y != new_y:
                    matrix[y][x] = '.'
                    matrix[new_y][x] = 'O'
                    
    return matrix

def rotate_matrix_CW(matrix):
    
    height = len(matrix)
    length = len(matrix[0])
    new_matrix = []
    
    for x in range(0,length):
        line = [matrix[y][x] for y in range(0, height)]
        line.reverse()
        new_matrix.append(line)
    
    return new_matrix
        
# Challenge 1/2
result = 0

if not PART2:
    matrix = slide_matrix_north(matrix)

if PART2:
    old_matrixes = []
    
    for i in range(0, 1000000000):
        
        matrix = slide_matrix_north(matrix)
        matrix = rotate_matrix_CW(matrix)
        matrix = slide_matrix_north(matrix)
        matrix = rotate_matrix_CW(matrix)
        matrix = slide_matrix_north(matrix)
        matrix = rotate_matrix_CW(matrix)
        matrix = slide_matrix_north(matrix)
        matrix = rotate_matrix_CW(matrix)
        
        if not matrix in old_matrixes:
            old_matrixes.append(copy.deepcopy(matrix))
        else:
            # Found period
            break

    # Some math to find the equivelent i of 1000000000 in old_matrix using the period
    before_period = old_matrixes.index(matrix)
    period = i - before_period
    goal_i = 1000000000
    i_1000000000 = (goal_i - before_period) % period + before_period - 1
    matrix = old_matrixes[i_1000000000]

# Calculate result
for y in range(0, len(matrix)):
    for x in range(0, len(matrix[0])):
        if matrix[y][x] == 'O':
            result += len(matrix) - y

print("CH2: " if PART2 else "CH1: ",str(result))
#  109638   102657