
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
	def setUp(self):
		self.calc = SimpleCalculator()

	def test_addition(self):
		self.assertEqual(self.calc.add(2, 3), 5)
		self.assertEqual(self.calc.add(-1, 1), 0)
		self.assertEqual(self.calc.add(0, 0), 0)
		self.assertEqual(self.calc.add(1000000, 1000000), 2000000)
		self.assertEqual(self.calc.add(2.5, 3.1), 5.6)
		self.assertEqual(self.calc.add(-2, -3), -5)
		self.assertEqual(self.calc.add(0, 5), 5)
		self.assertEqual(self.calc.add(-8, 1), -7)

	def test_subtraction(self):
		self.assertEqual(self.calc.subtract(5, 3), 2)
		self.assertEqual(self.calc.subtract(0, 5), -5)
		self.assertEqual(self.calc.subtract(-5, -3), -2)
		self.assertEqual(self.calc.subtract(0, 0), 0)
		self.assertEqual(self.calc.subtract(3.5, 2.5), 1.0)
		self.assertEqual(self.calc.subtract(1000000, 1), 999999)

	def test_multiply(self):
		self.assertEqual(self.calc.multiply(4, 3), 12)
		self.assertEqual(self.calc.multiply(-2, 3), -6)
		self.assertEqual(self.calc.multiply(-2, -3), 6)
		self.assertEqual(self.calc.multiply(0, 5), 0)
		self.assertEqual(self.calc.multiply(0, 0), 0)
		self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
		self.assertEqual(self.calc.multiply(1000000, 1000000), 1000000000000)

	def test_divide(self):
		self.assertEqual(self.calc.divide(10, 2), 5)
		self.assertEqual(self.calc.divide(5, 0), None)  # Edge case: division by zero
		self.assertEqual(self.calc.divide(0, 5), 0)
		self.assertEqual(self.calc.divide(-10, 2), -5)
		self.assertEqual(self.calc.divide(10, -2), -5)
		self.assertEqual(self.calc.divide(-10, -2), 5)
		self.assertEqual(self.calc.divide(5.5, 2), 2.75)
		self.assertEqual(self.calc.divide(1000000, 2), 500000)
		self.assertEqual(self.calc.divide(0, 0), None)  # Edge case: zero divided by zero

if __name__ == "__main__":
	unittest.main()

