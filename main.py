import numpy as np
import time

np.set_printoptions(threshold=np.inf)

rows,columns = 10, 10

grid = np.zeros((rows, columns))

#fuego semilla
grid[1,1] = 1

def start_simulation(map:np.ndarray):
    if (map.all()):
        return
    
    rows_on_fire, columns_on_fire = np.where(map == 1)
    for fire_index_row, fire_index_column in zip(rows_on_fire, columns_on_fire):
        #TODO CUIDADO CON EL HECHO DE QUE EL INDICE NO EXISTA
        #grid[fire_index_row + 0, fire_index_column + 1] = 1
        #grid[fire_index_row + 0, fire_index_column - 1] = 1
        #grid[fire_index_row + 1, fire_index_column + 0] = 1
        #grid[fire_index_row + 1, fire_index_column + 1] = 1
        #grid[fire_index_row + 1, fire_index_column - 1] = 1
        #grid[fire_index_row - 1, fire_index_column + 0] = 1
        #grid[fire_index_row - 1, fire_index_column + 1] = 1
        #grid[fire_index_row - 1, fire_index_column - 1] = 1
        
        for i in range(1,9):
            #las veces que toca sumar 0 al indice de la columna es multiplo de 3
            plus_in_column = 0 if i % 3 == 0 else 1
            #si es menor que dos significa que estamos en la fila del fuego semilla y no debemos cambiar de fila
            if (i <= 2):
                grid[fire_index_row, fire_index_column + plus_in_column] = 1
                continue
            plus_in_row = 1 if i <= 5 else -1
            grid(fire_index_row + plus_in_row, fire_index_column + plus_in_column)
            
            
        
        print(f"ROW:{fire_index_row} ",f"COLUMN{fire_index_column}")


    print(grid)
    start_simulation(grid)
        
    
start_simulation(grid)