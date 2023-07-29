#!/usr/bin/env python3
"""
test for utils.py functions
"""
import unittest
from utils import access_nested_map as anp
from utils import get_json
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test"""

    @parameterized.expand([
        [{"a": 1},  ["a"], 1],
        [{"a": {"b": 2}}, ["a"], {"b": 2}],
        [{"a": {"b": 2}}, ["a", "b"], 2]
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ testing the method with assert"""
        self.assertEqual(anp(nested_map, path), expected)

    @parameterized.expand([
            [{}, ["a"]],
            [{"a": 1}, ["a", "b"]]
            ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Using assertRaises to test keyError of the function"""
        with self.assertRaises(KeyError):
            anp(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, expected_result):
        """test get_json of utils.py"""
        mock_res = Mock()
        mock_res.json.return_value = expected_result
        with patch('requests.get', return_value=mock_res):
            response = get_json(url)
            self.assertEqual(response, expected_result)
