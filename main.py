from printer import print_parameters
from plotting import *

source = [0.9, 0.24, 0.55, -1.45, 0.17, -0.56, 1.45, 0.86, -0.22, -0.91,
          -1, 0.62, -1.45, -0.52, -1.31, 1.45, 0.54, -1.73, -0.64, 1.45]
source = sorted(source)

print_parameters(source)

show_graphs(source)
