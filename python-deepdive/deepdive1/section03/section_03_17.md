# Garbage Collection

Reclaims memory when the reference count reaches 0, including circular references.

- can be controlled programmatically using the gc module
- by default it is turned on
- you may turn it off but if code creates circular references it will have memory leaks
- runs periodically on its own
- you can call it manually, and do your own cleanup

# Circular References

my_var --> objA.var_1 --> objB.var_2 ---> objA

objA and objB have a cirular reference, without GC, this would create a memory leak.


```python
import ctypes
import gc
```


```python
def ref_count(address):
    return ctypes.c_long.from_address(address).value
```


```python
# Check if address exists in the garbage collector
def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj)== object_id:
            return "Object exists"
    
    return "Not Found"
```

# Defining two classes for circular references


```python
class A:
    def __init__(self):
        self.b = B(self)
        print(f"A: self:{hex(id(self))}, b: {hex(id(self.b))}")
```


```python
class B:
    def __init__(self, a):
        self.a = a
        print(f"B: self:{hex(id(self))}, a: {hex(id(self.a))}")
```


```python
# disabling garbage collector
gc.disable()
```


```python
my_var = A()
```

    B: self:0x7f81bc3633d0, a: 0x7f81bc3633a0
    A: self:0x7f81bc3633a0, b: 0x7f81bc3633d0



```python
hex(id(my_var))
```




    '0x7f81bc3633a0'




```python
a_id = id(my_var)
b_id = id(my_var.b)
```


```python
print(hex(a_id))
print(hex(b_id))
```

    0x7f81bc3633a0
    0x7f81bc3633d0



```python
ref_count(a_id)
```




    2




```python
ref_count(b_id)
```




    1




```python
object_by_id(a_id)
```




    'Object exists'




```python
object_by_id(b_id)
```




    'Object exists'




```python
my_var = None
```

# Since garbage collection is off

- the circular reference continues to count as a memory reference



```python
ref_count(a_id)
```




    1




```python
ref_count(b_id)
```




    1




```python
object_by_id(a_id)
```




    'Object exists'




```python
object_by_id(b_id)
```




    'Object exists'



# Turning on garbage collection

- will reclaim the circular referenced memory locations


```python
gc.collect()
```




    636




```python
object_by_id(a_id)
```




    'Not Found'




```python
object_by_id(b_id)
```




    'Not Found'




```python
# Checking reference count

- it may output no zero value because Python could be using the recently claimed memory location
```


```python
ref_count(a_id)
```




    0




```python
ref_count(b_id)
```




    1


