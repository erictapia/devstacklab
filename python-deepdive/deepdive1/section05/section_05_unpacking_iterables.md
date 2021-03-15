# Unpacking Iterables

## Packed Values

- values that are bundled together is some way
- types that are packed: tuples, lists, strings, set, dictionary, any iterable

## Unpacking Packed Values

- the act of splitting packed values into individual variables
- unpacking dictionaries returns keys

## Code Examples

### Packing


```python
a = (1, 2, 3)
```


```python
type(a)
```




    tuple




```python
a = 1, 2, 3
```


```python
type(a)
```




    tuple




```python
a
```




    (1, 2, 3)



## Unpacking


```python
a, b, c = [1, "a", 3.14]
```


```python
a, b, c
```




    (1, 'a', 3.14)




```python
a,b, c = "XYZ"
```


```python
a, b, c
```




    ('X', 'Y', 'Z')




```python
s = {1, 2, 3}
```


```python
a, b, c = s
```


```python
a, b, c
```




    (1, 2, 3)




```python
d = {"a": 1, "b": 2, "c": 3}
```


```python
# Unpacking keys
a, b, c = d
```


```python
a, b, c
```




    ('a', 'b', 'c')




```python
# Unpacking values
a, b, c = d.values()
```


```python
a, b, c
```




    (1, 2, 3)




```python
# Unpacking keys and values
a, b, c = d.items()
```


```python
a, b, c
```




    (('a', 1), ('b', 2), ('c', 3))


