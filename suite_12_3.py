import unittest
import tests_12_3

suite_test = unittest.TestSuite()
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(suite_test)