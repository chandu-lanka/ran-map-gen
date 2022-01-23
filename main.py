'''
Made By H. C. Lanka

.........

Hello! This is my own implementation of map generation

.........

I'm going to be using Python v3.8.7 for this project... but any version above 3.6.x is perfect
for this implementation
'''

import sys
import pygame
import time
import random
from itertools import product
import data.colors as colors

fps = 60
cell_width = 5
grid_size = width, height = (100, 50)
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
        
        return new_board

prev_update_time = time.time()
board = make_board(width, height, randomize=True)
paused = True
mouse_dragging = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                paused = not paused
            if event.key == pygame.K_SPACE:
                board = make_board(width, height, randomize=True)
                colors.random_color = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col, row = x//cell_width, y//cell_width

            state = board[col][row]
            board[col][row] = 1
            mouse_dragging = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_dragging = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if mouse_dragging:
        x, y = pygame.mouse.get_pos()
        col, row = x//cell_width, y//cell_width
        board[col][row] = 1

    if time.time() - prev_update_time < 1/fps:
        continue

    prev_update_time = time.time()
    screen.fill(colors.black)

    for x, y in product(range(width), range(height)):
        coords = ((x+0.5)*cell_width, (y+0.5)*cell_width)

        if board[x][y]:
            pygame.draw.circle(screen, colors.random_color, coords, cell_width/2)
    pygame.display.flip()