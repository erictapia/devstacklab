# Everything is an Object

Everything is an object, an instance of a class.  This includes the following:

Data types

- integers (int)
- booleans (bool)
- floats (float)
- strings (str)
- lists (list)
- tuples (tuple)
- sets (set)
- dictionaries (dict)
- None (NoneType)

other constructs

- Operators (+, -, ==, is, ...)
- Functions
- Classes
- Types
- and many more ...


All of them have a memory address.

As a consequence:

- any object can be assigned to a variable
- any object can be passed to a function
- any object can be returned from a function


```python
a = 10
```


```python
type(a)
```




    int




```python
b = int(10)
```


```python
b
```




    10




```python
type(b)
```




    int




```python
c = int()
```


```python
c
```




    0




```python
c = int('101', base=2)
```


```python
c
```




    5



# Functions are objects too


```python
def square(a):
    return a ** 2
```


```python
type(square)
```




    function




```python
f = square
```


```python
id(f)
```




    140157071634784




```python
f is square
```




    True




```python
square(2)
```




    4




```python
f(2)
```




    4




```python
def cube(a):
    return a ** 3
```


```python
def select_function(fn_id):
    if fn_id == 1:
        return square
    
    return cube
```


```python
f = select_function(1)
```


```python
f is square
```




    True




```python
f(2)
```




    4




```python
f = select_function(2)
```


```python
f(2)
```




    8




```python
def exec_function(fn, n):
    return fn(n)
```


```python
exec_function(cube, 3)
```




    27


