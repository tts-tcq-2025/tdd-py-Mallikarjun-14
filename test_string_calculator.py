import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers_comma_delimited(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_unknown_amount_of_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4,5"), 15)

    def test_newlines_between_numbers(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_invalid_delimiter_pattern(self):
        # Not needed to prove error, just ensuring no silent pass
        with self.assertRaises(ValueError):
            self.calc.add("1,\n")

    def test_custom_single_char_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_negative_number_raises(self):
        with self.assertRaises(Exception) as context:
            self.calc.add("1,-2,3,-4")
        self.assertIn("negatives not allowed", str(context.exception))
        self.assertIn("-2", str(context.exception))
        self.assertIn("-4", str(context.exception))

    def test_numbers_greater_than_1000_ignored(self):
        self.assertEqual(self.calc.add("2,1001"), 2)

    def test_custom_delimiter_any_length(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)

    def test_multiple_custom_delimiters(self):
        self.assertEqual(self.calc.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_custom_delimiters_any_length(self):
        self.assertEqual(self.calc.add("//[**][%%]\n1**2%%3"), 6)

if __name__ == "__main__":
    unittest.main()
