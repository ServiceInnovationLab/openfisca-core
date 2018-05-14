# -*- coding: utf-8 -*-

import time
import cProfile

from openfisca_core.scripts.simulation_generator import make_simulation, randomly_init_variable

from openfisca_france import CountryTaxBenefitSystem



tbs = CountryTaxBenefitSystem()

N = 1
P = 4 * N
NB_S = 10
period = '2018-04'

def init_simulation():
  simulation = make_simulation(tbs, P, N)
  # randomly_init_variable(simulation, 'salary', '2018-04', 4000)
  randomly_init_variable(simulation, 'salaire_net', '2018-04', 4000)
  # y = simulation.household.members_position
  # x = simulation.household.members

  return simulation

simulations = [init_simulation() for i in range(NB_S)]

def timed():
  for simulation in simulations:
    # salary_i = simulation.household.members('salary', '2018-04').sum()
    simulation.calculate('revenu_disponible', 2018)

# cProfile.run("timed()", 'NEW')


start_time = time.time()

timed()

dt = time.time() - start_time

print("Total time: --- %s seconds ---" % (dt))
