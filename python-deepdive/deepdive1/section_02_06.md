# Multi-Line Statements and Strings

## Python Program

*Physical* lines of code (written code) end with a *physical newline* character

*Logical* lines of code (grammar) end with a *logical NEWLINE* token

*Sometimes*, physical newlines are ignored *in order to* combine multiple physical lines
*into a* single logical line of code *terminated* by a logical NEWLINE token

This allows us to make code more readable.


## Implicit Multi-Line


list literals: []



```python
[
    1,
    2,
    3
]
```




    [1, 2, 3]



tuple lieterals: ()



```python
(
    1,
    2,
    3
)
```




    (1, 2, 3)



dictionary literals: {}



```python
{
    1: 1,
    2: 2,
    3: 3
}
```




    {1: 1, 2: 2, 3: 3}



set literals: {}



```python
{
    1,
    2,
    3
}
```




    {1, 2, 3}



function parameters / arguments with inline comments



```python
def func(
    a: int, # parameter a
    b: int, # parameter b
    c: int  # parameter c
) -> int:
    return a + b + c
```


```python
func(
    1, # argument a
    2, # argument b
    3  # argument c
)
```




    6



## Explicit Multi-Line

Statements can be broken into multiple lines explicitly, by using the *\* character.

Multi-line statements are not implicitly converted to a single logical line.


```python
a = b = c = True
```

*Invalid* multi-line statement


```python
if a
    and b
        and c:
    pass
```


      File "<ipython-input-9-044a5129ebdf>", line 1
        if a
            ^
    SyntaxError: invalid syntax




```python
*Valid* explicittly multi-line statement.  Indentention does not matter because logically it will be a
single line statement.

```


```python
if a \
    and b \
        and c:
    print(True)
```

    True


## Multi-line String Literals

Multi-line string literals are created using triple delimeters using either *'* single or *"* double
qoutes.  These strings will include control characters as part of the strings such as spaces, newline,
and tabs.



```python
m1 = '''
This is a multi-line string literal.
'''

m2 = """
This is also a multi-line string literal.
"""

m3 = '''
        This is also a multi-line string literal.
    '''
```


```python
print(m1)
print(m2)
print(m3)
```

    
    This is a multi-line string literal.
    
    
    This is also a multi-line string literal.
    
    
            This is also a multi-line string literal.
        


A string assigned as a multi-line will include space, and escaped new line characters.


```python
a = '''
This is a
   multi-line
     string.
'''
```


```python
a
```




    '\nThis is a\n   multi-line\n     string.\n'


