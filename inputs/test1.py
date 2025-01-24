# %%
from build123d import *

from IPython.display import display

# %%

pts = [(0, 0), (20, 20), (40, 0), (0, -40), (-60, 0), (0, 100), (100, 0)]
wts = [1.0, 1.0, 2.0, 3.0, 4.0, 2.0, 1.0]

ex30_ln = Polyline(pts) + Bezier(pts, weights=wts)
ex30_sk = make_face(ex30_ln)
ex30 = extrude(ex30_sk, -10)

display(ex30)

# %%

import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-10, 10)
plt.plot(X, X**2)

# %%

a, b, c = 80.0, 10.0, 1.0

ex32_sk = RegularPolygon(2 * b, 6, rotation=30)
ex32_sk += PolarLocations(a / 2, 6) * RegularPolygon(b, 4)
ex32 = Part() + [extrude(obj, c + 3 * idx) for idx, obj in enumerate(ex32_sk.faces())]
display(ex32)

