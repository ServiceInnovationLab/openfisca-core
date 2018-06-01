# -*- coding: utf-8 -*-

import time
from .base import tax_benefit_system

# python -m core.performance.test_new_simulation

scenario = tax_benefit_system.new_scenario()
# scenario.init_single_entity()

start_time = time.time()

simulation = scenario.new_simulation()
# simulation = Simulation(tax_benefit_system = tax_benefit_system, scenario)

dt = time.time() - start_time
print("Total time: --- %s seconds ---" % (dt))
