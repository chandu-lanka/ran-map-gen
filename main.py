'''
Made By H. C. Lanka

.........

Hello! This is my implementation of John Conways Game Of Life which is a cellular automaton
Cellular automaton means some sort of simulation based on certain rules

.........

I'm going to be using Python v3.8.7 for this project... but any version above 3.6.x is perfect
for this implementation
'''

import sys
import pygame
import time
import random
from itertools import product
import data.colors

fps = 60
cell_width = 3
grid_size = width, height = (500, 500)
screen_size = grid_size[0] * cell_width, grid_size[1] * cell_width

pygame.init()
screen = pygame.display.set_mode(screen_size)

def make_board(width, height, randomize=False):
    if randomize:
        new_board = [
            [random.choice([0, 1]) for y in range(height)]
            for x in range(width)
        ]
    else:
        new_board = [
            [0 for y in range(height)]
            for x in range(width)
        ]
    return new_board

def get_neighbors(x, y, board):
    neighbors = []
    for delta_x in [-1, 0, 1]:
        for delta_y in [-1, 0, 1]:
            nx = (x+delta_x) % width
            ny = (y+delta_y) % height
            neighbor = board[nx][ny]
            neighbors.append(neighbor)
    
    return neighbors

def advance(board):
    new_board = make_board(width, height)
    coords = product(range(width), range(height))
    for x, y in coords:
        neighbors = get_neighbors(x, y, board)
        alive_num = sum(neighbors)
        state = board[x][y]

        '''
        if living cell is alive and it has 2 or 3 
        neighbors, it stays alive
        '''
        
        if state == 1 and alive_num in [2, 3]:
            new_board[x][y] = 1

        '''
        if a cell is dead but has 3 neighbors, 
        it is alive again
        '''

        if state == 0 and alive_num in [3]:
            new_board[x][y] = 1
        
        return new_board