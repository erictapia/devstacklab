# Variable Re-Assignment

- the assignment does not change the value
- it creates a new reference
- variable points to a new memory location


```python
a = 10
```


```python
hex(id(a))
```




    '0x954f40'




```python
type(a)
```




    int




```python
a = 15
```


```python
hex(id(a))
```




    '0x954fe0'




```python
a = a + 1
```


```python
a
```




    16




```python
hex(id(a))
```




    '0x955000'


