
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
	def setUp(self):
		self.calc = SimpleCalculator()

	def test_add(self):
		self.assertEqual(self.calc.add(2, 3), 5)
		self.assertEqual(self.calc.add(-1, 1), 0)
		self.assertEqual(self.calc.add(4, 3), 7)
		self.assertEqual(self.calc.add(-8, 1), -7)

	def test_subtraction(self):
		self.assertEqual(self.calc.subtract(5, 3), 2)
		self.assertEqual(self.calc.subtract(0, 5), -5)

	def test_multiply(self):
		self.assertEqual(self.calc.multiply(4, 3), 12)
		self.assertEqual(self.calc.multiply(-2, 3), -6)

	def test_divide(self):
		self.assertEqual(self.calc.divide(10, 2), 5)
		self.assertEqual(self.calc.divide(5, 0), None)  # Edge case: division by zero
		self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == "__main__":
	unittest.main()

