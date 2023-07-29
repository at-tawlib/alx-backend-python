#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from utils import access_nested_map as anp


class TestAccessNestedMap(unittest.TestCase):

    def test_access_nested_map(self):
        """ testing the method with assert"""
        self.assertEqual(anp(nested_map={"a": 1}, path=("a",)), 1)
        self.assertNotEqual(anp(nested_map={"a": {"b": 2}}, path=("a",)), 2)
        self.assertEqual(anp(nested_map={"a": {"b": 2}}, path=("a", "b")), 2)
