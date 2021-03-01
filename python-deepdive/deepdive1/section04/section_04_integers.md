# Integers: Data Types

int - ex: 0, 10, -100, ...

- are represented internally using base-2
- the number of bits determines the value range
- uses a variable number of bits so an integer can be as large as the memory allows
- the larger the number, the slower operations run


```python
type(100)
```




    int




```python
import sys
```

The overhead of storing an integer in bytes


```python
sys.getsizeof(0)
```




    24




```python
sys.getsizeof(1)
```




    28




```python
sys.getsizeof(2**1000)
```




    160




```python
# Number of bits
(160 - 24) * 8
```




    1088



Operation is slower as the integer value increases


```python
import time
```


```python
def calc(a):
    start = time.perf_counter()
    
    for i in range(10_000_000):
        a * 2
    
    end = time.perf_counter()
    print(end - start)
```


```python
calc(10)
```

    0.7362740719690919



```python
calc(2 ** 100)
```

    1.1699034557677805



```python
calc( 2 ** 10_000)
```

    6.508364222943783


# Integers: Operations

Standard arithmetic operations

| Operation Name | Operator | Example | Result Type |
| --- | --- | --- | --- |
| addition | + | int + int | int |
| subtraction | - | int - int | int |
| multiplication | * | int * int | int |
| division | / | int / int | float |
| exponents | ** | int ** int | int |
| floor division | // | int // int | int |
| modulo | % | int % int | int |

floor of a real number is the largest integer <= than the real number.
Ex.: 
- floor(33.75) --> 33
- floor(-33.75)--> -34



```python
type(1 + 1)
```




    int




```python
type(2 * 3)
```




    int




```python
type(4 - 10)
```




    int




```python
type(3 ** 6)
```




    int




```python
type(2 / 3)
```




    float




```python
# Even divisible is still a float
type(10 / 5)
```




    float




```python
10/5
```




    2.0



# Floor


```python
import math
```


```python
math.floor(3.15)
```




    3




```python
math.floor(-3.15)
```




    -4



Floor has a limited precision


```python
math.floor(-3.000000000000001)
```




    -4




```python
math.floor(-3.0000000000000001)
```




    -3




```python
a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
```

    2.0625
    2
    2



```python
a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
```

    -2.0625
    -3
    -3



```python
a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
print(math.trunc(a/b))
```

    -2.0625
    -3
    -3
    -2


a: dividend

b: divsor

a // b: quotient

a % b: remainder

a = b * (a // b) + (a % b)


```python
a = 13
b = 4
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")

print( a == b * (a // b) + (a % b))
```

    13 / 4 = 3.25
    13 // 4 = 3
    13 % 4 = 1
    True



```python
a = -13
b = 4
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")

print( a == b * (a // b) + (a % b))
```

    -13 / 4 = -3.25
    -13 // 4 = -4
    -13 % 4 = 3
    True



```python
a = 13
b = -4
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")

print( a == b * (a // b) + (a % b))
```

    13 / -4 = -3.25
    13 // -4 = -4
    13 % -4 = -3
    True



```python
a = -13
b = -4
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")

print( a == b * (a // b) + (a % b))
```

    -13 / -4 = 3.25
    -13 // -4 = 3
    -13 % -4 = -1
    True


# Integers: Constructors and Bases

- is an object, instance of the int clas
- provides multiple constructors
- a constructor with a single numerical parameter
- a constructor with a string and a second optional parameter

Supported arguments of the int constructor

| Type | Example | Result |
| --- | --- | --- |
| float | int(10.9) | 10 - uses truncation |
| -float | int(-10.9) | -10 - uses truncation |
| bool | int(True) | 1 |
| Decimal | int(Decimal("10.9")) | 10 - uses truncation |

Constructor with non-numerical argument

int(str, base=10)

| Example | Result |
| --- | --- |
| int("123") | 123 |
| int("1010", base=2) | 10 |
| int("A12F", base=16) | 41264 |
| int("354", base=8 | 348 |

Built-in functions to output integer to as string with another base representation

| Function | Example | Result |
|--- | --- | --- |
| bin | bin(10) | "0b1010" |
| oct | oct(10) | "0o12" |
| hex | hex(10) | "0xa" |

Literal integers with base can be used, example: a = 0b1010 is the same as a=10

# Code examples


```python
int("12345")
```




    12345




```python
int("101", base=2)
```




    5




```python
int("ff", base=16)
```




    255




```python
bin(10)
```




    '0b1010'




```python
oct(10)
```




    '0o12'




```python
hex(10)
```




    '0xa'




```python
a = int("101", base=2)
b = 0b101
```


```python
a
```




    5




```python
b
```




    5



Function that output a base 10 number as a representation of the passed base


```python
def from_base10(n, b):
    if b < 2:
        raise ValueError("Base b must be >= 2")
    
    if n < 0:
        raise ValueError("Number n must be >= 0")
    
    if n == 0:
        return [0]

    digits = []
    
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)
    
    return digits
```


```python
from_base10(10, 2)
```




    [1, 0, 1, 0]




```python
from_base10(255, 16)
```




    [15, 15]




```python
def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digits_map is not long enough to encode the digits")
    
    return "".join([digit_map[digit] for digit in digits])
```


```python
encode([15, 15], "0123456789ABCDEF")
```




    'FF'




```python
def rebase_from10(number, base):
    digit_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    
    sign = -1 if number < 0 else 1
    
    number *= sign
    
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    
    if sign == -1:
        encoding = "-" + encoding
    
    return encoding
```


```python
e = rebase_from10(314, 2)
print(e)
print(int(e, base=2))
```

    100111010
    314



```python
e = rebase_from10(-314, 2)
print(e)
print(int(e, base=2))
```

    -100111010
    -314



```python
e = rebase_from10(3451, 16)
print(e)
print(int(e, base=16))
```

    D7B
    3451



```python

```
