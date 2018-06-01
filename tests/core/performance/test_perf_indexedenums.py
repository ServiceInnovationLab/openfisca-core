from openfisca_france import CountryTaxBenefitSystem
import numpy as np
import time

N = 5000
tbs = CountryTaxBenefitSystem()

categorie_salarie_int = np.floor(np.random.rand(4 * N) * 8)
enum = tbs.get_variable('categorie_salarie').possible_values
categorie_salarie_enum = np.select([categorie_salarie_int == i for i in range(8)], enum)
categorie_salarie_enum = enum.encode(categorie_salarie_enum)

# compare 'select' function with different inputs : index vs enums
def test_elem():
	def formula_before(categorie_salarie):
		return np.select(
			[categorie_salarie == i for i in range(8)],
			range(100, 900, 100)
			)

	def formula_after(categorie_salarie):
		return np.select(
			[categorie_salarie == i for i in enum],
			range(100, 900, 100)
			)

	start_time = time.time()
	formula_before(categorie_salarie_int)
	t1 = time.time() - start_time
	print("BEFORE: --- %s seconds ---" % (t1))


	start_time_2 = time.time()
	formula_after(categorie_salarie_enum)
	t2 = time.time() - start_time_2
	print("AFTER: --- %s seconds ---" % (t2))

	print(t2/t1)

test_elem()
