# Break, Continue and the Try Statement

- finally will execute even if there is a continue or break


```python
a = 10
b = 0

try:
    a/b
except ZeroDivisionError:
    print("Division by 0")
finally:
    print("this always executes")
```

    Division by 0
    this always executes



```python
a = 0
b = 2

while a < 4:
    print("-" * 25)
    a += 1
    b -= 1
    
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - Division by 0".format(a, b))
        continue
    finally:
        print("{0}, {1} - always executes".format(a, b))
    
    print("{0}, {1} - main loop".format(a, b))
```

    -------------------------
    1, 1 - always executes
    1, 1 - main loop
    -------------------------
    2, 0 - Division by 0
    2, 0 - always executes
    -------------------------
    3, -1 - always executes
    3, -1 - main loop
    -------------------------
    4, -2 - always executes
    4, -2 - main loop



```python
a = 0
b = 2

while a < 4:
    print("-" * 25)
    a += 1
    b -= 1
    
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - Division by 0".format(a, b))
        break
    finally:
        print("{0}, {1} - always executes".format(a, b))
    
    print("{0}, {1} - main loop".format(a, b))
```

    -------------------------
    1, 1 - always executes
    1, 1 - main loop
    -------------------------
    2, 0 - Division by 0
    2, 0 - always executes



```python
a = 0
b = 2

while a < 4:
    print("-" * 25)
    a += 1
    b -= 1
    
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - Division by 0".format(a, b))
        break
    finally:
        print("{0}, {1} - always executes".format(a, b))
    
    print("{0}, {1} - main loop".format(a, b))
else:
    # Due to break, this will not execute
    print("Code executed without a zero division error")
```

    -------------------------
    1, 1 - always executes
    1, 1 - main loop
    -------------------------
    2, 0 - Division by 0
    2, 0 - always executes



```python
a = 0
b = 10

while a < 4:
    print("-" * 25)
    a += 1
    b -= 1
    
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - Division by 0".format(a, b))
        break
    finally:
        print("{0}, {1} - always executes".format(a, b))
    
    print("{0}, {1} - main loop".format(a, b))
else:
    # Will execute becasue while loop will terminate and not execute break
    # statement
    print("Code executed without a zero division error")
```

    -------------------------
    1, 9 - always executes
    1, 9 - main loop
    -------------------------
    2, 8 - always executes
    2, 8 - main loop
    -------------------------
    3, 7 - always executes
    3, 7 - main loop
    -------------------------
    4, 6 - always executes
    4, 6 - main loop
    Code executed without a zero division error

