from unittest import TestCase
from main import find_literals


class Test(TestCase):
    def test_find_literals(self):
        self.assertEqual(find_literals(""), [])
        self.assertEqual(find_literals("'AAA' 'BBB' 'CCC'"), ['AAA', 'BBB', 'CCC'])
        self.assertEqual(find_literals("'AAA' 'AAA'"), ['AAA', 'AAA'])
        self.assertEqual(find_literals("'A\"A\"A' 'AAA'"), ['A\"A\"A', 'AAA'])
        self.assertEqual(find_literals("''"), [''])
