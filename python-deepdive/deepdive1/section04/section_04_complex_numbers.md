# Complex Numbers (huh? lol I forgot what I once knew)

- Construtor: complex(x, y)
- x: real part
- y: imaginary part
- literal: x + yJ or x + yj
- x and y are stored as floats

Example:

<pre>
    a = complex(1, 2)
    b = 1 + 2j
    a == b  --> True
</pre>

## Properties and methods

- .real
- .imag
- .conjugate() --> returns the complex conjugate

## Arithmetic operators

- standard arithmetic operators work as expected with complex numbers
- real and complex numbers can be mixed, (1 + 2j) * 3 --> 4 + 2j
- // and % operators are not supported

## Other operations

- == and != operators are supported
- comparison operators are not supported, <. >, ...
- math module functions will not work
- cmath module functions work

## cmath functions

- .phase(x): returns the angle between -pi, pi counter-clockwise from the real axis
- .abs(x): returns the magnitude (r) of x
- .rect(r, phi): returns a complex number equivalent to the complex number defined by r,phi

## Code Examples


```python
a = complex(1, 2)
```


```python
a
```




    (1+2j)




```python
b = 1 + 2j
```


```python
b
```




    (1+2j)




```python
a == b
```




    True




```python
a.real,type(a.real)
```




    (1.0, float)




```python
a.imag,type(a.imag)
```




    (2.0, float)




```python
a.conjugate()
```




    (1-2j)




```python
a = 1 + 2j
b = 10 + 8j
```


```python
a + b
```




    (11+10j)




```python
a * b
```




    (-6+28j)




```python
a / b
```




    (0.1585365853658537+0.07317073170731708j)



### Non-supported operators


```python
a // 2
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-15-066bb42fbcdc> in <module>
    ----> 1 a // 2
    

    TypeError: can't take floor of complex number.



```python
a % 2
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-16-1a711ff621d1> in <module>
    ----> 1 a % 2
    

    TypeError: can't mod complex numbers.



```python
divmod(a, b)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-17-317a292a216e> in <module>
    ----> 1 divmod(a, b)
    

    TypeError: can't take floor or mod of complex number.


### More code examples


```python
a = 0.1j
```


```python
format(a.imag, ".25f")
```




    '0.1000000000000000055511151'




```python
a + a + a == 0.3j
```




    False




```python
format((a + a + a).imag, ".25f")
```




    '0.3000000000000000444089210'




```python
format((0.3j).imag, ".25f")
```




    '0.2999999999999999888977698'



## cmath - watched video only
