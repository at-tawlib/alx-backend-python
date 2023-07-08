# 0x00. Python - Variable Annotations
`Python` -- `Back-end`
## Requirements

### General
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using  `python3`  (version 3.7)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/env python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `pycodestyle`  style (version 2.5.)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

### 0. Basic annotations - add
Files:  [0-add.py](0-add.py), [0-main.py](0-main.py)

Write a type-annotated function  `add`  that takes a float  `a`  and a float  `b`  as arguments and returns their sum as a float.

```
bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

### 1. Basic annotations - concat
Files:  [1-concat.py](1-concat.py), [1-main.py](1-main.py)

Write a type-annotated function  `concat`  that takes a string  `str1`  and a string  `str2`  as arguments and returns a concatenated string

```
bob@dylan:~$ ./1-main.py
True
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
```

### 2. Basic annotations - floor
Files:  [2-floor.py](2-floor.py), [2-main.py](2-main.py)

Write a type-annotated function  `floor`  which takes a float  `n`  as argument and returns the floor of the float.

```
bob@dylan:~$ ./2-main.py
True
{'n': <class 'float'>, 'return': <class 'int'>}
floor(3.14) returns 3, which is a <class 'int'>
```

### 3. Basic annotations - to string
File:  [3-to_str.py](3-to_str.py), [3-main.py](3-main.py)

Write a type-annotated function  `to_str`  that takes a float  `n`  as argument and returns the string representation of the float.

```
bob@dylan:~$ ./3-main.py
True
{'n': <class 'float'>, 'return': <class 'str'>}
to_str(3.14) returns 3.14, which is a <class 'str'>
```

### 4. Define variables
Files:  [4-define_variables.py](4-define_variables.py), [4-main.py](4-main.py)

Define and annotate the following variables with the specified values:

-   `a`, an integer with a value of 1
-   `pi`, a float with a value of 3.14
-   `i_understand_annotations`, a boolean with a value of True
-   `school`, a string with a value of “Holberton”

```
bob@dylan:~$ ./4-main.py
a is a <class 'int'> with a value of 1
pi is a <class 'float'> with a value of 3.14
i_understand_annotations is a <class 'bool'> with a value of True
school is a <class 'str'> with a value of Holberton
```

### 5. Complex types - list of floats
Files:  [5-sum_list.py](5-sum_list.py), [5-main.py](5-main.py)

Write a type-annotated function  `sum_list`  which takes a list  `input_list`  of floats as argument and returns their sum as a float.

```
bob@dylan:~$ ./5-main.py
True
{'input_list': typing.List[float], 'return': <class 'float'>}
sum_list(floats) returns 6.470000000000001 which is a <class 'float'>
```

### 6. Complex types - mixed list
Files:  [6-sum_mixed_list.py](6-sum_mixed_list.py), [6-main.py](6-main.py)

Write a type-annotated function  `sum_mixed_list`  which takes a list  `mxd_lst`  of integers and floats and returns their sum as a float.

```
bob@dylan:~$ ./6-main.py
{'mxd_lst': typing.List[typing.Union[int, float]], 'return': <class 'float'>}
True
sum_mixed_list(mixed) returns 679.13 which is a <class 'float'>
```

### 7. Complex types - string and int/float to tuple
Files:  [7-to_kv.py](7-to_kv.py) , [7-main.py](7-main.py)

Write a type-annotated function  `to_kv`  that takes a string  `k`  and an int OR float  `v`  as arguments and returns a tuple. The first element of the tuple is the string  `k`. The second element is the square of the int/float  `v`  and should be annotated as a float.

```
bob@dylan:~$ ./7-main.py
{'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
('eggs', 9)
('school', 0.0004)
```

### 8. Complex types - functions
File:  [8-make_multiplier.py](8-make_multiplier.py) , [8-main.py](8-main.py)

Write a type-annotated function  `make_multiplier`  that takes a float  `multiplier`  as argument and returns a function that multiplies a float by  `multiplier`.

```
bob@dylan:~$ ./8-main.py
{'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}
4.928400000000001
```

### 9. Let's duck type an iterable object
File:  [9-element_length.py](9-element_length.py), [9-main.py](9-main.py)

Annotate the below function’s parameters and return values with the appropriate types

```
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

```
bob@dylan:~$ ./9-main.py 
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
```

> Written with [StackEdit](https://stackedit.io/).
