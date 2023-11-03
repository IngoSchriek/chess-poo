import numpy as np

estado = np.array(['--']*24 + ['T']).reshape(5, 5)
estado[0][0] = 1
print(estado)