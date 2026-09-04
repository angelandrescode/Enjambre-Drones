import numpy as np
import time
from scipy.signal import convolve2d


def build_directional_kernel(pattern_row, pattern_col):
    """Crea un kernel 3x3 con un solo 1 en la posición de la dirección dada."""
    kernel = np.zeros((3, 3))
    kernel[1 + pattern_row, 1 + pattern_col] = 1
    return kernel


def compute_wind_similarity(direction_y, direction_x, normalized_wind_vector):
    """Similitud coseno entre la dirección del vecino y la dirección del viento."""
    direction_vector = np.array([direction_y, direction_x])
    normalized_direction = direction_vector / np.linalg.norm(direction_vector)
    return np.dot(normalized_direction, normalized_wind_vector)


def compute_directional_data(pattern_row, pattern_column, normalized_wind_vector,
                              base_probability, wind_force):
    """
    Precalcula, para cada una de las 8 direcciones, su kernel y su probabilidad
    efectiva de encendido según el viento. Esto no depende del estado del grid,
    así que se calcula una sola vez y se reutiliza en cada timestep.
    """
    directions = []
    for i in range(8):
        kernel = build_directional_kernel(pattern_row[i], pattern_column[i])
        similarity = compute_wind_similarity(pattern_row[i], pattern_column[i], normalized_wind_vector)
        probability = np.clip(
            base_probability + (1 - base_probability) * wind_force * similarity,
            base_probability, 1.0
        )
        directions.append((kernel, probability))
    return directions


def calculate_prob_total(grid, directional_data):
    """Calcula la probabilidad efectiva de que cada celda se encienda segun la dirección del viento"""
    probability_maps = [
        convolve2d(grid, kernel, mode='same', boundary='fill') * probability
        for kernel, probability in directional_data
    ]
    
    return 1 - np.prod(1 - np.array(probability_maps), axis=0)

def propagate_step(grid, directional_data):
    """Ejecuta un timestep de propagación: calcula prob_total y enciende celdas nuevas."""
    prob_total = calculate_prob_total(grid, directional_data)
    random_array = np.random.random(grid.shape)
    success_mask = random_array < prob_total

    new_grid = grid.copy()
    new_grid[success_mask] = 1
    return new_grid


def run_simulation(initial_grid, normalized_wind_vector, base_probability, wind_force):
    pattern_row = [0, 0, 1, 1, 1, -1, -1, -1]
    pattern_column = [1, -1, 0, 1, -1, 0, 1, -1]

    directional_data = compute_directional_data(
        pattern_row, pattern_column, normalized_wind_vector, base_probability, wind_force
    )

    grid = initial_grid.copy()
    while not grid.all():
        grid = propagate_step(grid, directional_data)
    return grid


if __name__ == "__main__":
    grid = np.zeros((200, 200))
    grid[0, 0] = 1  # fuego semilla inicial

    wind_vector = np.array([-5, 0])
    normalized_wind_vector = wind_vector / np.linalg.norm(wind_vector)

    inicio = time.time()
    final_grid = run_simulation(grid, normalized_wind_vector, base_probability=0.1, wind_force=1)
    print(time.time() - inicio)
    
    
    