# \*args

- \* can be used on a function definition, result is a tuple
- customary to name it \*args
- no positional arguments can be added after the \*args

## Code Examples


```python
def func1(a, b, *c):
    print(a, b, c)
```


```python
func1(10, 20)
```

    10 20 ()



```python
func1(10, 20, 1, 2, 3)
```

    10 20 (1, 2, 3)



```python
def avg(*args):
    print(args)
```


```python
avg()
```

    ()



```python
avg(10, 20)
```

    (10, 20)



```python
def avg(*args):
    count = len(args)
    total= sum(args)
    # short circuit to avoid division by 0
    return count and total/count
```


```python
avg(2, 2, 4, 4)
```




    3.0




```python
avg()
```




    0




```python
# Enforcing at least one argument
def avg(a, *args):
    count = len(args) + 1
    total= sum(args) + a
    # short circuit to avoid division by 0
    return count and total/count
```


```python
avg(2, 2, 4, 4)
```




    3.0




```python
# TypeError because it is missing a positional argument
avg()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-21-94a565368bbb> in <module>
          1 # TypeError because it is missing a positional argument
    ----> 2 avg()
    

    TypeError: avg() missing 1 required positional argument: 'a'



```python
def funct1(a, b, c):
    print(a, b, c)
```


```python
l = [10, 20, 30]
```


```python
# without unpacking, TypeError
funct1(l)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-24-6ca352dc4bcc> in <module>
          1 # without unpacking, TypeError
    ----> 2 funct1(l)
    

    TypeError: funct1() missing 2 required positional arguments: 'b' and 'c'



```python
funct1(*l)
```

    10 20 30



```python
def funct1(a, b, c, *args):
    print(a, b, c, args)
```


```python
l = [1, 2, 3, 4, 5, 6, 7]
```


```python
funct1(*l)
```

    1 2 3 (4, 5, 6, 7)

