#!/usr/bin/python3
"""test module for Place class"""

import unittest
import pep8
import inspect
from models import place, BaseModel
from models.place import Place


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that models/place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_base(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'tests/test_models/test_place.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(place.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Place class docstring"""
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestPlace(unittest.TestCase):
    '''
        Testing Place class
    '''

    def setUp(self):
        '''
            Creates an instance for place.
        '''
        self.test_place = Place()

    def TearDown(self):
        """Remove an instance of the class"""
        del self.test_place

    def test_place_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''
        self.assertIsInstance(self.test_place, BaseModel)

    def test_place_attributes(self):
        '''
            Checks that the attribute exist.
        '''
        self.assertTrue("city_id" in self.test_place.__dir__())
        self.assertTrue("user_id" in self.test_place.__dir__())
        self.assertTrue("description" in self.test_place.__dir__())
        self.assertTrue("name" in self.test_place.__dir__())
        self.assertTrue("number_rooms" in self.test_place.__dir__())
        self.assertTrue("max_guest" in self.test_place.__dir__())
        self.assertTrue("price_by_night" in self.test_place.__dir__())
        self.assertTrue("latitude" in self.test_place.__dir__())
        self.assertTrue("longitude" in self.test_place.__dir__())
        self.assertTrue("amenity_ids" in self.test_place.__dir__())

    def test_type_longitude(self):
        '''
            Test the type of longitude.
        '''
        longitude = getattr(self.test_place, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_latitude(self):
        '''
            Test the type of latitude
        '''
        latitude = getattr(self.test_place, "latitude")
        self.assertIsInstance(latitude, float)

    def test_type_amenity(self):
        '''
            Test the type of latitude
        '''
        amenity = getattr(self.test_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    def test_type_price_by_night(self):
        '''
            Test the type of price_by_night
        '''
        price_by_night = getattr(self.test_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_max_guest(self):
        '''
            Test the type of max_guest
        '''
        max_guest = getattr(self.test_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_number_bathrooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_bathrooms = getattr(self.test_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_number_rooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_rooms = getattr(self.test_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_description(self):
        '''
            Test the type of description
        '''
        description = getattr(self.test_place, "description")
        self.assertIsInstance(description, str)

    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.test_place, "name")
        self.assertIsInstance(name, str)

    def test_type_user_id(self):
        '''
            Test the type of user_id
        '''
        user_id = getattr(self.test_place, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_city_id(self):
        '''
            Test the type of city_id
        '''
        city_id = getattr(self.test_place, "city_id")
        self.assertIsInstance(city_id, str)
