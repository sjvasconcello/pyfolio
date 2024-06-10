import unittest
from pyfolio.bonds import ZeroCouponBond, CouponBond

class TestBond(unittest.TestCase):
    def test_ZeroCouponBond(self):
        # Crear un bono cupón cero
        bond = ZeroCouponBond(1000, 10, 0.05)

        # Test calcular precio
        self.assertAlmostEqual(bond.calculate_price(), 613.91, delta=0.01)

        # Test representación de cadena
        self.assertEqual(repr(bond), "ZeroCouponBond(1000, 10, 0.05)")

    def test_CouponBond(self):
        # Crear un bono cupón
        bond = CouponBond(1000, 10, 0.05, 0.04)

        # Test calcular precio
        self.assertAlmostEqual(bond.calculate_price(), 922.78, delta=0.01)

        #! Test representación de cadena
        self.assertEqual(repr(bond), "CouponBond(1000, 10, 0.05, 0.04)")

    def test_invalid_type(self):
        # Verificar tipo de interés inválido
        with self.assertRaises(ValueError):
            ZeroCouponBond(1000, 10, "x")
        
        with self.assertRaises(ValueError):
            CouponBond(1000, 10, 0.05, "x")

if __name__ == '__main__':
    unittest.main()
