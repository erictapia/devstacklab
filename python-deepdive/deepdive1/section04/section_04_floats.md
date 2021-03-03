# Floats: Internal Representations

- is Python's default implementation for representing real numbers
- implemented using the C double type, also called binary64
- uses a fixed number of bytes, 8 bytes but with overhead is 24 bytes
- infinite numbers have an approximate float representation

64 bits structure:
- sign: 1 bit
- exponent: 11 bits, range: -1022, 1023
- significant digits: 52 bits, 15-17 significant (base 10) digits 

Examples:

| Value | Sign | Exponent | Significant |
| --- | --- | --- | --- |
| 1.2345 | 0 | -4 | 12345 |
| 1234.5 | 0 | -1 | 12345 |
| 12345000000 | 0 | 6 | 12345 |
| 0.00012345 | 0 | -3 | 12345 |
| 12345e-50 | 0 | -50 | 12345 |

Representation: decimal

- numbers can be represented as base-10 intgers and fractions

Examples:

0.75 = 7/10 + 5/100 = 7 x 10^-1 + 5 x 10^-2

0.256 = 2/10 + 5/100 + 6/1000 = 2 x 10^-1 + 5 x 10^-2 + 6 x 10^-3

Representation: decimal

- numbers are represented using bits, powers of 2
- not all numbers have a finite binary representation

Examples:

binary float(0.11) = 1/2 + 1/4 = 1 x 2^-1 + 1 x 2^-2 (BASE 10)

## Code examples


```python
float(10)
```




    10.0




```python
float(10.4)
```




    10.4




```python
float("12.5")
```




    12.5



Float from a string fraction raises a ValueError exception


