# Python Optimizations - String Interning

Some strings are interned but don't count on it.

Identifiers are interned:

- variable names
- function names
- class names
- etc.

Some string literals may be automatically interned:

- string literals that look like identifiers (variable naming rules)
- starts with a digit

Interning is about (speed, and possibly memory) optimization.  

Not all strings are interned but you can force strings to be interned by using the sys.intern() method.

When should you do this?

- repetive string comparisons where strings hardly changes
- lots of string comparisons


```python
a = "hello"
b = "hello"
```


```python
a is b
```




    True




```python
a = "hello world"
b = "hello world"
```


```python
a is b
```




    False




```python
a = "_this_is_a_string_that_follows_rules_for_variable_naming"
b = "_this_is_a_string_that_follows_rules_for_variable_naming"
```


```python
a is b
```




    True



# Interning example


```python
import sys
```


```python
a = sys.intern("Hello World")
b = sys.intern("Hello World")
c = "Hello World"
```


```python
a is b # Interned strings
```




    True




```python
a is c # c was not interned
```




    False




```python
a == c # comparing strings character by character
```




    True



# Example comparing non-interned vs interned


```python
def compare_using_equals(n):
    a = "a long string that is not interned" * 200
    b = "a long string that is not interned" * 200
    
    for i in range(n):
        if a == b:
            pass
```


```python
def compare_using_interning(n):
    a = sys.intern("a long string that is not interned" * 200)
    b = sys.intern("a long string that is not interned" * 200)
    
    for i in range(n):
        if a is b:
            pass
```


```python
import time
```


```python
start = time.perf_counter()
compare_using_equals(10_000_000)
end = time.perf_counter()
f"Equality: {end - start}"
```




    'Equality: 3.8765763060655445'




```python
start = time.perf_counter()
compare_using_interning(10_000_000)
end = time.perf_counter()
f"Interning: {end - start}"
```




    'Interning: 0.6557386880740523'


