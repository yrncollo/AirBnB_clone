#!/usr/bin/python3
"""
Test module for BaseModel class
"""

import unittest
import pep8
import inspect
from models import City, base_model
from models.city import City


class TestCityDocs(unittest.TestCase):
    """
    Test to check documentation for City class
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.base_func = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_style_base(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_style_Base(self):
        """Test that models/city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
