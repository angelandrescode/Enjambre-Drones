import numpy as np
import main

def test_is_row_column_order():
    wind_vector = np.array([0,1])
    normalized_wind_vector = wind_vector / np.linalg.norm(wind_vector)
    similarity = main.compute_wind_similarity(0, 1, normalized_wind_vector)
    assert np.isclose(similarity, 1)

def test_prob_total_is_valid():
    def kernel_at(row, col):
        kernel = np.zeros((3, 3))
        kernel[row, col] = 1
        return kernel
    directional_data = [
    (kernel_at(1, 2), 0.1),
    (kernel_at(1, 0), 0.1),
    (kernel_at(2, 1), 0.1),
    (kernel_at(2, 2), 0.1),
    (kernel_at(2, 0), 0.1),
    (kernel_at(0, 1), 1.0),
    (kernel_at(0, 2), 0.7363961030678927), 
    (kernel_at(0, 0), 0.7363961030678927),

    ]
    grid = np.zeros((200, 200))
    grid[0, 0] = 1  
    prob_total = np.zeros((200,200))
    prob_total[0,1] = 0.1
    prob_total[1,0] = 0.1
    prob_total[1,1] = 0.1
    assert np.allclose(
        main.calculate_prob_total(grid, directional_data),
        prob_total
    )
    