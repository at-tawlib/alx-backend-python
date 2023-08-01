# 0x03. Unittests and Integration Tests

### 0. Parameterize a unit test

[test_utils.py](test_utils.py), [utils.py](utils.py)

Familiarize yourself with the  `utils.access_nested_map`  function and understand its purpose. 
In this task you will write the first unit test for  `utils.access_nested_map`.

Create a  `TestAccessNestedMap`  class that inherits from  `unittest.TestCase`.

Implement the  `TestAccessNestedMap.test_access_nested_map`  method to test that the method returns what it is supposed to.

Decorate the method with  `@parameterized.expand`  to test the function for following inputs:
```
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
```
```
pc@pc:~$ python3 -m unittest test_utils.py -v
test_access_nested_map_0 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': 1}, path=['a'], expected=1] ... ok
test_access_nested_map_1 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': {'b': 2}}, path=['a'], expected={'b': 2}] ... ok
test_access_nested_map_2 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': {'b': 2}}, path=['a', 'b'], expected=2] ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s
```

### 1. Parameterize a unit test

[test_utils.py](test_utils.py), [utils.py](utils.py)

Implement  `TestAccessNestedMap.test_access_nested_map_exception`. Use the  `assertRaises`  context manager to test that a  `KeyError`  is raised for the following inputs (use  `@parameterized.expand`):

```
nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
```
Also make sure that the exception message is as expected.
```
pc@pc:~$ python3 -m unittest test_utils.py -v
test_access_nested_map_0 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': 1}, path=['a'], expected=1] ... ok
test_access_nested_map_1 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': {'b': 2}}, path=['a'], expected={'b': 2}] ... ok
test_access_nested_map_2 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': {'b': 2}}, path=['a', 'b'], expected=2] ... ok
test_access_nested_map_exception_0 (test_utils.TestAccessNestedMap)
Using assertRaises to test keyError of the function [with nested_map={}, path=['a']] ... ok
test_access_nested_map_exception_1 (test_utils.TestAccessNestedMap)
Using assertRaises to test keyError of the function [with nested_map={'a': 1}, path=['a', 'b']] ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```


### 2. Mock HTTP calls

[test_utils.py](test_utils.py), [utils.py](utils.py)

Define the  `TestGetJson(unittest.TestCase)`  class and implement the  `TestGetJson.test_get_json`  method to test that  `utils.get_json`  returns the expected result.

We don’t want to make any actual external HTTP calls. Use  `unittest.mock.patch`  to patch  `requests.get`. Make sure it returns a  `Mock`  object with a  `json`  method that returns  `test_payload`  which you parametrize alongside the  `test_url`  that you will pass to  `get_json`  with the following inputs:

```
test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
```

Test that the mocked  `get`  method was called exactly once (per input) with  `test_url`  as argument.

Test that the output of  `get_json`  is equal to  `test_payload`.
```
pc@pc:~$ python3 -m unittest test_utils.py -v
test_access_nested_map_0 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': 1}, path=['a'], expected=1] ... ok
test_access_nested_map_1 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': {'b': 2}}, path=['a'], expected={'b': 2}] ... ok
test_access_nested_map_2 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': {'b': 2}}, path=['a', 'b'], expected=2] ... ok
test_access_nested_map_exception_0 (test_utils.TestAccessNestedMap)
Using assertRaises to test keyError of the function [with nested_map={}, path=['a']] ... ok
test_access_nested_map_exception_1 (test_utils.TestAccessNestedMap)
Using assertRaises to test keyError of the function [with nested_map={'a': 1}, path=['a', 'b']] ... ok
test_get_json_0_http_example_com (test_utils.TestGetJson)
test get_json of utils.py [with url='http://example.com', expected_result={'payload': True}] ... ok
test_get_json_1_http_holberton_io (test_utils.TestGetJson)
test get_json of utils.py [with url='http://holberton.io', expected_result={'payload': False}] ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.002s
```

### 3. Parameterize and patch

[test_utils.py](test_utils.py), [utils.py](utils.py)

