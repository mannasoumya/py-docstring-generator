# Auto Generate Python Docstrings 

## Quick Start

```console
$ python3 docstring_generator_auto.py test.py

Function `hello1`
Params ['a:str', 'b:list', 'c']
Do you want to write docstring for `hello1` ? (y/n)  y
Enter function summary:  This is first hello
Are you sure? (y/n)  y

a : str
Enter parameter summary:  first param
Are you sure? (y/n)  y

b : list
Enter parameter summary:  second param
Are you sure? (y/n)  y

c : 
Enter parameter summary:  third param
Are you sure? (y/n)  y

Function `hello2`
Params ['a:tuple']
Do you want to write docstring for `hello2` ? (y/n)  y
Enter function summary:  This is second hello
Are you sure? (y/n)  y

a : tuple
Enter parameter summary:  Tuple param
Are you sure? (y/n)  y

Function `hello3` has no parameters
Do you want to write docstring for `hello3` ? (y/n)  y
Enter function summary:  This is third hello
Are you sure? (y/n)  y

New file with docstings saved at : `test_docstrings.py`
```

#### When all docstrings are added, skip all functions
```console
$ python3 docstring_generator_auto.py test.py

Function `hello1`
Params ['a:str', 'b:list', 'c']
Do you want to write docstring for `hello1` ? (y/n)  n

Function `hello2`
Params ['a:tuple']
Do you want to write docstring for `hello2` ? (y/n)  n

Function `hello3` has no parameters
Do you want to write docstring for `hello3` ? (y/n)  n

No docstrings to save... Exiting
```
 **New file with docstring is generated at <file-path_docstrings.py>** 