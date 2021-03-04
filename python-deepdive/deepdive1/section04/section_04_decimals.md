# Decimals

- have a context that controls aspects of working with decimals, precision and rounding
- context can be global (default) or teimporary (local)
- import decimal
- default context: decimal.getcontext()
- local context: decimal.localcontext(ctx=None) <-- returns a context manager (with)

## Why use decimals?

- float's have a finite number of decimal expansion
- Fraction's is complex and requires extra memory

## Precision and Rounding

precision: during arithmetic operations

rounding: algorithm

### Get context

ctx = decimal.getcontext()

### Get or set the precision (value is an int)

ctx.prec

### Get or set the rounding mechanism (value is a string)

ctx.rounding

| Algorithm | Description |
| --- | --- |
| ROUND_UP | rounds away from zero |
| ROUND_DOWN | rounds toward zero |
| ROUND_CEILING | rounds to ceiling (infinity) |
| ROUND_FLOOR | rounds to floor (-infinity) |
| ROUND_HALF_UP | rounds to nearest, ties away from zero |
| ROUND_HALF_DOWN | rounds to nearest, ties towards zero |
| ROUND_EVEN | rounds to nearest, ties to even (lease significant digit) |

## Working with Global and Local Contexts

### Global

All operations will use the global contexts and any changes to the
global contexts will stick.

Setting the global context rounding 

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

### Local

Operations will use the local contexts only with statements inside the
with block

<pre>
with decimal.localcontext() as ctx:

  ctx.prec = 2

  ctx.rounding = decimal.ROUND_HALF_UP
</pre>

### Code Examples


```python
import decimal
from decimal import Decimal
```


```python
decimal.getcontext()
```




    Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])




```python
decimal.getcontext().rounding
```




    'ROUND_HALF_EVEN'



### Jupyter BUG:

- decimal.getcontext().prec is not working correctly


```python
decimal.getcontext().prec = 6
```


```python
decimal.getcontext()
```




    Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])




```python
g_ctx = decimal.getcontext()
```


```python
type(g_ctx)
```




    decimal.Context




```python
g_ctx.prec = 6
```


```python
g_ctx
```




    Context(prec=6, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])




```python
decimal.getcontext()
```




    Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])




```python
decimal.getcontext().prec = 28
```

### Local


```python
decimal.localcontext()
```




    <decimal.ContextManager at 0x7fa7982eb670>




```python
with decimal.localcontext() as ctx:
    print(type(ctx))
    print(ctx)
```

    <class 'decimal.Context'>
    Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])



