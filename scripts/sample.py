import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../solver'))
from generator import *

# puzzle = generate_symmetric_grid('R', 'KNIGHT', True)
puzzle = generate_grid('KNIGHT', True)
print score(puzzle, 'KNIGHT')
print_grid(puzzle)