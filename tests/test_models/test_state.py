#!/usr/bin/python3
"""
This contain all tests for state
"""
import unittest
import inspect
import pep8
from models import state, BaseModel
from models.state import State


class TestStateDocs(unittest.TestCase):
    """
    To check for documentation
    """
    @classmethod
    def setUpClass(cls):
        cls.base_func = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_style_base(self):
        """
        To tests for pep8 styling has been met
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_pep8_style_Base(self):
        """
        To tests for pep8 styling has been met
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_module_docstring(self):
        """
        Test for module docstring
        """
        self.assertTrue(len(state.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test for state class docstring
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstings(self):
        """
        Test for docstring in all the functions
        """
        for func in self.base_func:
            self.assertTrue(len(func[1].__doc__) >= 1)
