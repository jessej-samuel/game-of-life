WIDTH = 700
HEIGHT = 690
FPS = 60

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (169, 169, 169)

alive_color = WHITE
dead_color = BLACK
bg_color = DARK_GRAY

cell_size = 5
cell_count = 90  # No. of cells in a row
grid_offset = (WIDTH - (cell_count+cell_count*cell_size+1))//2
