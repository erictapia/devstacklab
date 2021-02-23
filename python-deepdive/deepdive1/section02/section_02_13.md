# Classes

- Two steps when creating a new instance
- step 1: create an instance
- step 2: call __init__ method


```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self.width = width
        self.height = height

```


```python
r1 = Rectangle(10, 20)
r1.width
```




    10




```python
r1.width = 100
r1.width
```




    100




```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self.width = width
        self.height = height

        
    def area(self):
        return self.width * self.height

    
    def perimeter(self):
        return 2 * self.area()

```


```python
r1 = Rectangle(10, 20)
r1.area()
```




    200




```python
r1.perimeter()
```




    400




```python
# String representation of a Rectangle object
str(r1)
```




    '<__main__.Rectangle object at 0x7f2cf007a7c0>'




```python
hex(id(r1))
```




    '0x7f2cf007a7c0'



# Special methods

- \__str__
- \__repr__
- \__eq__
- \__lt__



```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self.width = width
        self.height = height

        
    def area(self):
        return self.width * self.height

    
    def perimeter(self):
        return 2 * self.area()

    
    def __str__(self):
        # This is a special method is used to convert to a string
        return f"Rectangle: width={self.width}, height={self.height}"
```


```python
r1 = Rectangle(10, 20)
str(r1)
```




    'Rectangle: width=10, height=20'




```python
r1
```




    <__main__.Rectangle at 0x7f2cf007a9d0>




```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self.width = width
        self.height = height

        
    def area(self):
        return self.width * self.height

    
    def perimeter(self):
        return 2 * self.area()

    
    def __str__(self):
        # This is a special method is used to convert to a string
        return f"Rectangle: width={self.width}, height={self.height}"
    
    
    def __repr__(self):
        # This is a special method typically used to represent how this object would be created
        return f"Rectangle({self.width}, {self.height})"

```


```python
r1 = Rectangle(10, 20)
r1
```




    Rectangle(10, 20)




```python
r2 = Rectangle(10, 20)
```


```python
# Testing memory address
r1 is not r2
```




    True




```python
# Testing value, not implemented
r1 == r2
```




    False




```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self.width = width
        self.height = height

        
    def area(self):
        return self.width * self.height

    
    def perimeter(self):
        return 2 * self.area()

    
    def __str__(self):
        # This is a special method is used to convert to a string
        return f"Rectangle: width={self.width}, height={self.height}"
    
    
    def __repr__(self):
        # This is a special method typically used to represent how this object would be created
        return f"Rectangle({self.width}, {self.height})"
    
    
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

```


```python
r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
```


```python
# Testing if not same memory location
r1 is not r2
```




    True




```python
# Testing if same values
r1 == r2
```




    True




```python
# comparing to non Rectangle
r1 == 100
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-35-7b227cedb3f6> in <module>
    ----> 1 r1 == 100
    

    <ipython-input-30-60247f507393> in __eq__(self, other)
         25 
         26     def __eq__(self, other):
    ---> 27         return self.width == other.width and self.height == other.height
    

    AttributeError: 'int' object has no attribute 'width'



```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self.width = width
        self.height = height

        
    def area(self):
        return self.width * self.height

    
    def perimeter(self):
        return 2 * self.area()

    
    def __str__(self):
        # This is a special method is used to convert to a string
        return f"Rectangle: width={self.width}, height={self.height}"
    
    
    def __repr__(self):
        # This is a special method typically used to represent how this object would be created
        return f"Rectangle({self.width}, {self.height})"
    
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        
        return False    

```


```python
r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
```


```python
r1 == r2
```




    True




```python
r1 == 100
```




    False




```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self.width = width
        self.height = height

        
    def area(self):
        return self.width * self.height

    
    def perimeter(self):
        return 2 * self.area()

    
    def __str__(self):
        # This is a special method is used to convert to a string
        return f"Rectangle: width={self.width}, height={self.height}"
    
    
    def __repr__(self):
        # This is a special method typically used to represent how this object would be created
        return f"Rectangle({self.width}, {self.height})"
    
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        
        return False    

    
    def __lt__(self, other):
        # Area will be used to verify less than other
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        
        return NotImplemented

```


```python
r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)
```


```python
r1 < r2
```




    True




```python
r2 < r1
```




    False




```python
# comparing to a non-Rectangle
r1 < 1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-53-d7d3051d6ade> in <module>
          1 # comparing to a non-Rectangle
    ----> 2 r1 < 1
    

    TypeError: '<' not supported between instances of 'Rectangle' and 'int'



```python
# Its not implemented but Python flips it to make it work
r2 > r1
```




    True



# Getter and Setter


```python
r1 = Rectangle(10, 20)
```


```python
r1.width
```




    10




```python
# Direct access to attribute and allows invalid values
r1.width = -100
```


```python
r1.width
```




    -100




