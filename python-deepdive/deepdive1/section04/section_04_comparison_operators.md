# Comparison Operators

- binary operators: evaluate to a bool value
- identity operations(is, is not): compares memory address
- value comparisons (==, !=): compares values
- ordering comparisons (< &lt;=, >, >=): doesn't work for all types
- membership operations (in, not in): used with iterable types

## Numeric Types

- value comparisons will work with all numeric types
- mixed types (except complex) in value and ordering comparisons is supported

## Code Examples

### Comparison Operators

bug using the is operator: juypter warnings


```python
0.1 is (3+4j)
```

    <>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
    <>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
    <ipython-input-2-aadb6322e9fe>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
      0.1 is (3+4j)





    False




```python
3 is 3
```

    <>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
    <>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
    <ipython-input-3-1ee75a7b8cc8>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
      3 is 3





    True




```python
[1, 2] is [1, 2]
```




    False




```python
"a" in "this is a test"
```




    True




```python
3 in [1, 2, 3]
```




    True




```python
3 not in [1, 2, 3]
```




    False




```python
"key" in {"key": 1}
```




    True




```python
1 in {"key": 1}
```




    False




```python
3 < 5
```




    True




```python
1+ 1j < 3 + 4j
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-cd96fc565854> in <module>
    ----> 1 1+ 1j < 3 + 4j
    

    TypeError: '<' not supported between instances of 'complex' and 'complex'



```python
from decimal import Decimal
from fractions import Fraction
```


```python
4 < Decimal("10.5")
```




    True




```python
Fraction(2, 3) < Decimal("0.5")
```




    False




```python
0.1 == Decimal("0.1")
```




    False




```python
0.1 == Decimal(0.1)
```




    True




```python
4 == (4 + 0j)
```




    True


