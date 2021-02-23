# Reference Counting

When variables are created, Python maintains a reference count.  It uses this non-zero count to know if the memory location is being used.

Getting reference count

- sys.getrefcount(variable) <-- this also creates an extra count
- ctypes.c_long.from_address(address).value <-- address is an integer so it does not affect teh reference count


```python
import sys
```


```python
a = [1, 2, 3]

```


```python
id(a)
```




    139808100278976




```python
sys.getrefcount(a)
```




    2




```python
import ctypes
```


```python
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value
```


```python
ref_count(id(a))
```




    1




```python
b = a
```


```python
id(b)
```




    139808100278976




```python
ref_count(id(a))
```




    2




```python
c = a
ref_count(id(a))
```




    3




```python
c = 10
ref_count(id(a))
```




    2




```python
b = None
```


```python
ref_count(id(a))
```




    1




```python
a_id = id(a)
a = None
ref_count(a_id)
```




    1




```python
# After references is 0, Python is free to reuse the memory location for other
# objects
ref_count(a_id)
```




    2


