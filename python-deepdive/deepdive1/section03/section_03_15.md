# Variables are Memory References


# Heap

| Memory Address | Object at Memory Address |
| --- | --- |
| 0x1000 | Object1 |
| 0x1001 | Object1 |
| 0x1002 | Object2 |
| 0x1003 | Object2 |
| 0x1004 | Object2 |
| 0x1005 | Object3 |
| ... | |



```python
# my_var is a reference to a memory address
my_var = 10

print(my_var)
```

    10



```python
# id outputs the memory address referenced by my_var
print(id(my_var))
```

    9785152



```python
# Hex version of ID
print(hex(id(my_var)))
```

    0x954f40

