# Putting it all Together

## Code Examples


```python
def func1(a, b, * args):
    print(a, b, args)
```


```python
func1(1, 2, "X", "Y", "z")
```

    1 2 ('X', 'Y', 'z')



```python
def func1(a, b=2, c=3, *args):
    print(a, b, c, args)
```


```python
func1(1, 2, 3,"x", "y", "z")
```

    1 2 3 ('x', 'y', 'z')



```python
func1(1, c=4)
```

    1 2 4 ()



```python
# once you use keyword arguments, all following arguments must too
# can't use the *args in function
func1(1, c=4, 5, 6, 7)
```


      File "<ipython-input-9-d2ae9d70ad3a>", line 3
        func1(1, c=4, 5, 6, 7)
                      ^
    SyntaxError: positional argument follows keyword argument




```python
# add *args after a parameter with a default will make the
# default value unusable
def func1(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)
```


```python
func1(10, 20, "X", "y", "z", c=4, d=1)
```

    10 20 ('X', 'y', 'z') 4 1



```python
# using c default
func1(10, 20, "X", "y", "z", d=1)
```

    10 20 ('X', 'y', 'z') 3 1



```python
# can't use b default value
func1(10, "X", "y", "z", c=4, d=1)
```

    10 X ('y', 'z') 4 1



```python
def func1(a, b, *args, c=10, d=20, **kwargs):
    print(a, b, args, c, d, kwargs)
```


```python
func1(1, 2, 3, 4, 5, c=100, d=200, x=0.1, y=0.2)
```

    1 2 (3, 4, 5) 100 200 {'x': 0.1, 'y': 0.2}



```python
def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    
    avg = (hi + lo) / 2
    
    if log_to_console:
        print(f"high:{hi}, low:{lo}, avg: {avg}")
    
    return avg
```


```python
avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=True)
```

    high:5, low:1, avg: 3.0



```python
avg
```




    3.0


