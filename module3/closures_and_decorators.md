# Closures and Decorators

## Local Function

  - New local function is created each time it's parent function is called

## Global and Local Variables

  - `global` to redefine global variables
  - `nonlocal` to redefine variables in the enclosing scope (will raise
    `SyntaxError` if there is not such variable in the enclosing scope)

## `functools.wraps()`

Updates wrapped functions metadata

```python
def hello():
    print('Hello world!')

print(hello.__name__)
# hello

def noop(func):
    def noop_wrapper():
        return func()
    return noop_wrapper

@noop
def hello2():
    print('Hello world!')

print(hello2.__name__)
# noop_wrapper

import functools

def noop(func):
    @functools.wraps(func)
    def noop_wrapper():
        return func()
    return noop_wrapper

@noop
def hello3():
    print('Hello world!')

print(hello3.__name__)
# hello3
```
