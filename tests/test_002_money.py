import unittest
from math import isclose

from pyfolio.money import Money 

class TestMoney(unittest.TestCase):
    def setUp(self):
        """Set Up de Money"""
        self.money = Money(1000)
    
    def test_pv_discreto(self):
        self.assertTrue(isclose(self.money.pv(0.05, 10), 613.91, rel_tol=1e-2))

    def test_pv_continuo(self):
        self.assertTrue(isclose(self.money.pv(0.05, 10, False), 606.53, rel_tol=1e-2))

    def test_fv_discreto(self):
        self.assertTrue(isclose(self.money.fv(0.05, 10), 1628.89, rel_tol=1e-2))

    def test_fv_continuo(self):
        self.assertTrue(isclose(self.money.fv(0.05, 10, False), 1648.72, rel_tol=1e-2))

    def test_invalid_pv_argument(self):
        with self.assertRaises(ValueError):
            self.money.pv(0.05, 10, 'x')

    def test_invalid_fv_argument(self):
        with self.assertRaises(ValueError):
            self.money.fv(0.05, 10, 'x')

if __name__ == '__main__':
    unittest.main(verbosity=2)
