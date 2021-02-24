# Python Optimizations: Interning

- reusing objects on-demand
- pre-loads a global list of integers in the range -5 - 256
- integer in the range will use a cached version (singleton) of the object


```python
a = 10
b = 10
```


```python
a is b
```




    True




```python
a = -5
b = -5
```


```python
a is b
```




    True




```python
a = 257
b = 257
```


```python
a is b
```




    False




```python
a = 256
b = 256
```


```python
a is b
```




    True


