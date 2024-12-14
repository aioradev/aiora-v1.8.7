# aiora/utils.py
import numpy as np

def generate_theoretical_vector(size: int = 256):
    """
    Generate a high-dimensional theoretical research vector
    """
    return np.random.normal(0, 1, size=size)
