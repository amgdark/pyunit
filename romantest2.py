import unittest, roman1

class ToRomanBadInput(unittest.TestCase):
	def test_too_large(self):
		'''to_roman shoul fail with large input'''
		self.assertRaises(roman1.OutOfRangeError, roman1.to_roman,4000)

if __name__ == '__main__':
	unittest.main()