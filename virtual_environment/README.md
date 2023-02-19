# Python virtual environment

Python natively can setup **virtual environments**, which is:

>  A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available. [Python docs | venv](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20created,the%20virtual%20environment%20are%20available.)

## Quick guide

|Action|Command|Sample|
|---|---|---|
|Create venv|`python3 -m venv *venv_directory*`|`python3 -m venv .venv`|
|Activeate venv|`source *venv_directory*/bin/activate`|n/a|
|Deactivate venv (.venv)|`deactivate`|n/a|

### Notes

- `-m` means module.
- `(.venv)` means the venv is active.
- The `.venv` directory is recommended to be .gitignored, as this directory contains the installed dependencies.
- Export dependencies list file with `pip3 freeze > requirements.txt` and **COMMIT** this file.

## TODO

- [poetry tool | PYTHON PACKAGING AND DEPENDENCY MANAGEMENT MADE EASY](https://python-poetry.org/)
- https://medium.com/towards-data-science/best-practices-for-python-development-bf74c2880f87
