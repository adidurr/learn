from unittest import TestCase, main
from mymath import add

class SimpleTest(TestCase):
        def test_add(self):
                self.assertEqual(add(4,5), 9)
                self.assertEqual(add(0,0), 0)
                self.assertEqual(add(0,-1), -1)
                self.assertEqual(add(0,-1.1), -1.1)

if __name__ == '__main__':
        main()
