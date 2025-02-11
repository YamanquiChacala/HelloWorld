"""Pruebas para saluda al mundo"""

import unittest

class TestHelloWorld(unittest.TestCase):
    """Puebas generales"""

    def test_hello(self):
        """Algo aqui"""
        self.assertEqual(2,2)


if __name__ == '__main__':
    unittest.main()
    