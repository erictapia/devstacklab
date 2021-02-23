# While Loop


```python
i = 0

while i < 5:
    print(i)
    i += 1

```

    0
    1
    2
    3
    4


# While loop that runs at least one time using break

- breaks out of the while loop


```python
i = 5

while True:
    print(i)
    
    if i >= 5:
        break
```

    5



```python
min_length = 2
name = input("Please enter your name: ")

while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name: ")

print("Hello, {0}".format(name))
```

    Please enter your name:  a
    Please enter your name:  12
    Please enter your name:  Eric


    Hello, Eric



```python
min_length = 2

while True:
    name = input("Please enter your name: ")
    
    if (len(name) >= min_length and name.isprintable() and name.isalpha()):
        break  

print("Hello, {0}".format(name))
```

    Please enter your name:  a
    Please enter your name:  12
    Please enter your name:  Eric


    Hello, Eric


# Continue statement

- Skips everything after the statement


```python
a = 0

while a < 10:
    a += 1
    
    if a % 2 == 0:
        continue
    
    print(a)
```

    1
    3
    5
    7
    9


# While with a Else clause

- else will execute if, and only if, the loop executes to termination (no break).


```python
l = [1, 2, 3]

val = 10

found = False
idx = 0

while idx < len(l):
    if l[idx] == val:
        found = True
        break
    
    idx += 1

if not found:
    l.append(val)

print(l)
    
```

    [1, 2, 3, 10]



```python
# rewrite using else clause
l = [1, 2, 3]
val = 10
idx = 0

while idx < len(l):
    if l[idx] == val:
        break
    
    idx += 1

else:  # executes only if the while didn't use the break statement
    l.append(val)

print(l)
```

    [1, 2, 3, 10]

