import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from generator import *

# print_grid(generate_symmetric_grid('R', 'KNIGHT'))
print_grid(generate_grid('KNIGHT'))