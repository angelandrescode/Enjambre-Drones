import numpy as np
import time


inicio = time.time()
rows, columns = 200, 200
grid = np.zeros((rows, columns))

grid[0, 0] = 1  # fuego semilla inicial

base_probability = 0.2
wind_force = 1 # si la extension del fuego esta alineada con la direccion del viento, entonces, habra un 100% de que se encienda ese fuego
wind_vector = np.array([5,0]) 
normalized_wind_vector = wind_vector / np.linalg.norm(wind_vector) #solo hallamos la direccion del viento, que es lo que nos importa

def start_simulation(grid):
    while not grid.all():
        rows_on_fire, columns_on_fire = np.where(grid == 1)
        #Estos son los numeros que se tiene que sumar al indice del fuego semilla de un nuevo "vecindario"
        pattern_row = [0, 0, 1, 1, 1, -1, -1, -1]
        pattern_column = [1, -1, 0, 1, -1, 0, 1, -1]
        news = []
        
        for fire_row, fire_col in zip(rows_on_fire, columns_on_fire):
            #Aqui ocurre la expansión
            for i in range(8):
                new_row = fire_row + pattern_row[i]
                new_col = fire_col + pattern_column[i]
                #el vector de expansion es un vector de direccion que indica, hacia donde se expande el fuego
                vector_expansion = np.array([pattern_row[i], pattern_column[i]])
                norm_vector_expansion = vector_expansion / np.linalg.norm(vector_expansion)
                #obtenemos el factor multiplicador del viento
                similarity_to_wind_direction = np.dot(normalized_wind_vector, norm_vector_expansion)
                
                #chequeo de limites de índice
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= columns:
                    continue
                #si ya esta en llamas, ya no cambiar el estado
                if grid[new_row, new_col] == 1:
                    continue
                # si la expansion del fuego es favorecida por el viento (hay similitud), las probabilidades aumentan, si no, no reducen, se quedan en base_probability
                if np.random.random() < min(base_probability + (1 - base_probability) * wind_force * similarity_to_wind_direction, 1.0):
                    news.append((new_row, new_col, similarity_to_wind_direction))

        #settear a 1 los que se incendian por la expansion.
        for r, c, sim in news:
            grid[r, c] = 1
            #print(grid)
            #print(f"NUEVA FILA: {r} | NUEVA COLUMNA: {c} SIMILITUD CON EL VIENTO: {sim}")
        
    return grid

start_simulation(grid)
print(f"Tiempo total: {time.time() - inicio:.2f}s")