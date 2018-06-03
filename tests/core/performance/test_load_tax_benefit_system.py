# -*- coding: utf-8 -*-

import time
from openfisca_france import CountryTaxBenefitSystem


start_time = time.time()
tax_benefit_system = CountryTaxBenefitSystem()
dt = time.time() - start_time
print("Total time: --- %s seconds ---" % (dt))

# Tear down
tax_benefit_system = None
