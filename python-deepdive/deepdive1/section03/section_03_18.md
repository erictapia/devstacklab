# Dynamic vs Static Typing

Static typing languages do no allow variables to change the type of value being assigned

- c
- c++
- java

Dynamic typing languages can be assigned any type of value

- python

# type function

- a built-in function to determine the type of the object referenced by a variable


```python
a = "hello"
```


```python
type(a)
```




    str




```python
a = 10
```


```python
type(a)
```




    int




```python
a = lambda x: x**2
```


```python
type(a)
```




    function




```python
a = 3 + 4j
```


```python
type(a)
```




    complex


