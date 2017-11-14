import unittest
from RomanToArabic import *


class RomanToArabicTests(unittest.TestCase):

    def test_i_eq_1(self):
        i = roman_numeral_to_int('I')
        self.assertEqual(1, i)

    def test_ii_eq_2(self):
        ii = roman_numeral_to_int('II')
        self.assertEqual(2, ii)

    def test_iii_eq_3(self):
        iii = roman_numeral_to_int('III')
        self.assertEqual(3, iii)

    def test_v_eq_5(self):
        v = roman_numeral_to_int('V')
        self.assertEqual(5, v)

    def test_xlix_eq_49(self):
        xlix = roman_numeral_to_int('XLIX')
        self.assertEqual(49, xlix)

    def test_p_invalid(self):
        p = valid('P')
        self.assertFalse(p)


if __name__ == '__main__':
    unittest.main()
