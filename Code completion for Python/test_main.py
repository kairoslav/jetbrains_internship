from unittest import TestCase
from main import find_literals


class Test(TestCase):
    def test_find_literals(self):
        with self.subTest(msg="1"):
            self.assertEqual(find_literals(r""), [])
        with self.subTest(msg="2"):
            self.assertEqual(find_literals(r"'AAA' 'BBB' 'CCC'"), ['AAA', 'BBB', 'CCC'])
        with self.subTest(msg="3"):
            self.assertEqual(find_literals(r"'AAA' 'AAA'"), ['AAA', 'AAA'])
        with self.subTest(msg="4"):
            self.assertEqual(find_literals(r"'A\"A\"A' 'AAA'"), [r'A\"A\"A', 'AAA'])
        with self.subTest(msg="5"):
            self.assertEqual(find_literals(r"''"), [''])
        with self.subTest(msg="6"):
            self.assertEqual(find_literals(r"x = 'a \' b'; y = 'a \' b'"), [r'a \' b', r'a \' b'])
