import numpy as np
import time
from scipy.signal import convolve2d

inicio = time.time()
rows, columns = 10, 10
grid = np.zeros((rows, columns))

grid[0, 0] = 1  # fuego semilla inicial

base_probability = 0.1
wind_force = 1 # si la extension del fuego esta alineada con la direccion del viento, entonces, habra un 100% de que se encienda ese fuego
wind_vector = np.array([5,0]) 
normalized_wind_vector = wind_vector / np.linalg.norm(wind_vector) #solo hallamos la direccion del viento, que es lo que nos importa


#TODO: Falta aplicar la fuerza del viento, actualmente solo hay una "probabilidad base"
def start_simulation(initial_grid):
    new_grid = initial_grid
    #Indica que celdas tomar en cuenta por la convolución
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    
    while not new_grid.all():
        neighbors = convolve2d(new_grid, kernel, mode='same', boundary='fill')
        random_array = np.random.random(new_grid.shape)
        # Si esta incendiadada: que se mantenga incendiada
        # Si esta apagada: La probabilidad de que se encienda aumenta segun la cantidad de vecinos tenga a su alrededor.        
        new_grid_in_boolean = (new_grid == 1) | ((new_grid == 0) & ((1 - (1 - base_probability) ** neighbors) > random_array))
        new_grid = new_grid_in_boolean.astype(int)
    return new_grid

start_simulation(grid)


