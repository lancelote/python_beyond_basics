# Organizing Larger Programs

## Path

```python
import sys
sys.path
```

First item is a current directory:
```python
sys.path[0] == ''
```

To add module to path:
```python
sys.append('module_name')
```

Adding via environment variable:
```bash
export PYTHONPATH=module_name
```

## Module

A Python file

## Package

- A directory with `__init__.py` (package init file) file inside
- Package init file is sourced upon package importing
- Packages are modules that contains other modules

## Absolute Imports
