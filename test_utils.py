# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.compute(5),0)
        # À compléter...
        pass
    
    def test_roots(self):
        self.assertEqual(utils.compute(1,0,1),1.4)
        # À compléter...
        pass
    
    def test_integrate(self):
        self.assertEqual(utils.compute(3),3)
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