```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        # By convention a _, let users know the attributes are meant to be private
        self._width = width
        self._height = height

    
    def get_width(self):
        return self._width
    
    
    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width
    
        
    def area(self):
        return self._width * self._height

    
    def perimeter(self):
        return 2 * self.area()

    
    def __str__(self):
        # This is a special method is used to convert to a string
        return f"Rectangle: width={self._width}, height={self._height}"
    
    
    def __repr__(self):
        # This is a special method typically used to represent how this object would be created
        return f"Rectangle({self._width}, {self._height})"
    
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        
        return False    

    
    def __lt__(self, other):
        # Area will be used to verify less than other
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        
        return NotImplemented

```


```python
r1 = Rectangle(10, 20)
```


```python
# Attribute does not exist
r1.width
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-58-0fef21a529ba> in <module>
    ----> 1 r1.width
    

    AttributeError: 'Rectangle' object has no attribute 'width'



```python
# Monkey patching, adding a property at runtime
r1.width = -100
```


```python
r1.width
```




    -100




```python
r1._width
```




    10




```python
r1
```




    Rectangle(10, 20)




```python
r1.get_width()
```




    10




```python
# setting to invalid value
r1.set_width(-10)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-64-cc061d39edc3> in <module>
          1 # setting to invalid value
    ----> 2 r1.set_width(-10)
    

    <ipython-input-56-a0049b9a0e39> in set_width(self, width)
         13     def set_width(self, width):
         14         if width <= 0:
    ---> 15             raise ValueError("Width must be positive")
         16         else:
         17             self._width = width


    ValueError: Width must be positive



```python
r1.set_width(100)
```


```python
r1
```




    Rectangle(100, 20)




```python
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self._width = width
        self._height = height

    
    @property
    def width(self):
        # Getter for width
        print("Width property called")
        return self._width
    
    
    @width.setter
    def width(self, width):
        # Setter for width
        print("Width setter called")
        
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width
        
    
    @property
    def height(self):
        # Getter for height
        print("Height property called")
        return self._height
   
    
    @height.setter
    def height(self, height):
        # Setter for height
        print("Height setter called")
        
        if heigth <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height
            
        
    def area(self):
        return self.width * self.height

    
    def perimeter(self):
        return 2 * self.area()

    
    def __str__(self):
        # This is a special method is used to convert to a string
        return f"Rectangle: width={self.width}, height={self.height}"
    
    
    def __repr__(self):
        # This is a special method typically used to represent how this object would be created
        return f"Rectangle({self.width}, {self.height})"
    
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        
        return False    

    
    def __lt__(self, other):
        # Area will be used to verify less than other
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        
        return NotImplemented

```


```python
r1 = Rectangle(10, 20)
```


```python
r1
```

    Width property called
    Height property called





    Rectangle(10, 20)




```python
r1.width
```

    Width property called





    10




```python
r1.height
```

    Height property called





    20




```python
r1.width = -100
```

    Width setter called



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-85-7febe5f9cdf2> in <module>
    ----> 1 r1.width = -100
    

    <ipython-input-80-3693e9715175> in width(self, width)
         19 
         20         if width <= 0:
    ---> 21             raise ValueError("Width must be positive")
         22         else:
         23             self._width = width


    ValueError: Width must be positive



```python
r1.width = 100
```

    Width setter called



```python
r1
```

    Width property called
    Height property called





    Rectangle(100, 20)




```python
# Creating instance with a negative number
r1 = Rectangle(-100, 100)
```


```python
r1
```

    Width property called
    Height property called





    Rectangle(-100, 100)




```python
# Fixing the init so it doesn't allow negative nubmers
# This is done by using the setter instead of assign directly
class Rectangle:
    # by convention, first argument is self for instance objects
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    @property
    def width(self):
        # Getter for width
        print("Width property called")
        return self._width
    
    
    @width.setter
    def width(self, width):
        # Setter for width
        print("Width setter called")
        
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width
        
    
    @property
    def height(self):
        # Getter for height
        print("Height property called")
        return self._height
   
    
    @height.setter
    def height(self, height):
        # Setter for height
        print("Height setter called")
        
        if heigth <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height
            
        
    def area(self):
        return self.width * self.height

    
    def perimeter(self):
        return 2 * self.area()

    
    def __str__(self):
        # This is a special method is used to convert to a string
        return f"Rectangle: width={self.width}, height={self.height}"
    
    
    def __repr__(self):
        # This is a special method typically used to represent how this object would be created
        return f"Rectangle({self.width}, {self.height})"
    
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        
        return False    

    
    def __lt__(self, other):
        # Area will be used to verify less than other
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        
        return NotImplemented

```


```python
r1 = Rectangle(-100, 100)
```

    Width setter called



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-91-a66a705986f8> in <module>
    ----> 1 r1 = Rectangle(-100, 100)
    

    <ipython-input-90-b7aad4473f3e> in __init__(self, width, height)
          4     # by convention, first argument is self for instance objects
          5     def __init__(self, width, height):
    ----> 6         self.width = width
          7         self.height = height
          8 


    <ipython-input-90-b7aad4473f3e> in width(self, width)
         21 
         22         if width <= 0:
    ---> 23             raise ValueError("Width must be positive")
         24         else:
         25             self._width = width


    ValueError: Width must be positive



```python

```
