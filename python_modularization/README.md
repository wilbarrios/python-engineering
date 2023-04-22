# Python Modularization

Notes from: https://medium.com/geekculture/an-introduction-to-python-modules-and-packages-5da67bfb2a42

## Packages vs Modules

Every python file is a module, i.e. if you create a `calculator.py` file, you've created a calculator module.

### Import

```python
import <module_name>
```

#### Shortener

```python
import <module_name> as <shortened_name>
```

#### Import some functions

```python
from <module_name> import <function_1>, <function_2>
```

## Imports on scripts

The python interpreter frist searches the current directory from where the script is being run.

### Import search steps

- The same directory from where the script was run.
- The list of directories in the PYTHONPATH environment variable. You need to manually set the environment variable.
- The list of installation-dependent directories that were configured when Python was installed on your computer. (The modules from Python’s standard library and also the third-party modules that you install.)

## Package

- calc_pkg
  - __init.py
  - sum.py
  - sybtrack.py

## Namespaces
