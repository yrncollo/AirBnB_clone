#!/usr/bin/python3
"""
This contain all tests for state
"""
import untittest
import inspect
import pep8
from models import state, BaseModel
from models.state import State


class TestStateDocs(untittest.TestCase):
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