```python
with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print()
    print(decimal.getcontext())
    print()
    # Confirm decimal.getcontext uses the current context and not global
    print(id(ctx) == id(decimal.getcontext()))
```

    Context(prec=6, rounding=ROUND_HALF_UP, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
    
    Context(prec=6, rounding=ROUND_HALF_UP, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
    
    True


### Rounding


```python
x = Decimal("1.25")
y = Decimal("1.35")
```


```python
with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print("Local Context:")
    print(round(x, 1))
    print(round(y, 1))

print("Global Context:")
print(round(x, 1))
print(round(y, 1))
```

    Local Context:
    1.3
    1.4
    Global Context:
    1.2
    1.4


# Decimals: Constructors and Contexts

- class is in the decimal module
- Decimal(x): x can be a variety of types; int, str, tuples, ...

## Using the tuple constructor

1.23 --> +123 x 10 ^ -2

-1.23 --> -123 x 10 ^ -2

Using tuple, format: (sign, (digit1, digit2, ..., digitn), exp)

example: -3.1415 --> Decimal(1, (3, 1, 4, 1, 5), -4)

## Context Precision and the Constructor

- Context precision affects mathematical operations
- Context precision does not affect the constructor

Example:

### Setting global precision

decimal.getcontext().prec = 2

<pre>
Global precision does not affect the constructor

    a = Decimal("0.12345") --> a = 0.12345

    b = Decimal("0.12345") --> b = 0.12345
</pre>
<pre>
Global precision does affect the operations

    c = a + b --> c = 0.25
</pre>

### Code examples


```python
import decimal
from decimal import Decimal
```

### Constructor with different types


```python
Decimal(10)
```




    Decimal('10')




```python
Decimal("10.1")
```




    Decimal('10.1')




```python
Decimal((0, (3, 1, 4, 1, 5), -4))
```




    Decimal('3.1415')




```python
Decimal((1, (3, 1, 4, 1, 5), -4))
```




    Decimal('-3.1415')



### Floats has issues


```python
# Issues with floats
format(0.1, ".25f")
```




    '0.1000000000000000055511151'




```python
Decimal(0.1)
```




    Decimal('0.1000000000000000055511151231257827021181583404541015625')




```python
Decimal(0.1) == Decimal("0.1")
```




    False



### Context (Jupyter has a bug)


```python
decimal.getcontext().prec = 2
```


```python
# global context precision does not affect constructor
a = Decimal("0.123456789")
```


```python
a
```




    Decimal('0.123456789')




```python
# Juypter bug, global precision not working
a + a
```




    Decimal('0.246913578')




```python
print(f"Global context: a + a = {a + a}")

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(f"Local context: a + a = {a + a}")
```

    Global context: a + a = 0.246913578
    Local context: a + a = 0.25


# Decimals: Mathematical Operations

- some arithmetic operators don't work the same as floats or integers: //, %, divmod()
- // operator performs a truncated division, affects negative numbers

Examples

| Integer | Decimal |
| --- | --- |
| 10 // 3 = 3 | Decimal(10) // Decimal(10) // Decimal(3) = Decimal(3) |
| -10 // 3 = -4 | Decimal(10) // Decimal(-10) // Decimal(3) = Decimal(-3) |

## Code Examples


```python
import decimal
from decimal import Decimal
```


```python
x = 10
y = 3
print(x//y, x%y)
print(divmod(x,y))
print(x== y * (x//y) + (x%y))
```

    3 1
    (3, 1)
    True



```python
x = Decimal(10)
y = Decimal(3)
print(x//y, x%y)
print(divmod(x,y))
print(x== y * (x//y) + (x%y))
```

    3 1
    (Decimal('3'), Decimal('1'))
    True



```python
x = -10
y = 3
print(x//y, x%y)
print(divmod(x,y))
print(x== y * (x//y) + (x%y))
```

    -4 2
    (-4, 2)
    True



```python
x = Decimal(-10)
y = Decimal(3)
print(x//y, x%y)
print(divmod(x,y))
print(x== y * (x//y) + (x%y))
```

    -3 -1
    (Decimal('-3'), Decimal('-1'))
    True


### Other Math functions


```python
a = Decimal("1.5")
```


```python
a
```




    Decimal('1.5')




```python
a.ln()
```




    Decimal('0.4054651081081643819780131155')




```python
a.exp()
```




    Decimal('4.481689070338064822602055460')




```python
a.sqrt()
```




    Decimal('1.224744871391589049098642037')




```python
x = 2
x_dec = Decimal(2)
```


```python
import math
```


```python
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
```


```python
print(format(root_float, "1.27f"))
print(format(root_mixed, "1.27f"))
print(root_dec)
```

    1.414213562373095145474621859
    1.414213562373095145474621859
    1.414213562373095048801688724



```python
print(format(root_float * root_float, "1.27f"))
print(format(root_mixed * root_mixed, "1.27f"))
print(root_dec * root_dec)
```

    2.000000000000000444089209850
    2.000000000000000444089209850
    1.999999999999999999999999999



```python
x = 0.01
x_dec = Decimal("0.01")
```


```python
print(format(x, ".27f"))
print(x_dec)
```

    0.010000000000000000208166817
    0.01



```python
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
```


```python
print(format(root_float, "1.27f"))
print(format(root_mixed, "1.27f"))
print(root_dec)
```

    0.100000000000000005551115123
    0.100000000000000005551115123
    0.1



```python
print(format(root_float * root_float, "1.27f"))
print(format(root_mixed * root_mixed, "1.27f"))
print(root_dec * root_dec)
```

    0.010000000000000001942890293
    0.010000000000000001942890293
    0.01


# Decimals: Performance Considerations

Drawbacks to the Decimal class vs the float class

- not as easy to code: construction via strings or tuples
- not all mathematical functions that exist in the math module have a Decimal counterpart
- more memory overhead
- performance is much slower than floats

## Code Examples:


```python
from decimal import Decimal
```


```python
import sys
```

### Comparing overhead


```python
a = 3.1415
b = Decimal("3.1415")
```


```python
sys.getsizeof(a)
```




    24




```python
sys.getsizeof(b)
```




    104



### Performance


```python
import time
```

### Timing duration of creating a float vs decimal


```python
def run_float(n=1):
    for i in range(n):
        a = 3.1415

def run_decimal(n=1):
    for i in range(n):
        a = Decimal("3.1415")
```


```python
n = 10_000_000
```


```python
start = time.perf_counter()
run_float(n)
end_time = time.perf_counter()
print(f"float: {end_time - start}")
```

    float: 0.5650138259807136



```python
start = time.perf_counter()
run_decimal(n)
end_time = time.perf_counter()
print(f"float: {end_time - start}")
```

    float: 3.263208988995757


### Timing duration of adding, float vs decimal


```python
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a

def run_decimal(n=1):
    a = Decimal("3.1415")
    for i in range(n):
        a + a
```


```python
start = time.perf_counter()
run_float(n)
end_time = time.perf_counter()
print(f"float: {end_time - start}")
```

    float: 0.8693183780123945



```python
start = time.perf_counter()
run_decimal(n)
end_time = time.perf_counter()
print(f"float: {end_time - start}")
```

    float: 1.784163254982559


### Timing duration of using sqrt, float vs decimal


```python
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)

def run_decimal(n=1):
    a = Decimal("3.1415")
    for i in range(n):
        a.sqrt()
```


```python
n = 5_000_000
```


```python
start = time.perf_counter()
run_float(n)
end_time = time.perf_counter()
print(f"float: {end_time - start}")
```

    float: 0.914245280000614



```python
start = time.perf_counter()
run_decimal(n)
end_time = time.perf_counter()
print(f"float: {end_time - start}")
```

    float: 22.89354524301598

