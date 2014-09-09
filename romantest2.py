import unittest
import roman1
from romantest1 import KnownValues as kv

class ToRomanBadInput(unittest.TestCase):

	def test_too_large(self):
		'''to_roman shoul fail with large input'''
		self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 4000)

	def test_zero(self):
		''' to_roman should fail with 0 input '''
		self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 0)

	def test_negative(self):
		'''to_roman should fail with negative input'''
		self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, -1)
	def test_no_integer(self):
		'''to_roman should fail with float input '''
		self.assertRaises(roman1.NoIntegerError,roman1.to_roman,0.5)
	def test_from_roman_known_values(self):
		'''from_roman should give known result with known input'''
		for integer, numeral in kv.known_values:
			result = roman1.from_roman(numeral)
			self.assertEqual(integer, result)	
	def test_roundtrip(self):
		'''from_roman(to_roman(n))==n for all n'''
		for integer in range(1, 4000):
			numeral = roman1.to_roman(integer)
			result = roman1.from_roman(numeral)
			self.assertEqual(integer, result)

if __name__ == '__main__':
	unittest.main()
