#!/usr/bin/python3
""" Test for base class """
import unittest
import os
from models import Base


class TestBase(unittest.TestCase):
    """ Test base class """
    def test_id(self):
        """ id test """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base(10)
        self.assertEqual(obj3.id, 10)
        obj4 = Base(-20)
        self.assertEqual(obj4, -20)

    def test_to_json_string(self):
        """ convert list to json - test """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), {"id": 1})
        self.assertEqual(Base.to_json_string([False]), False)

    def test_from_json_string(self):
        """ convert json to list - test"""
        self.assertAlmostEqual(Base.from_json_string(None), [])
        self.assertAlmostEqual(Base.from_json_string("[]"), [])
        test = Base.from_json_string('[{ "id": 30 }]')
        self.assertAlmostEqual(test, [{"id": 30}])

    def test_save_to_file(self):
        """test save_to_file."""
        r1 = Base.save_to_file(None)
        self.assertEqual(Base.load_from_file(), [])
        os.remove("./Square.json")
        r1 = Base.save_to_file([])
        self.assertEqual(Base.load_from_file(), [])
        os.remove("./Square.json")
        r1 = Base.save_to_file([Base.Square(1)])
        self.assertIsInstance(Base.load_from_file()[0], Base.Square)
        os.remove("./Square.json")
        r1 = Base.load_from_file()
        self.assertEqual(Base.save_to_file(r1), None)


if __name__ == "__main__":
    unittest.main()
