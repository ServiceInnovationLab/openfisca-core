# -*- coding: utf-8 -*-

import time
from .base import tax_benefit_system, init_simulation

# python -m core.performance.test_calculate

# Set up
simulations = [init_simulation() for i in range(10)]

# Test
start_time = time.time()

for simulation in simulations:
    simulation.calculate('revenu_disponible', 2018)

dt = time.time() - start_time
print("Total time: --- %s seconds ---" % (dt))

# Tear down
simulations = None