```python
float("1/7")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-6-af90f7de8da8> in <module>
    ----> 1 float("1/7")
    

    ValueError: could not convert string to float: '1/7'



```python
from fractions import Fraction
```


```python
a = Fraction("22/7")
```


```python
float(a)
```




    3.142857142857143



Python will sometimes use smaller precision but internally the float has a
different precision


```python
print(0.1)
```

    0.1



```python
format(0.1, ".15f")
```




    '0.100000000000000'




```python
format(0.1, ".25f")
```




    '0.1000000000000000055511151'



There are some float numbers that have an exact float representation


```python
print(0.125)
```

    0.125



```python
1/8
```




    0.125




```python
format(0.125, ".25f")
```




    '0.1250000000000000000000000'



# Floats: Equality Testing

- float equality can lead to some "weirdness", 0.1 + 0.1 + 0.1 != 0.3
- equality can be compared with absolute tolerances, format(f, tolarance)

## Example of absolute tolerances

x = 0.1 + 0.1 + 0.1 --> 0.30000000000000004441

y = 0.3 --> 0.2 --> 0.29999999999999998890

difference: 0.00000000000000005551

Using absolute tolerances, 

abs_tol = 10^-15 = 0.000000000000001

math.fabs(x - y) < abs_tol   <-- True

a = 10000.1 + 10000.1 + 10000.1 --> 30000.30000000000291038305

b = 30000.3 --> 30000.29999999999927240424

difference: 0.0000000000033797881

math.fabs(a - b) < abs_tol   <-- False


## Examples of relative tolerances

### small numbers

rel_tol = 0.001% = 1e-5

tol = rel_tol * max(|x|, |y|)

x = 0.1 + 0.1 + 0.1

y = 0.3 --> 0.2

tol = 0.000003000000000

math.fabs(x - y) < tol   <-- True


### Big numbers

x = 10000.1 + 10000.1 + 10000.1

y = 30000.3

tol = 0.300003000000000

math.fabs(a - b) < tol   <-- True

## Combining both techniques

- use the larger of the two tolerances
- math uses this solution as described in PEP 485
- math.isclose(a, b, *, rel_tol-le-09, abs_tol=0.0)
- math.isclose defaults is not good for values close to 0

## Code Examples


```python
x = 0.1
```


```python
format(x, ".25f")
```




    '0.1000000000000000055511151'




```python
x = 0.125
```


```python
format(x, ".25f")
```




    '0.1250000000000000000000000'




```python
x = 0.125 + 0.125 + 0.125
```


```python
y = 0.375
```


```python
x == y
```




    True




```python
x = 0.1 + 0.1 + 0.1
```


```python
y = 0.3
```


```python
x == y
```




    False




```python
format(x, ".25f")
```




    '0.3000000000000000444089210'




```python
format(y, ".25f")
```




    '0.2999999999999999888977698'




```python
round(x, 3) == round(y, 3)
```




    True




```python
x = 10000.01
y = 10000.02
x/y
```




    0.9999990000019999




```python
x = 0.1
y = 0.2
x/y
```




    0.5




```python
from math import isclose
```


```python
x = 0.1+ 0.1 + 0.1
y = 0.3
```


```python
isclose(x, y)
```




    True




```python
x == y
```




    False




```python
x = 123456789.01
y = 123456789.02
```


```python
isclose(x, y, rel_tol=0.01)
```




    True




```python
x = 0.01
y = 0.02
isclose(x, y, rel_tol=0.01)
```




    False




```python
x = 0.0000001
y = 0.0000002
isclose(x, y, rel_tol=0.01)
```




    False




```python
isclose(x, y, rel_tol=0.01, abs_tol=0.01)
```




    True



# Floats: Coercing to Integers

- float -> Integer
- data loss
- different ways to configure data loss

Methods (data loss in all cases)

- truncation
- floor
- ceiling
- rounding

## Truncation

- returns the integer portion of the number
- ignores everything after the decimal point
- math.trunc()
- ex: 10.4 -> 10
- the int constructor uses truncation, ex: int(10.4) -> 10

## Floor

- returns the largest integer less than (or equal to) the number
- ex: 10.4 -> 10, -10.4 -> -11
- positive numbers, truncation and floor are equivalent
- negative numbers, truncation and floor are different
- //
- math.floor()

## Ceiling

- returns the smallest integer greater than (or equal to) the number
- ex: 10.4 -> 11, -10.3 -> -10
- math.ceil()

## Code Examples


```python
from math import trunc
```


```python
trunc(10.3), trunc(10.5), trunc(10.9)
```




    (10, 10, 10)




```python
int(10.4), int(10.5), int(10.9)
```




    (10, 10, 10)




```python
from math import floor
```


```python
floor(10.3), floor(10.5), floor(10.9)
```




    (10, 10, 10)




```python
trunc(-10.3), trunc(-10.5), trunc(-10.9)
```




    (-10, -10, -10)




```python
floor(-10.3), floor(-10.5), floor(-10.9)
```




    (-11, -11, -11)




```python
from math import ceil
```


```python
ceil(10.4), ceil(10.5), ceil(10.9)
```




    (11, 11, 11)




```python
ceil(-10.4), ceil(-10.5), ceil(-10.9)
```




    (-10, -10, -10)



# Floats: Rounding

- built-in function, round(x, n=0)
- returns integer x to the closest multiple of 10 ^-n
- by default, n = 0, round will return the int
- passing an n argument, the return type is the same as the passed type
- it looks at the differences between the passed value and the integer before and after in the 10^-n position.
- the integer with smallest difference is returned value
- ex: round(18.2, -1) -> 20.0
- with ties, same difference, it rounds using banker's rounding
- banker's rounding: it rounds to the nearest value with an even least significant digit
- ex: round(1.25, 1) -> 1.2, round(-1.25, 1) -> -1.2  <-- Not 1.3, -1.3

## Rounding away from zero

- sign(x) * int(x + 0.5 * sign(x))
- ex: 10.4 + 0.5 = 10.9 = int(10.9) = 10
- ex: 10.5 + 0.5 = 11.0 = int(11.0) = 11

## Math.copysign()

- returns the magnitude (absolute value) of x but with the sign of y
- copysign(x, y)

## Code Examples


```python
a = round(1.9)
a, type(a)
```




    (2, int)




```python
a = round(1.9, 0)
a, type(a)
```




    (2.0, float)



### n > 0


```python
round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0)
```




    (1.889, 1.89, 1.9, 2.0)



### n < 0


```python
round(888.88, 1), round(888.88, 0), \
round(888.88, -1), round(888.88, -2), round(888.88, -3), round(888.88, -4)
```




    (888.9, 889.0, 890.0, 900.0, 1000.0, 0.0)



### Ties - Banker's Rounding


```python
round(1.25, 1)
```




    1.2




```python
round(1.35, 1)
```




    1.4




```python
round(-1.25, 1)
```




    -1.2




```python
round(-1.35, 1)
```




    -1.4



### Impementing a float rounding away from 0 


```python
from math import copysign

def _round(x):
    return int(x + 0.5 * copysign(1, x))
```


```python
round(1.5), _round(1.5)
```




    (2, 2)




```python
round(2.5), _round(2.5)
```




    (2, 3)


