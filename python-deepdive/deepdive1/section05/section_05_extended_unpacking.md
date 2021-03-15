# Extended Unpacking

## \* Unpacking

- simple unpacking using slices: a, b = l\[0\], l\[1:\]
- unpacking to LHS with \*: a,\*b = l
- remainder of a \* unpacking is a list
- unpacking on RHS with \*: l = \[\*l1, \*l2\]

## \*\* Unpacking

- \*\* can be used to unpack key/value pairs but only on the RHS

## Nested Unpacking

- a, b, (c, d) = \[1, 2, \[3, 4\]\]

## Code Examples


```python
l = [1, 2, 3, 4, 5, 6]
```


```python
# Slicing
a = l[0]
b = l[1:]
```


```python
a, b
```




    (1, [2, 3, 4, 5, 6])




```python
a, b = l[0], l[1:]
```


```python
a, b
```




    (1, [2, 3, 4, 5, 6])




```python
a, *b = l
```


```python
a, b
```




    (1, [2, 3, 4, 5, 6])




```python
s = "python"
```


```python
a, *b = s
```


```python
a, b
```




    ('p', ['y', 't', 'h', 'o', 'n'])




```python
t = "a", "b", "c"
```


```python
a, *b = t
```


```python
a, b
```




    ('a', ['b', 'c'])




```python
a, b, *c, d = s
```


```python
a, b, c, d
```




    ('p', 'y', ['t', 'h', 'o'], 'n')




```python
# Merging lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
```


```python
l
```




    [1, 2, 3, 4, 5, 6]




```python
s1 = "abc"
s2 = "cde"
```


```python
[*s1, *s2]
```




    ['a', 'b', 'c', 'c', 'd', 'e']




```python
s = {*s1, *s2}
```


```python
s
```




    {'a', 'b', 'c', 'd', 'e'}




```python
# converting to a list
l = list(s)
```


```python
l
```




    ['e', 'b', 'c', 'a', 'd']




```python
*l, = s
```


```python
l
```




    ['e', 'b', 'c', 'a', 'd']




```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
```


```python
# union
s1.union(s2).union(s3).union(s4)
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9}




```python
s1.union(s2, s3, s4)
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9}




```python
{*s1, *s2, *s3, *s4}
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9}




```python
d1 = {"key1": 1, "key2": 2}
d2 = {"key2": 3, "key4": 4}
```


```python
# Union of unpacked keys
{*d1, *d2}
```




    {'key1', 'key2', 'key4'}




```python
# Union of unpacked key/value pairs
{**d1, **d2}
```




    {'key1': 1, 'key2': 3, 'key4': 4}




```python
# RHS unpacking of key/value pairs
{"a": 1, "b": 2, **d1, "c":3}
```




    {'a': 1, 'b': 2, 'key1': 1, 'key2': 2, 'c': 3}




```python
# nested unpacking
a, b, e = [1, 2, "xy"]
```


```python
a, b, e
```




    (1, 2, 'xy')




```python
c, d = e
```


```python
c, d
```




    ('x', 'y')




```python
a, b, (c, d) = [1, 2, "xy"]
```


```python
l = [1, 2, 3, 4, "python"]
```


```python
a, *b, (c, d, *e) = l
```


```python
a, b, c, d, e
```




    (1, [2, 3, 4], 'p', 'y', ['t', 'h', 'o', 'n'])


