# Booleans

- bool clas is a subclass of the int class
- singleton object of type bool
- is vs ==, boolean can use either because a bool is a singleton object
- True vs 1, are not the same objects; same applies to False vs 0

## Boolean constructor

- bool(x)
- each class has a truth state, constructor returns the class truth value (truthyness)

## Code Examples


```python
issubclass(bool, int)
```




    True




```python
type(True), id(True), int(True)
```




    (bool, 9472352, 1)




```python
type(False), id(False), int(False)
```




    (bool, 9469920, 0)




```python
3 < 4
```




    True




```python
type(3 < 4), id(3 < 4), int(3 < 4)
```




    (bool, 9472352, 1)




```python
# == compares variable value
# is compares variable id
(3 < 4) == True, (3 < 4) is True
```




    (True, True)




```python
None is False
```




    False




```python
int(True), int(False)
```




    (1, 0)




```python
1 + True
```




    2




```python
(True + True + True) % 2
```




    1




```python
bool(0)
```




    False




```python
bool(1)
```




    True




```python
bool(-1)
```




    True



# Booleans: Truth Values

- all objects in Python have an associated truth value

## Object Truth value rule: True except

- None
- False
- 0 in any numeric type
- empty sequences (list, tuple, string, ...)
- empty mapping types (dictionary, set, ...)
- custom classesthat implement a \__bool__ or \__len__ method that returns False or 0

## Under the hood

Classes define their truth values by defining a special instance method:

- \__bool__
- \__len__

bool(x) --> Python will execute x.\__bool__()

If \__bool__ is not defined then it tries x.\__len__()

If neither is defined, then it returns True

## Code Examples


```python
bool(1), bool(0), bool(-1)
```




    (True, False, True)




```python
# __bool__ does the following
1 != 0
```




    True




```python
bool(0), (0).__bool__()
```




    (False, False)




```python
a = []
bool(a)
```




    False




```python
# bool(list) does the following
a.__len__()
```




    0




```python
bool(a), a.__len__()
```




    (False, 0)




```python
# Lists do not have a __bool__
a.__bool__()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-24-248732f76df1> in <module>
    ----> 1 a.__bool__()
    

    AttributeError: 'list' object has no attribute '__bool__'



```python
bool(0), bool(0.0), bool(0 + 0j)
```




    (False, False, False)




```python
from decimal import Decimal
from fractions import Fraction
```


```python
bool(Fraction(0, 1)), bool(Decimal("0.0"))
```




    (False, False)




```python
bool(10.5), bool(1j), bool(Fraction(1, 2)), bool(Decimal("10.5"))
```




    (True, True, True, True)




```python
a = []
b = ""
c = ()
bool(a), bool(b), bool(c)
```




    (False, False, False)




```python
a = [1, 2]
b = "a"
c = (1, 2)
bool(a), bool(b), bool(c)
```




    (True, True, True)




```python
a = dict()
b = set()
bool(a), bool(b)
```




    (False, False)




```python
a = {"a": 1}
b = {1, 2}
bool(a), bool(b)
```




    (True, True)




```python
bool(None)
```




    False




```python
None.__bool__()
```




    False



# Booleans; Precedence and Short-Circuiting

- boolean operators: not, and, or

## Commutativity

<pre>
    A or B == B or A
    A and B == B and A
</pre>

## Distributivity
<pre>
    A and (B or C) == (A and B) or (A and C)
    A or (B and C) == (A or B) and (A or C)
</pre>

## Associativity

<pre>
    A or (B or C) == (A or B) or C
    A and (B and C) == (A and B) and C
    
    A or B or C --> (A or B) or C
    A and B and C --> (A and B) and C
    
    left-to-right evaluation
</pre>

## De Morgan's Theorem

<pre>
    not(A or B) == (not A) and (not B)
    not(A and B) == (not A) or (not B)
</pre>

# Miscellaneous

<pre>
    not(x < y) == x >= y
    not(x > y) == x &lt;= y
    not(x &lt;= y) == x > y
    not(x >= y) == x < y
    not(not A) == A
</pre>

## Operator Precedence

Higest to lowest order

- ()
- < > &lt;= >= == != in is
- not
- and
- or

Example:

True or True and False --> True or False --> True

(True or True) and False --> True and False --> False

## Short-Circuit Evaluation

- or: stops evaluating on the first True, and return True
- and: stops evaluating on the first False, and return False

## Code Example

### Precedence


```python
True or True and False
```




    True




```python
True or (True and False)
```




    True




```python
(True or True) and False
```




    False



### Short-Circuiting


```python
a = 10
b = 2

if a/b > 2:
    print("a is at least twice b")
```

    a is at least twice b



```python
a = 10
b = 0

if a/b > 2:
    print("a is at least twice b")
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-42-8dbac3607676> in <module>
          2 b = 0
          3 
    ----> 4 if a/b > 2:
          5     print("a is at least twice b")


    ZeroDivisionError: division by zero



