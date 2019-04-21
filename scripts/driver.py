import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from generator import *

puzzle = generate_symmetric_grid('D+', 'DEFAULT', True)
print_grid(puzzle)