# -*- coding: utf-8 -*-

from openfisca_core.scripts.simulation_generator import make_simulation, randomly_init_variable
from openfisca_france import CountryTaxBenefitSystem


NB_FAMILIES = 1
NB_PERSONS = 4 * NB_FAMILIES
NB_SIMULATIONS = 10

VARIABLE = 'salaire_net'
VARIABLE_VALUE = 4000
PERIOD = '2018-04'

ACTIVATE_TRACE=False


tax_benefit_system = CountryTaxBenefitSystem()


def init_simulation():
  simulation = make_simulation(tax_benefit_system, NB_PERSONS, NB_FAMILIES, trace=ACTIVATE_TRACE)
  randomly_init_variable(simulation, VARIABLE, PERIOD, VARIABLE_VALUE)

  return simulation
