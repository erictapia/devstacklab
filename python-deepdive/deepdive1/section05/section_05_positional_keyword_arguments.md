# Positional and Keyword Arguments

## Positional Arguments

- assigning arguments to parameters via the order(position) in which they are passed
- a positional arguments can be made optional by specifying a default value
- once a defaul value is used, all parameters follwing that one must have a default value

## Keyword Arguments

- uses the name of the parameter in the argument
- can be mixed with positional and keyword arguments
- once a keyword arugment is used, all arguments after that have to use keyword arguments
- parameters with default values can be omitted

## Code Examples

### Positional Arguments:


```python
def my_func(a, b, c):
    print(f"a={a}, b={b}, c={c}")
```


```python
# Positional arguments
my_func(1, 2, 3)
```

    a=1, b=2, c=3



```python
# Missing 1 positional argument
my_func(1, 2)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-409cde905e71> in <module>
          1 # Missing 1 positional argument
    ----> 2 my_func(1, 2)
    

    TypeError: my_func() missing 1 required positional argument: 'c'



```python
def my_func(a=1, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")
```


```python
my_func(10, 20, 30)
```

    a=10, b=20, c=30



```python
my_func(10, 20)
```

    a=10, b=20, c=3



```python
my_func(10)
```

    a=10, b=2, c=3



```python
my_func()
```

    a=1, b=2, c=3


### Keyword Arguments


```python
def my_func(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")
```


```python
# order is not relevant
my_func(c=30, b=20, a=10)
```

    a=10, b=20, c=30



```python
my_func(10, c=30, b=20)
```

    a=10, b=20, c=30



```python
my_func(10, c=30)
```

    a=10, b=2, c=30

