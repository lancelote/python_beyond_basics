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

`from module1.reader.reader import Reader`

## Relative Imports

`from .reader import Reader`

- Can be helped but should be generally avoided

## `__all__`

- List of attribute names imported via `from module import *`

## Namespace Packages

- Have no `__init__.py` file (this avoids complex initialisation ordering
  problems)

```
path1
  - split_farm
    - bovine
        __init__.py
        common.py
        cow.py
        ox.py
        string.py
path2
  - split_farm
    - bird
      __init__.py
      chicken.py
      turkey.py
```

`path1` and `path2` should be in the `sys.path`

```python
import sys
sys.path.extend(['path1', 'path2'])
import split_farm

print(split_farm.__path__)

import split_farm.bovine
import split_farm.bird
```

## Executable Directories

```
reader
    __main__.py
    - reader
        __init__.py
        - compressed
            __init__.py
            bzipped.py
            gzipped.py
        reader.py
```

## Executable Zip-files

```bash
cd reader
zip -r ../reader.zip *

cd ..
python reader.zip some_file
```

## Recommended Project Structure

```
project_name/
    __main__.py
    project_name/
        __init__.py
        more_source.py
        subpackage1/
            __init__.py
        test/
            __init__.py
            test_code.py
    setup.py
```

## Modules as Singeltons

```python
# registry.py
_registry = []


def register(name):
    _registry.append(name)


def registered_names():
    return iter(_registry)
```

```python
import registry

registry.register('my_name')
for name in registry.registered_names():
    print(name)
```
