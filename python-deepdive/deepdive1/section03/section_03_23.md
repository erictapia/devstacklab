# Variable Equality

Two fundamental ways:

| Memory Address | Object State (data) |
| --- | --- |
| is (identity operator) | == (equality operator) |

Negation

| Memory Address | Object State (data) |
| --- | --- |
| is not | != |

# None object

- this object can be assigned to variables to indicate that it is not set
- a real object managed by the Python memory manager
- always uses a shared reference

# Variables using shared reference


```python
# shared reference via Python memory manager
a = 10
b = 10
```


```python
id(a)
```




    9785152




```python
id(b)
```




    9785152




```python
print("a is b", a is b)
```

    a is b True



```python
print("a == b", a == b)
```

    a == b True


# Variables referencing different memory address


```python
a = 500
b = 500
```


```python
id(a)
```




    140247333037360




```python
id(b)
```




    140247333038672




```python
print("a is b", a is b)
```

    a is b False



```python
print("a == b", a == b)
```

    a == b True


# Examples with None object


```python
id(None)
```




    9480688




```python
a = None
b = None
c = None
```


```python
 a is b
```




    True




```python
a is c
```




    True




```python
a is None
```




    True


