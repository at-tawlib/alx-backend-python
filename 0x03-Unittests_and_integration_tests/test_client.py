#!/usr/bin/env python3
"""
Tests for client.py
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Parameterizxe and patch as decorators"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
        ])
    @patch("client.get_json")
    def test_org(self, org, expected_res, mock_function):
        """test GithubOrgClient.org and using @patch to make sure
        get_json is called once"""
        mock_function.return_value = MagicMock(return_value=expected_res)
        google_client = GithubOrgClient(org)
        self.assertEqual(google_client.org(), expected_res)
        mock_function.assert_called_once_with("https://api.github.com/orgs/{}"
                                              .format(org))
