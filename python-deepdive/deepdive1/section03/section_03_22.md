# Shared References and Mutability

shared reference: two variables referencing the same object in memory
(same memory address)

The Python memory manager may create a shared reference on immutable objects
such as:


```python
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



The variables, a and b, will point to same memory location (Python internals).

The Python memory manager will not create a shared reference on mutable objects,
each will point to its own object in memory.


```python
a = [10]
b = [10]
```


```python
id(a)
```




    139821401524288




```python
id(b)
```




    139821401531392