```python
if b > 0:
    if a/b > 2:
        print("a is at least twice b")
```


```python
if b > 0 and a/b > 2:
    print("a is at least twice b")
```


```python
if b and a/b > 2:
    print("a is at least twice b")
```


```python
b = None
```


```python
if b > 0 and a/b > 2:
    print("a is at least twice b")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-49-49963ee778d8> in <module>
    ----> 1 if b > 0 and a/b > 2:
          2     print("a is at least twice b")


    TypeError: '>' not supported between instances of 'NoneType' and 'int'



```python
if b and a/b > 2:
    print("a is at least twice b")
```


```python
import string
```


```python
a = "c"
a in string.ascii_uppercase
```




    False




```python
a in string.ascii_lowercase
```




    True




```python
name = "Bob"

if name[0] in string.digits:
    print("Name cannot start with a digit")
```


```python
name = ""

if name[0] in string.digits:
    print("Name cannot start with a digit")
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-55-ab9b331784f7> in <module>
          1 name = ""
          2 
    ----> 3 if name[0] in string.digits:
          4     print("Name cannot start with a digit")


    IndexError: string index out of range



```python
if len(name) and name[0] in string.digits:
    print("Name cannot start with a digit")
```


```python
name = None
bool(name)
```




    False




```python
if len(name) and name[0] in string.digits:
    print("Name cannot start with a digit")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-60-47d1f189d1e2> in <module>
    ----> 1 if len(name) and name[0] in string.digits:
          2     print("Name cannot start with a digit")


    TypeError: object of type 'NoneType' has no len()



```python
if name and name[0] in string.digits:
    print("Name cannot start with a digit")
```

# Booleans: Boolean Operators

- Normally, Boolean operators are defined to operate on and return Boolean values

## Definition of or in Python

- X or Y --> If X is truthy, returns X, otherwise returns Y

| X | Y | Rule | Result |
| --- | --- | --- | --- |
| 0 | 0 | X is False, so return Y | 0 |
| 0 | 1 | X is False, so return Y | 1 |
| 1 | 0 | X is True, so return X | 1 |
| 1 | 1 | X is True, so return X | 1 |

| X | Y | Result |
| --- | --- | --- |
| None | "N/A" | "N/A" |
| "" | "N/A" | "N/A" |
| "hello" | "N/A" | "hello" |

- X and Y --> If X is falsy, returns X, otherwise returns Y

| X | Y | Rule | Result |
| --- | --- | --- | --- |
| 0 | 0 | X is False, so return X | 0 |
| 0 | 1 | X is False, so return X | 0 |
| 1 | 0 | X is True, so return Y | 0 |
| 1 | 1 | X is True, so return Y | 1 |

| X | Y | Result |
| --- | --- | --- |
| None | "N/A" | None |
| "" | "N/A" | "" |
| "hello" | "N/A" | "N/A" |

- not X --> True if x is falsy, False if x is truthy

## Code Examples

### X or Y

- if X is truthy, return X
- if X is falsy, evaluate Y and return it


```python
"a" or [1, 2]
```




    'a'




```python
"" or [1, 2]
```




    [1, 2]




```python
# Division by zero
0 or 1/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-64-7885d3533ce6> in <module>
          1 # Division by zero will not get evaluated due to short circuit
    ----> 2 0 or 1/0
    

    ZeroDivisionError: division by zero



```python
# Division by zero will not get evaluated due to short circuit
1 or 1/0
```




    1




```python
s1 = None
s2 = ""
s3 = "abc"
```


```python
# Technique to assign default value
s1 = s1 or "n/a"
s2 = s2 or "n/a"
s3 = s3 or "n/a"
s1, s2, s3
```




    ('n/a', 'n/a', 'abc')



### X and Y

- if X is falsy, return X
- if X is truthy, evaluate Y and return Y


```python
print(None and 100)
```

    None



```python
[] and [0]
```




    []




```python
a = 2
b = 0
a/b
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-72-32aaa10883f1> in <module>
          1 a = 2
          2 b = 0
    ----> 3 a/b
    

    ZeroDivisionError: division by zero



```python
if b == 0:
    print(0)
else:
    print(a/b)
```

    0



```python
a = 2
b = 4
if b == 0:
    print(0)
else:
    print(a/b)
```

    0.5



```python
print(b and a/b)
```

    0.5



```python
b = 0
print(b and a/b)
```

    0



```python
s1 = None
s2 = ""
s3 = "abc"
```


```python
print(s1 and s1[0])
print(s2 and s2[0])
print(s3 and s3[0])
```

    None
    
    a



```python
# Or to set default
print(s1 and s1[0] or "")
print(s2 and s2[0] or "")
print(s3 and s3[0] or "")
```

    
    
    a


### Not

- return value is always a bool


```python
not True
```




    False




```python
not False
```




    True




```python
not "abc"
```




    False




```python
not ""
```




    True




```python

```
