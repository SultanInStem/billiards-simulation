import numpy as np 
def to_math_coords(point, screen_size): 
    math_x = point[0] - (screen_size[0] // 2)
    math_y = (screen_size[1] // 2) - point[1]
    return (math_x, math_y) 

def to_screen_coords(point, screen_size):
    screen_x = point[0] + (screen_size[0] // 2) 
    screen_y = (screen_size[1] // 2) - point[1]
    return (screen_x, screen_y)

def normalize_vector(v): 
    mag = np.linalg.norm(v)
    if mag == 0: 
        return v 
    return v / mag