# -*- coding: utf-8 -*-

import time
import cProfile

from openfisca_core.scripts.simulation_generator import make_simulation, randomly_init_variable

from openfisca_france import CountryTaxBenefitSystem


tbs = CountryTaxBenefitSystem()

N = 1  # nombre familles
P = 4 * N  # nombre personnes
NB_S = 10
PERIOD = '2018-04'


def init_simulation(with_trace):
  simulation = make_simulation(tbs, P, N, trace=with_trace)
  # randomly_init_variable(simulation, 'salary', '2018-04', 4000)
  randomly_init_variable(simulation, 'salaire_net', PERIOD, 4000)
  # y = simulation.household.members_position
  # x = simulation.household.members

  return simulation

simulations_with_trace = [init_simulation(True) for i in range(NB_S)]
simulations_without_trace = [init_simulation(False) for i in range(NB_S)]


# test calculate
def timed_without_trace():
  for simulation in simulations_without_trace:
    # salary_i = simulation.household.members('salary', '2018-04').sum()
    simulation.calculate('revenu_disponible', 2018)

def timed_with_trace():
  for simulation in simulations_with_trace:
    # salary_i = simulation.household.members('salary', '2018-04').sum()
    simulation.calculate('revenu_disponible', 2018)


# measure specific function duration
print("Without trace - #simulations: " + str(NB_S))
start_time = time.time()
timed_without_trace()
dt_without = time.time() - start_time
print("Total time: --- %s seconds ---" % (dt_without))

print("With trace - #simulations: " + str(NB_S))
start_time = time.time()
timed_with_trace()
dt_with = time.time() - start_time
print("Total time: --- %s seconds ---" % (dt_with))

print("% diff: " + str(100 * ((dt_with - dt_without)/dt_without)))

# profile specific function
# cProfile.run("timed()", 'timed.prof')
