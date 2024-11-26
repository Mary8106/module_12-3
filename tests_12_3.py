import unittest
import runner as rr
import runner_1 as rt


def frozen(func):
    def wrapper(atr):
        if atr.is_frozen == True:
            atr.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen
    def test_walk(self):
        walk_ = rr.Runner('cat')
        for _ in range(10):
            walk_.walk()
        self.assertEqual(walk_.distance, 50)
        print('Test "walk" OK')

    @frozen
    def test_run(self):
        run_ = rr.Runner('cat')
        for _ in range(10):
            run_.run()
        self.assertEqual(run_.distance, 100)
        print('Test "run" OK')

    @frozen
    def test_challenge(self):
        challenge1 = rr.Runner('cat_1')
        challenge2 = rr.Runner('cat_2')
        for _ in range(10):
            challenge1.run()
            challenge2.walk()
        self.assertNotEqual(challenge1.distance, challenge2.distance)
        print('Test "challenge" OK')


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @frozen
    def setUp(self):
        self.run1 = rt.Runner('Усэйн', 10)
        self.run2 = rt.Runner('Андрей', 9)
        self.run3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for testkey, testval in cls.all_results.items():
            print(f'TEST: {testkey}')
            for key, val in testval.items():
                result[key] = str(val.name)
            print(result)

    @frozen
    def testrun_1(self):
        run_1 = rt.Tournament(90, self.run1, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1} и {self.run3}'] = finish

    @frozen
    def testrun_2(self):
        run_1 = rt.Tournament(90, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run2} и {self.run3}'] = finish

    @frozen
    def testrun_3(self):
        run_1 = rt.Tournament(90, self.run1, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1}, {self.run2} и {self.run3}'] = finish


if __name__ == "__main__":
    unittest.main()