import numpy as np
import time
from scipy.signal import convolve2d

inicio = time.time()
rows, columns = 200, 200
grid = np.zeros((rows, columns))

grid[0, 0] = 1  # fuego semilla inicial

base_probability = 0.1
wind_force = 1 # si la extension del fuego esta alineada con la direccion del viento, entonces, habra un 100% de que se encienda ese fuego
wind_vector = np.array([-5,0]) 
normalized_wind_vector = wind_vector / np.linalg.norm(wind_vector) #solo hallamos la direccion del viento, que es lo que nos importa

def start_simulation(initial_grid):
    pattern_row = [0, 0, 1, 1, 1, -1, -1, -1]
    pattern_column = [1, -1, 0, 1, -1, 0, 1, -1]
    new_grid = initial_grid.copy()
    template_kernel = np.zeros((3, 3))
    array_of_convolutions = []
    while not new_grid.all():
        for i in range(8):
            template_kernel[1+pattern_row[i], 1+pattern_column[i]] = 1
            kernel_in_actual_direction = template_kernel.copy()
            
            neighbors = convolve2d(new_grid, kernel_in_actual_direction, mode='same', boundary='fill')
            vector_fire_expansion = np.array([pattern_row[i], pattern_column[i]])
            normalized_vector_fire_expansion = vector_fire_expansion / np.linalg.norm(vector_fire_expansion)
            similarity_to_wind_vector = np.dot(normalized_vector_fire_expansion, normalized_wind_vector)
            
            probability_to_get_burnt = np.clip(base_probability + (1 - base_probability) * wind_force * similarity_to_wind_vector, base_probability, 1.0)
            neighbors = neighbors * probability_to_get_burnt
            array_of_convolutions.append(neighbors)
            template_kernel[1+pattern_row[i], 1+pattern_column[i]] = 0
        
        prob_total = 1 - np.prod(1 - np.array(array_of_convolutions), axis=0)
        random_array = np.random.random(new_grid.shape)
        success_mask = random_array < prob_total
        new_grid[success_mask] = 1
        array_of_convolutions = []
            
            
            
            
            
            
start_simulation(grid)
print(time.time() - inicio)