import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """ Test rectangle class """
    def setUp(self):
        self.rectangle1 = Rectangle(5, 10)
        self.rectangle2 = Rectangle(7, 3, 2, 4, 1)

    """ Test area function """
    def test_area(self):
        self.assertEqual(self.rectangle1.area(), 50)
        self.assertEqual(self.rectangle2.area(), 21)

    """ Test display function """
    def test_display(self):
        rectangle_dis = Rectangle(5, 10)
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_dis.display()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output = "#####\n" * 10
        self.assertEqual(output, expected_output)

    def test_update(self):
        self.rectangle1.update(2, 8, 6, 1, 2)
        self.assertEqual(self.rectangle1.width, 8)
        self.assertEqual(self.rectangle1.height, 6)
        self.assertEqual(self.rectangle1.x, 1)
        self.assertEqual(self.rectangle1.y, 2)


if __name__ == '__main__':
    unittest.main()
