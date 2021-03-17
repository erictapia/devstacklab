# Parameter Defaults - Beware Again



```python
def add_item(name, quantity, unit, grocery_list):
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list
```


```python
store1 = list()
store2 = list()
```


```python
add_item("banana", 2, "units", store1)
```




    ['banana (2 units)']




```python
add_item("milk", 1, "liter", store1)
```




    ['banana (2 units)', 'milk (1 liter)']




```python
store1
```




    ['banana (2 units)', 'milk (1 liter)']




```python
add_item("python", 1, "medium-rare", store2)
```




    ['python (1 medium-rare)']




```python
store2
```




    ['python (1 medium-rare)']




```python
# Default value is an empty grocery_list
# Issue: all calls that use the default value will
# share the same default list (pointer to same object)
def add_item(name, quantity, unit, grocery_list=[]):
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list
```


```python
store3 = add_item("banana", 2, "units")
```


```python
add_item("milk", 1, "liter", store3)
```




    ['banana (2 units)', 'milk (1 liter)']




```python
store3
```




    ['banana (2 units)', 'milk (1 liter)']




```python
store4 = add_item("python", 1, "medium-rare")
```


```python
store4
```




    ['banana (2 units)', 'milk (1 liter)', 'python (1 medium-rare)']




```python
# Rewrite to fix issue
def add_item(name, quantity, unit, grocery_list=None):
    grocery_list = grocery_list or list()
    
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list
```


```python
store5 = add_item("banana", 2, "units")
```


```python
add_item("milk", 1, "liter", store5)
```




    ['banana (2 units)', 'milk (1 liter)']




```python
store6 = add_item("python", 1, "medium-rare")
```


```python
store6
```




    ['python (1 medium-rare)']




```python
def factorial(n):
    if n < 1:
        return 1
    else:
        print(f"calculating {n}")
        return n * factorial(n-1)
```


```python
factorial(3)
```

    calculating 3
    calculating 2
    calculating 1





    6




```python
cache = {}

def factorial(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f"calculating {n}")
        result = n* factorial(n-1, cache=cache)
        cache[n] = result
        return result
```


```python
factorial(3, cache=cache)
```

    calculating 3
    calculating 2
    calculating 1





    6




```python
factorial(3, cache=cache)
```




    6




```python
# Leveraging immutable default value that gets shared
def factorial(n, *, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f"calculating {n}")
        result = n* factorial(n-1, cache=cache)
        cache[n] = result
        return result
```


```python
factorial(3)
```

    calculating 3
    calculating 2
    calculating 1





    6




```python
factorial(3)
```




    6


