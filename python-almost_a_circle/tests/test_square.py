import unittest
from models import square


class TestSquare(unittest.TestCase):
    """ Test square class """
    def general_test(self):
        self.assertEqual(square.Square.width(1), 1)
        self.assertEqual(square.Square(1, 3).x, 3)
        self.assertEqual(square.Square(1, 2, 4).y, 4)
        self.assertEqual(square.Square(1, 2, 3, 4, 5).id, 5)

    def str_test(self):
        test_string = square.Square(1, 2, 3, 4).__str__()
        self.assertEqual(test_string, "[Square] (4) 2/3 - 1")

    def update_test(self):
        sq12 = square.Square(1, 1, 2, 2)
        self.assertEqual(str(sq12), "[Square] (2) 1/2 - 1")
        sq12.update(89)
        self.assertEqual(str(sq12), "[Square] (89) 1/2 - 1")
        sq12.update(89, 2)
        self.assertEqual(str(sq12), "[Square] (89) 1/2 - 2")
        sq12.update(89, 2, 3)
        self.assertEqual(str(sq12), "[Square] (89) 3/2 - 2")
        sq12.update(89, 2, 3, 4)
        self.assertEqual(str(sq12), "[Square] (89) 3/4 - 2")


if __name__ == '__main__':
    unittest.main()
