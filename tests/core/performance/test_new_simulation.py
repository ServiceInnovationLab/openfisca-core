# -*- coding: utf-8 -*-

import time
from base import tax_benefit_system

# python -m core.performance.test_new_simulation

scenario = tax_benefit_system.new_scenario()

start_time = time.time()

for i in range(10):
    simulation = scenario.new_simulation()

dt = time.time() - start_time
print("Total time: --- %s seconds ---" % (dt))
