# Standard Library
import os

POP_SIZE = int(os.environ.get('POP_SIZE', 10))
CROSSOVER_RATE = float(os.environ.get('CROSSOVER_RATE', 0.4))
MUTATION_RATE = float(os.environ.get('MUTATION_RATE', 0.01))