Implement the  `TestMemoize(unittest.TestCase)`  class with a  `test_memoize`  method.

Use  `unittest.mock.patch`  to mock  `a_method`. Test that when calling  `a_property`  twice, the correct result is returned but  `a_method`  is only called once using  `assert_called_once`.
```
pc@pc:~$ python3 -m unittest test_utils.py -v
test_access_nested_map_0 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': 1}, path=['a'], expected=1] ... ok
test_access_nested_map_1 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': {'b': 2}}, path=['a'], expected={'b': 2}] ... ok
test_access_nested_map_2 (test_utils.TestAccessNestedMap)
testing the method with assert [with nested_map={'a': {'b': 2}}, path=['a', 'b'], expected=2] ... ok
test_access_nested_map_exception_0 (test_utils.TestAccessNestedMap)
Using assertRaises to test keyError of the function [with nested_map={}, path=['a']] ... ok
test_access_nested_map_exception_1 (test_utils.TestAccessNestedMap)
Using assertRaises to test keyError of the function [with nested_map={'a': 1}, path=['a', 'b']] ... ok
test_get_json_0_http_example_com (test_utils.TestGetJson)
test get_json of utils.py [with url='http://example.com', expected_result={'payload': True}] ... ok
test_get_json_1_http_holberton_io (test_utils.TestGetJson)
test get_json of utils.py [with url='http://holberton.io', expected_result={'payload': False}] ... ok
test_memoize (test_utils.TestMemoize)
test for utils.memoize ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.004s

OK
```

### 4. Parameterize and patch as decorators

[test_client.py](test_client.py), [client.py](client.py)

In a new  `test_client.py`  file, declare the  `TestGithubOrgClient(unittest.TestCase)`  class and implement the  `test_org`  method.

This method should test that  `GithubOrgClient.org`  returns the correct value.

Use  `@patch`  as a decorator to make sure  `get_json`  is called once with the expected argument but make sure it is not executed.

Use  `@parameterized.expand`  as a decorator to parametrize the test with a couple of  `org`  examples to pass to  `GithubOrgClient`, in this order:

-   `google`
-   `abc`

Of course, no external HTTP calls should be made.
```
pc@pc:~$ python3 -m unittest test_client.py -v
test_org_0_google (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('google', {'login': 'google'})] ... ok
test_org_1_abc (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('abc', {'login': 'abc'})] ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

### 5. Mocking a property

[test_client.py](test_client.py), [client.py](client.py)

`memoize`  turns methods into properties. Read up on how to mock a property (see resource).

Implement the  `test_public_repos_url`  method to unit-test  `GithubOrgClient._public_repos_url`.

Use  `patch`  as a context manager to patch  `GithubOrgClient.org`  and make it return a known payload.

Test that the result of  `_public_repos_url`  is the expected one based on the mocked payload.
```
pc@pc:~$ python3 -m unittest test_client.py -v
test_org_0_google (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('google', {'login': 'google'})] ... ok
test_org_1_abc (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('abc', {'login': 'abc'})] ... ok
test_public_repos_url (test_client.TestGithubOrgClient)
test for GithubOrgClient._public_repos_url ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```


### 6. More patching

[test_client.py](test_client.py), [client.py](client.py)

Implement  `TestGithubOrgClient.test_public_repos`  to unit-test  `GithubOrgClient.public_repos`.

Use  `@patch`  as a decorator to mock  `get_json`  and make it return a payload of your choice.

Use  `patch`  as a context manager to mock  `GithubOrgClient._public_repos_url`  and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

Test that the mocked property and the mocked  `get_json`  was called once.
```
pc@pc:~$ python3 -m unittest test_client.py -v
test_org_0_google (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('google', {'login': 'google'})] ... ok
test_org_1_abc (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('abc', {'login': 'abc'})] ... ok
test_public_repos (test_client.TestGithubOrgClient)
test for GithubOrgClient.public_repos ... ok
test_public_repos_url (test_client.TestGithubOrgClient)
test for GithubOrgClient._public_repos_url ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
```


### 7. Parameterize

[test_client.py](test_client.py), [client.py](client.py)

Implement  `TestGithubOrgClient.test_has_license`  to unit-test  `GithubOrgClient.has_license`.
Parametrize the test with the following inputs
```
pc@pc:~$ python3 -m unittest test_client.py -v
repo={"license": {"key": "my_license"}}, license_key="my_license"
repo={"license": {"key": "other_license"}}, license_key="my_license"
```
You should also parameterize the expected returned value.
```
untest test_client.py -v
test_has_license_0 (test_client.TestGithubOrgClient)
test TestGithubOrgClient.has_license) [with repo={'license': {'key': 'my_license'}}, license_key='my_license', expected_res=True] ... ok
test_has_license_1 (test_client.TestGithubOrgClient)
test TestGithubOrgClient.has_license) [with repo={'license': {'key': 'other_license'}}, license_key='my_license', expected_res=False] ... ok
test_org_0_google (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('google', {'login': 'google'})] ... ok
test_org_1_abc (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('abc', {'login': 'abc'})] ... ok
test_public_repos (test_client.TestGithubOrgClient)
test for GithubOrgClient.public_repos ... ok
test_public_repos_url (test_client.TestGithubOrgClient)
test for GithubOrgClient._public_repos_url ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.004s

