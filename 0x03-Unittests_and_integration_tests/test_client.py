#!/usr/bin/env python3
"""
Tests for client.py
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators"""

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

    def test_public_repos_url(self):
        """test for GithubOrgClient._public_repos_url"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock
        ) as mock_property:
            mock_property.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """test for GithubOrgClient.public_repos"""
        test_payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "id": 7968417,
                    "name": "dagger",
                    "full_name": "google/dagger",
                    "private": False,
                    "owner": {
                            "login": "google",
                            "id": 1342004,
                    },
                    "fork": True,
                    "url": "https://api.github.com/repos/google/dagger",
                    "created_at": "2013-02-01T23:14:14Z",
                    "updated_at": "2019-12-03T12:39:55Z",
                    "pushed_at": "2019-11-27T21:20:38Z",
                },
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "owner": {
                            "login": "google",
                            "id": 1342004,
                    },
                    "fork": False,
                    "url":
                    "https://api.github.com/repos/google/episodes.dart",
                        "created_at": "2013-01-19T00:31:37Z",
                        "updated_at": "2019-09-23T11:53:58Z",
                        "pushed_at": "2014-10-09T21:39:33Z",
                },
                {
                    "id": 7776515,
                    "name": "cpp-netlib",
                        "full_name": "google/cpp-netlib",
                        "private": False,
                        "owner": {
                            "login": "google",
                            "id": 1342004,
                        },
                    "fork": True,
                    "url":
                    "https://api.github.com/repos/google/cpp-netlib",
                        "created_at": "2013-01-23T14:45:32Z",
                        "updated_at": "2019-11-15T02:26:31Z",
                        "pushed_at": "2018-12-05T17:42:29Z",
                },
            ]}
        mock_get_json.return_value = test_payload["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "dagger",
                    "episodes.dart",
                    "cpp-netlib",
                ],
            )
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, expected_res):
        """test TestGithubOrgClient.has_license)"""
        org_client = GithubOrgClient("google")
        has_license = org_client.has_license(repo, license_key)
        self.assertEqual(has_license, expected_res)
