# Function Arguments and Mutability

- Immutable objects are safe from unintended side-effects
- Immutable objects that contain mutable objects are not safe from unintended side-effects
- Mutable objects are not safe from unintended side-effects

# Example of value not changing when modifying an immutable object from a passed argument


```python
def process(s):
    print(f"Initial s # = {id(s)}")
    s = s + " world"
    print(f"Final s # = {id(s)}")
```


```python
my_var = "hello"
print(f"my_var # = {id(my_var)}")
```

    my_var # = 140446981035376



```python
process(my_var)
```

    Initial s # = 140446981035376
    Final s # = 140446981040048



```python
print(f"my_var # = {id(my_var)}")
```

    my_var # = 140446981035376


# Example of address not changing when modifying immutable object from a passed argument, but value does change


```python
def modify_list(lst):
    print(f"Initial lst # = {id(lst)}")
    lst.append(100)
    print(f"Final lst # = {id(lst)}")
```


```python
my_list = [1, 2, 3]
print(f"my_list # = {id(my_list)}")
```

    my_list # = 140446981105984



```python
modify_list(my_list)
```

    Initial lst # = 140446981105984
    Final lst # = 140446981105984



```python
print(f"my_list # = {id(my_list)}")
```

    my_list # = 140446981105984


# Example of side effects, immutable object data changes


```python
def modify_tuple(t):
    print(f"Initial t # = {id(t)}")
    t[0].append(100)
    print(f"Final t # = {id(t)}")
```


```python
my_tuple = ([1, 2], "a")
print(f"my_tuple # = {id(my_tuple)}")
```

    my_tuple # = 140447049035584



```python
modify_tuple(my_tuple)
```

    Initial t # = 140447049035584
    Final t # = 140447049035584



```python
print(f"my_tuple # = {id(my_tuple)}")
```

    my_tuple # = 140447049035584

