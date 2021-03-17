# Application: A Simple Function Timer


```python
import time
```


```python
def time_it(fn, *args, **kwargs):
    print(args, kwargs)
```


```python
time_it(print, 1, 2, 3, sep=" - ", end=" *** ")
```

    (1, 2, 3) {'sep': ' - ', 'end': ' *** '}



```python
def time_it(fn, *args, **kwargs):
    fn(args, kwargs)
```


```python
time_it(print, 1, 2, 3, sep=" - ", end=" *** ")
```

    (1, 2, 3) {'sep': ' - ', 'end': ' *** '}



```python
def time_it(fn, *args, **kwargs):
    fn(*args, **kwargs)
```


```python
time_it(print, 1, 2, 3, sep=" - ", end=" *** ")
```

    1 - 2 - 3 *** 


```python
def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)
```


```python
time_it(print, 1, 2, 3, sep=" - ", end=" ***\n", rep=5)
```

    1 - 2 - 3 ***
    1 - 2 - 3 ***
    1 - 2 - 3 ***
    1 - 2 - 3 ***
    1 - 2 - 3 ***



```python
def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    
    for i in range(rep):
        fn(*args, **kwargs)
    
    end = time.perf_counter()
    
    return (end - start) / rep
```


```python
time_it(print, 1, 2, 3, sep=" - ", end=" ***\n", rep=5)
```

    1 - 2 - 3 ***
    1 - 2 - 3 ***
    1 - 2 - 3 ***
    1 - 2 - 3 ***
    1 - 2 - 3 ***





    0.00013640380000197184




```python
# Using for loop
def compute_powers_1(n, *, start=1, end):
    results = list()
    
    for i in range(start, end):
        results.append(n**i)
        
    return results
```


```python
compute_powers_1(2, end=5)
```




    [2, 4, 8, 16]




```python
# Using list comprehension
def compute_powers_2(n, *, start=1, end):
    return [n**i for i in range(start, end)]
```


```python
compute_powers_2(2, end=5)
```




    [2, 4, 8, 16]




```python
# Using generator
def compute_powers_3(n, *, start=1, end):
    return (n**i for i in range(start, end))
```


```python
list(compute_powers_3(2, end=5))
```




    [2, 4, 8, 16]




```python
time_it(compute_powers_1, 2, start=0, end=20_000, rep=5)
```




    0.5922450575999847




```python
time_it(compute_powers_2, 2, start=0, end=20_000, rep=5)
```




    0.593792359400004




```python
# this returns the time to create a genarator and not calculate values
time_it(compute_powers_3, 2, start=0, end=20_000, rep=5)
```




    1.960000008693896e-06


