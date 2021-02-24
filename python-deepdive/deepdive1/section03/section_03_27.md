# Python Optimizations: Peephole

- another variety of optimizations occuring at compile time

Peephole optimizations

- constant expressions: numeric calculations  24 * 60 --> 1440
- short sequences length: (1, 2) * 3  --> (1, 2, 1, 2, 1, 2), strings up to 20 characters
- membership tests: if e in list, list --> tuple; sets --> frozensets


```python
def my_func():
    a= 24 * 60
    b = (1, 2) * 5
    c = "abc" * 3
    d = "ab" * 11
    e = "The quick brown fox" * 5
    f = ["a", "b"] * 3
```

# Looking at function constants


```python
my_func.__code__.co_consts
```




    (None,
     1440,
     (1, 2, 1, 2, 1, 2, 1, 2, 1, 2),
     'abcabcabc',
     'ababababababababababab',
     'The quick brown foxThe quick brown foxThe quick brown foxThe quick brown foxThe quick brown fox',
     'a',
     'b',
     3)



# Looking at function membership test constants


```python
def my_func(e):
    if e in [1, 2, 3]:  # peephole optimization: list to tuple
        pass
```


```python
my_func.__code__.co_consts
```




    (None, (1, 2, 3))



# Membership comparison


```python
import string
import time
```


```python
string.ascii_letters
```




    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'




```python
char_list = list(string.ascii_letters)
```


```python
char_tuple = tuple(string.ascii_letters)
```


```python
char_set = set(string.ascii_letters)
```


```python
print(char_list)
```

    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



```python
print(char_tuple)
```

    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')



```python
print(char_set) # unordered
```

    {'Z', 'i', 't', 'T', 'y', 'g', 'a', 'G', 'e', 'M', 'm', 'j', 'n', 'A', 'F', 'r', 'p', 'R', 'H', 'P', 'V', 'c', 'h', 'W', 'X', 'B', 'O', 'I', 'L', 'z', 'o', 'U', 's', 'u', 'q', 'd', 'b', 'J', 'x', 'Y', 'w', 'C', 'k', 'N', 'E', 'Q', 'K', 'D', 'v', 'l', 'S', 'f'}



```python
def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass
```


```python
start = time.perf_counter()
membership_test(10_000_000, char_list)
end = time.perf_counter()
print("list: ", end - start)
```

    list:  6.183510106056929



```python
start = time.perf_counter()
membership_test(10_000_000, char_tuple)
end = time.perf_counter()
print("tuple: ", end - start)
```

    tuple:  5.429904733086005



```python
start = time.perf_counter()
membership_test(10_000_000, char_set)
end = time.perf_counter()
print("set: ", end - start)
```

    set:  0.7203901440370828

