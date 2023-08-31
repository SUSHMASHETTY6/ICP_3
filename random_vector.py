
import numpy as np
z = np.random.uniform(1, 20, 20)
m = z.reshape(4, 5)
print(m)

m = np.where(m == np.max(m, axis=1, keepdims=True), 0, m)
print(m)