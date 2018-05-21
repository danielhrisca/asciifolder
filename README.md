## asciifolder
pretty print folder structure to cli

### Install
```
pip install asciifolder
```

### Usage

```python
>>> asciifolder "Python/Lib/concurent"

>>>
concurrent/
├── __pycache__/
│   └── __init__.cpython-36.pyc
├── futures/
│   ├── __pycache__/
│   │   ├── __init__.cpython-36.pyc
│   │   ├── _base.cpython-36.pyc
│   │   ├── process.cpython-36.pyc
│   │   └── thread.cpython-36.pyc
│   ├── __init__.py
│   ├── _base.py
│   ├── process.py
│   └── thread.py
└── __init__.py
```

```python
from asciifolder import folde2ascii

for line in folder2ascii(path):
    print(line)
```