# Object Mutability

Object is made up:

- Type
- State(data)

changing the object data is called modifying the internal state of the,
object (aka mutated)

Mutable object

- an object whose internal state can be changed

Immutable object

- an object whose internal state cannot be changed

| Immutable | Mutable |
| --- | --- |
| Numbers (int, float, bool, etc) | Lists |
| Strings | Sets |
| Tuples | Dictionaries |
| Frozen Sets | User-Defined Classes |


```python
# Tuples are immutable, elements cannot be deleted, inserted, or replaced
# In this example, both the container(tuple) and elements(ints) are immutable
t = (1, 2, 3)
```


```python
# Lists are mutable
a = [1, 2]
b = [3, 4]
t = (a, b)
```


```python
print(t)
hex(id(t))
```

    ([1, 2, 3], [3, 4, 5])





    '0x7f381c388640'




```python
# Adding elements to the lists
# Tuple has not changed
a.append(3)
b.append(5)
```


```python
print(t)
hex(id(t))
```

    ([1, 2, 3], [3, 4, 5])





    '0x7f381c388640'



Objects may be immutable, the object references may not change but the the referenced mutable objects can mutate.

# Example of a mutable object

- memory address does not change


```python
my_list = [1, 2, 3]
```


```python
type(my_list)
```




    list




```python
my_list
```




    [1, 2, 3]




```python
hex(id(my_list))
```




    '0x7f381c3e0a80'




```python
my_list.append(4)
```


```python
my_list
```




    [1, 2, 3, 4]




```python
hex(id(my_list))
```




    '0x7f381c3e0a80'



# Example of mutable object when concatenating lists

- the address will change because its assigning a new list


```python
my_list_1 = [1, 2, 3]
```


```python
hex(id(my_list_1))
```




    '0x7f381c3a4e80'




```python
my_list_1 = my_list_1 + [4]
```


```python
my_list_1
```




    [1, 2, 3, 4, 4]




```python
hex(id(my_list_1))
```




    '0x7f381c3a4800'


