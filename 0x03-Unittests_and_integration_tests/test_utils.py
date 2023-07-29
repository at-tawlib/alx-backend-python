#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from utils import access_nested_map as anp
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        [{"a": 1},  ["a"], 1],
        [{"a": {"b": 2}}, ["a"], {"b": 2}],
        [{"a": {"b": 2}}, ["a", "b"], 2]
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ testing the method with assert"""
        self.assertEqual(anp(nested_map, path), expected)
