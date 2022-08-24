# Auto Generate Python Docstrings 

## Quick Start

```console
$ python3 docstring_generator_auto.py test.py

Function `hello1`
Params ['a:str', 'b:list', 'c']
Do you want to write docstring for `hello1` ? (y/n)                     
Enter function summary:  This is first hello
Are you sure? (y/n)  

a : str
Enter parameter summary:  first param
Are you sure? (y/n)  

b : list
Enter parameter summary:  second param
Are you sure? (y/n)  

c : 
Enter parameter summary:  third param
Are you sure? (y/n)  

Function `hello2`
Params ['a:tuple']
Do you want to write docstring for `hello2` ? (y/n)  y
Enter function summary:  This is second hello
Are you sure? (y/n)  

a : tuple
Enter parameter summary:  first param of second hello
Are you sure? (y/n)  

Function `hello3` has no parameters
Do you want to write docstring for `hello3` ? (y/n)  
Enter function summary:  This is third hello with no parameters
Are you sure? (y/n)  
New file with docstings saved at : `test_docstrings.py`
```

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