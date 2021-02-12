# For loop


In Python, an iterable is an object capable of returning values one at a time


```python
i = 0

while i < 5:
    print(i)
    i += 1

i = None
```

    0
    1
    2
    3
    4



```python
# range(5) is an iterable object
# on each loop, the object returns the next value and is assigned to i
for i in range(5):
    print(i)

```

    0
    1
    2
    3
    4



```python
for i in [1, 2, 3, 4]:
    print(i)

```

    1
    2
    3
    4



```python
for c in "hello":
    print(c)

```

    h
    e
    l
    l
    o



```python
for x in ("a", "b", "c", 4):
    print(x)

```

    a
    b
    c
    4



```python
for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)

```

    (1, 2)
    (3, 4)
    (5, 6)



```python
# unpacking the tuple
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

```

    1 2
    3 4
    5 6



```python
for i in range(5):
    if i == 3:
        continue
    
    print(i)

```

    0
    1
    2
    4



```python
for i in range(5):
    if i == 3:
        break
    
    print(i)

```

    0
    1
    2



```python
for i in range(1, 4):
    print(i)
    
    if i % 7 == 0:
        print("multiple of 7 found")
        break
else:
    print("no multiples of 7 found in the range")

```

    1
    2
    3
    no multiples of 7 found in the range



```python
for i in range(1, 8):
    print(i)
    
    if i % 7 == 0:
        print("multiple of 7 found")
        break
else:
    print("no multiples of 7 found in the range")
```

    1
    2
    3
    4
    5
    6
    7
    multiple of 7 found



```python
for i in range(5):
    print("-" * 25)
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print("divided by 0")
        continue
    finally:
        print("always run")
    
    print(i)

```

    -------------------------
    always run
    0
    -------------------------
    always run
    1
    -------------------------
    always run
    2
    -------------------------
    divided by 0
    always run
    -------------------------
    always run
    4



```python
# Standard for loop
s = "hello"

for c in s:
    print(c)

```

    h
    e
    l
    l
    o



```python
# For loop indexing
s = "hello"
i = 0

for c in s:
    print(i, c)
    i += 1

```

    0 h
    1 e
    2 l
    3 l
    4 o



```python
# For loop indexing
s = "hello"

for i in range(len(s)):
    print(i, s[i])

```

    0 h
    1 e
    2 l
    3 l
    4 o



```python
# For loop indexing via enumerate
s = "hello"

for i, c in enumerate(s):
    print(i, c)

```

    0 h
    1 e
    2 l
    3 l
    4 o

