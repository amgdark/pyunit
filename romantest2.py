import unittest
import roman1


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

if __name__ == '__main__':
	unittest.main()
