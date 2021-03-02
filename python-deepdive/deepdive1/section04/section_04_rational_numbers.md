# Rational Numbers

- are fractions of integer numbers, ex. 1/2 -22/7
- any real number with a finite numbe of digits after the decimal is also a rational number

Fraction Class

- represents rational numbers
- from fractions import Fraction
- automatically reduces numerator and denominator
- sign is always on the numerator
- defaults: Fraction(numerator=0, denominator=1)
- x.numerator
- x.denominator
- float in Python have finite precision so any float can be written as a fraction

Limiting the denominator to the closest approximation: x.limit_denominator(interger)

# Code examples


```python
from fractions import Fraction
```


```python
Fraction(1)
```




    Fraction(1, 1)




```python
Fraction(numerator=1, denominator=2)
```




    Fraction(1, 2)




```python
Fraction(0.125)
```




    Fraction(1, 8)




```python
Fraction("0.125")
```




    Fraction(1, 8)




```python
Fraction("22/7")
```




    Fraction(22, 7)



Operators


```python
x = Fraction(2, 3)
y = Fraction(3, 4)
```


```python
x + y
```




    Fraction(17, 12)




```python
x * y
```




    Fraction(1, 2)




```python
x / y
```




    Fraction(8, 9)



Fraction automatically reduces


```python
Fraction(8, 16)
```




    Fraction(1, 2)



Fraction moves sign to numerator


```python
x = Fraction(1, -4)
```


```python
x.numerator
```




    -1




```python
x.denominator
```




    4



Float has finite precision


```python
import math
x = Fraction(math.pi)
```


```python
x
```




    Fraction(884279719003555, 281474976710656)




```python
float(x)
```




    3.141592653589793




```python
y = Fraction(math.sqrt(2))
```


```python
y
```




    Fraction(6369051672525773, 4503599627370496)




```python
float(y)
```




    1.4142135623730951



Fraction tries its best to reduce to an approximation of the value


```python
a = 0.125
```


```python
a
```




    0.125




```python
b = 0.3
```


```python
b
```




    0.3




```python
Fraction(a)
```




    Fraction(1, 8)




```python
Fraction(b)
```




    Fraction(5404319552844595, 18014398509481984)




```python
b
```




    0.3




```python
format(b, "0.5f")
```




    '0.30000'




```python
format(b, "0.15f")
```




    '0.300000000000000'



In Python, 0.3 is not stored as 0.3 as seen below


```python
format(b, "0.25f")
```




    '0.2999999999999999888977698'




```python
Fraction(b)
```




    Fraction(5404319552844595, 18014398509481984)



The Fraction denominator can be limited to approximate based on limitation


```python
x = Fraction(0.3)
```


```python
x
```




    Fraction(5404319552844595, 18014398509481984)




```python
x.limit_denominator(10)
```




    Fraction(3, 10)




```python
x = Fraction(math.pi)
```


```python
x
```




    Fraction(884279719003555, 281474976710656)




```python
float(x)
```




    3.141592653589793




```python
x.limit_denominator(10)
```




    Fraction(22, 7)




```python
x.limit_denominator(100_000)
```




    Fraction(312689, 99532)


