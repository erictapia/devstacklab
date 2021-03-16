# Keyword Arguments

- parameters following a \*args will become a mandatory keyword argument
- \* can be used to end positional arguments
- \*: Python will raise a TypeError when positional arguments are passed

## Code Examples


```python
def func1(a, b, c):
    print(a, b, c)
```


```python
func1(1, 2, 3)
```

    1 2 3



```python
func1(1, c=3, b=2)
```

    1 2 3



```python
func1(c=3, b=2, a=1)
```

    1 2 3



```python
def func1(a, b, *args):
    print(a, b, args)
```


```python
func1(1, 2, 3, 4)
```

    1 2 (3, 4)



```python
# d is a mandatory keyword argument
def func1(a, b, *args, d):
    print(a, b, args, d)
```


```python
# Fails because d must be a keyword argument
func1(1, 2, 3, 4, 5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-db9b4eaca7c8> in <module>
          1 # Fails because d must be a keyword argument
    ----> 2 func1(1, 2, 3, 4, 5)
    

    TypeError: func1() missing 1 required keyword-only argument: 'd'



```python
func1(1, 2, 3, 4, d=5)
```

    1 2 (3, 4) 5



```python
def func1(*args,d):
    print(args, d)
```


```python
func1(1, 2, 3, d=4)
```

    (1, 2, 3) 4



```python
func1(d=1)
```

    () 1



```python
# No positional arguments allowed
def func(*, d):
    print(d)
```


```python
func(1, 2, d=100)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-16-e590558e6857> in <module>
    ----> 1 func(1, 2, d=100)
    

    TypeError: func() takes 0 positional arguments but 2 positional arguments (and 1 keyword-only argument) were given



```python
func1(d=100)
```

    () 100



```python
def func1(a, b, *, d):
    print(a, b, d)
```


```python
func1(1, 2, d=4)
```

    1 2 4



```python
# passing a 3rd positional argument will throw an exception
func1(1, 2, 3, d=4)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-f6d4f36d8dbc> in <module>
          1 # passing a 3rd positional argument will throw an exception
    ----> 2 func1(1, 2, 3, d=4)
    

    TypeError: func1() takes 2 positional arguments but 3 positional arguments (and 1 keyword-only argument) were given



```python
def func1(a, b=2, *args, d):
    print(a, b, args, d)
```


```python
func1(1,5, 3, 4, d="A")
```

    1 5 (3, 4) A



```python
# d, e are mandatory keyword arguments
# since any parameter after args is mandatory,
# the parameters do not all have a default
def func1(a, b=20, *args, d=0, e):
    print(a, b, args, d, e)
```


```python
func1(5, 4, 3,2,1, e="a")
```

    5 4 (3, 2, 1) 0 a



```python
func1(0,600, d=1, e=2)
```

    0 600 () 1 2