OK
```

### 8. Integration test: fixtures

[test_client.py](test_client.py), [client.py](client.py), [fixtures.py](fixtures.py)

We want to test the  `GithubOrgClient.public_repos`  method in an integration test. That means that we will only mock code that sends external requests.

Create the  `TestIntegrationGithubOrgClient(unittest.TestCase)`  class and implement the  `setUpClass`  and  `tearDownClass`  which are part of the  `unittest.TestCase`  API.

Use  `@parameterized_class`  to decorate the class and parameterize it with fixtures found in  `fixtures.py`. The file contains the following fixtures:

```
org_payload, repos_payload, expected_repos, apache2_repos
```

The  `setupClass`  should mock  `requests.get`  to return example payloads found in the fixtures.

Use  `patch`  to start a patcher named  `get_patcher`, and use  `side_effect`  to make sure the mock of  `requests.get(url).json()`  returns the correct fixtures for the various values of  `url`  that you anticipate to receive.

Implement the  `tearDownClass`  class method to stop the patcher.

### 9. Integration tests

[test_client.py](test_client.py), [client.py](client.py), [fixtures.py](fixtures.py)

Implement the  `test_public_repos`  method to test  `GithubOrgClient.public_repos`.

Make sure that the method returns the expected results based on the fixtures.

Implement  `test_public_repos_with_license`  to test the  `public_repos`  with the argument  `license="apache-2.0"`  and make sure the result matches the expected value from the fixtures.
```
pc@pc:~$ python3 -m unittest test_client.py -v
test_has_license_0 (test_client.TestGithubOrgClient)
test TestGithubOrgClient.has_license) [with repo={'license': {'key': 'my_license'}}, license_key='my_license', expected_res=True] ... ok
test_has_license_1 (test_client.TestGithubOrgClient)
test TestGithubOrgClient.has_license) [with repo={'license': {'key': 'other_license'}}, license_key='my_license', expected_res=False] ... ok
test_org_0_google (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('google', {'login': 'google'})] ... ok
test_org_1_abc (test_client.TestGithubOrgClient)
test GithubOrgClient.org and using @patch to make sure [with *args=('abc', {'login': 'abc'})] ... ok
test_public_repos (test_client.TestGithubOrgClient)
test for GithubOrgClient.public_repos ... ok
test_public_repos_url (test_client.TestGithubOrgClient)
test for GithubOrgClient._public_repos_url ... ok
test_public_repos (test_client.TestIntegrationGithubOrgClient_0)
test GithubOrgClient.public_repos ... ok
test_public_repos_with_license (test_client.TestIntegrationGithubOrgClient_0)
test GithubOrgClient.public_repos with license ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.006s

OK
```

> Written with [StackEdit](https://stackedit.io/).
