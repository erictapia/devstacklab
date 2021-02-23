# Identifier names

are case-sensitive, must follow certain rules, and must follow certain conventions

## *Must*

- start with underscore (_) or letter (a-zA-Z)
- followed by any number of underscores (_), letters (a-zA-Z), or digits (0-9)
- cannot be reserved words

## *Conventions*

- first character is single underscore (_) is used to indicate "internal use"
or "private" objects; Objects named this way will not get imported by a
statement such as:

    ```python
    from module import *
    ```

- first characters is double underscore, dunder, ( __ ) is used to "mangle"
class attributes -- useful in inheritance chains
- starts and ends with dunder characters used for system-defined names that
have a special meaning to the interpreter; Don't invent them, stick to the ones
pre-defined by Python.
- Packages should be short, all-lowercase names, preferably no underscores
- Modules should be short, all-lowercase names, can have underscores
- Classes should be upper camel case (CapWords)
- Functions should be lowercase, words separated by underscores (snake_case)
- Variables should be lowercase, words separated by underscores (snake_case)
- Constants should be all-uppercase, words separated by underscores

[PEP 8](https://www.python.org/dev/peps/pep-0008)
