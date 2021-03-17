# Parameter Defaults - Beware

- when modules load, it executes all code that reference an object
- default values are created when a module loads

## Code Examples


```python
from datetime import datetime
```


```python
datetime.utcnow()
```




    datetime.datetime(2021, 3, 17, 14, 15, 37, 461499)




```python
print(datetime.utcnow())
```

    2021-03-17 14:16:00.499770



```python
# Default value will be evaluated at module load and
# remain the same for all function calls
def log(msg, *, dt=datetime.utcnow()):
    print(f"{dt}: {msg}")
```


```python
log("message 1", dt="2021-01-01 00:00:00.000")
```

    2021-01-01 00:00:00.000: message 1



```python
log("message 2")
```

    2021-03-17 14:17:44.830221: message 2



```python
log("message 3")
```

    2021-03-17 14:17:44.830221: message 3



```python
# Default value is set to None
# then a conditional can be used
# to set dt to the current time
def log(msg, *, dt=None):
    if not dt:
        dt = datetime.utcnow()
        
    print(f"{dt}: {msg}")
```


```python
log("message 2")
```

    2021-03-17 14:21:45.853547: message 2



```python
log("message 3")
```

    2021-03-17 14:21:46.461564: message 3



```python
# rewriting with short circuting
def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
        
    print(f"{dt}: {msg}")
```


```python
log("message 2")
```

    2021-03-17 14:22:47.393956: message 2



```python
log("message 3")
```

    2021-03-17 14:22:53.717303: message 3

