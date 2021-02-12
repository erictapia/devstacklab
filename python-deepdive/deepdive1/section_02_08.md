# Conditionals



```python
a = 6

if a < 5:
    print("a < 5")
else:
    print("a >= 5")
```

    a >= 5



```python
a = 5

if a < 5:
    print("a < 5")
else:
    if a < 10:
        print("5 <= a < 10")
    else:
        print("a >= 10")
```

    5 <= a < 10


# else if conditionals


```python
a = 5

if a < 5:
    print("a < 5")
elif a < 10:
    print("5 <= a < 10")
elif a < 15:
    print("10 <= a < 15")
elif a < 20:
    print("15 <= a < 20")
else:
    print("a > 20")
```

    5 <= a < 10


# Non Ternary operator


```python
a = 25

if a < 5:
    b = "a < 5"
else:
    b = "a >= 5"

print(b)
```

    a >= 5


# Ternary operator


```python
a = 25

b = "a < 5" if a < 5 else "a >= 5"

print(b)
```

    a >= 5

