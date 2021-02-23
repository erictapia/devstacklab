# Functions


```python
s = [1, 2, 3]

# builtin len function
len(s)
```




    3




```python
# builtin functions that can be imported
from math import sqrt

sqrt(4)
```




    2.0




```python
# import the whole module
import math

math.pi
```




    3.141592653589793




```python
math.exp(1)
```




    2.718281828459045




```python
# Defining a function
def func_1():
    print("running func_1")

# calling function
func_1()
```

    running func_1



```python
# Defining a function with parameters and annotations
def func_2(a: int, b: int):
    return a * b


func_2(2, 3)
```




    6




```python
# Annotation do not do any type checking, its mainly for documentation
func_2("a", 3)
```




    'aaa'



# Functions must be defined before being called


```python
# This works because a function definition does not execut the code
def func_3():
    return func_4()


def func_4():
    return "returning func_4"


func_3()
```




    'returning func_4'




```python
# This will not work because the call is happening before defining func_6
# This works because a function definition does not execut the code
def func_5():
    return func_6()


func_5()


def func_6():
    return "returning func_6"

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-3ae999ef8030> in <module>
          5 
          6 
    ----> 7 func_5()
          8 
          9 


    <ipython-input-10-3ae999ef8030> in func_5()
          2 # This works because a function definition does not execut the code
          3 def func_5():
    ----> 4     return func_6()
          5 
          6 


    NameError: name 'func_6' is not defined


# Lambda functions


```python
lambda x: x**2
```




    <function __main__.<lambda>(x)>




```python
fn1 = lambda x: x**2

fn1(2)
```




    4


