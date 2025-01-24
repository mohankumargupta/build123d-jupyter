# %%
from build123d import *

# %%

box = Box(10,10,10)
box

# %%

print(box.show_topology())

# %%

with BuildPart() as part_builder:
    with BuildSketch() as sketch:
        Rectangle(50,20)
    extrude(amount=10)
    
part = part_builder.part
part


