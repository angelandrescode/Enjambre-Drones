import numpy as np
import time

rows, columns = 10, 10
grid = np.zeros((rows, columns))
grid[0, 0] = 1  # fuego semilla

probabilidad_base = 0.1  # probabilidad para que el siguiente vecino se encienda

def start_simulation(grid):
    while not grid.all():
        rows_on_fire, columns_on_fire = np.where(grid == 1)
        pattern_row = [0, 0, 1, 1, 1, -1, -1, -1]
        pattern_column = [1, -1, 0, 1, -1, 0, 1, -1]
        nuevas = []
        
        for fire_row, fire_col in zip(rows_on_fire, columns_on_fire):
            for i in range(8):
                new_row = fire_row + pattern_row[i]
                new_col = fire_col + pattern_column[i]
                #chequeo de limites de índice
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= columns:
                    continue
                #si ya esta en llamas, ya no cambiar el estado
                if grid[new_row, new_col] == 1:
                    continue
                if np.random.random() < probabilidad_base:
                    nuevas.append((new_row, new_col))

        for r, c in nuevas:
            grid[r, c] = 1
        print(grid)
        
    return grid

start_simulation(grid)