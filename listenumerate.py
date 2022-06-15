Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ['Bannana', 'apple', 'mango']
>>> loud_fruits = [fruit.upper() for fruit in fruits]
>>> print(loud_fruits)
['BANNANA', 'APPLE', 'MANGO']
>>> list(enumerate(loud_fruits)
     print(list)
     
SyntaxError: invalid syntax
>>> list(enumerate(loud_fruits))
[(0, 'BANNANA'), (1, 'APPLE'), (2, 'MANGO')]
>>> 