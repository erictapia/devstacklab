# \*\*kwargs

- holds a variable amount of remaining keyword arguments
- data type: dictionary
- no parameters can be defined after the \*\*kwargs

## Code Examples


```python
def func1(**kwargs):
    print(kwargs)
```


```python
func1(a=1, b=2, c=3)
```

    {'a': 1, 'b': 2, 'c': 3}



```python
def func1(*args, **kwargs):
    print(args, kwargs)
```


```python
func1(1, 2, x=100, y=200)
```

    (1, 2) {'x': 100, 'y': 200}



```python
def func1(a, b, *, d, **kwargs):
    print(a, b, d, kwargs)
```


```python
func1(1, 2, x=100, y=200, d=20)
```

    1 2 20 {'x': 100, 'y': 200}



```python
def func1(a, b, **kwargs):
    print(a, b, kwargs)
```


```python
func1(1, 2, x=100, y=200)
```

    1 2 {'x': 100, 'y': 200}

