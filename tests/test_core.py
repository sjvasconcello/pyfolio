

import unittest
from pyfolio.core import main_function

class TestCore(unittest.TestCase):
    def test_main_function(self):
        self.assertEqual(main_function(), "Hello from the core function!")

if __name__ == '__main__':
    unittest.main()
