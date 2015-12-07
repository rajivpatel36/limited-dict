limited-dict
============

This is a Python library which provides a dict-like structure which keeps elements sorted by value and maintains only the top or bottom N elements. It provides a memory efficient way of storing only the highest or lowest elements.

Installation
------------
You can install the library using pip:

.. code-block:: bash

   $ pip install limited_dict

Using the library
-----------------
You can create the dict-like structure as follows:

.. code:: python

    from limited_dict import LimitedDict

    my_dict = LimitedDict(max_length=50, cache_mapping=True, reverse_order=False)

The arguments are:

* ``max_length`` (required):
    This is the maximum number of elements to store.

* ``cache_mapping`` (optional):
    If this is ``True`` the mapping between keys and values is stored in a more efficient way. This improves performance at the expense of greater memory usage.

* ``reverse_order`` (optional):
    If this is ``False`` the elements with the lowest  ``max_length`` values are maintained. If this is ``True`` the elements with the highest ``max_length`` values are maintained.

The ``LimitedDict`` class can then be used like a ``dict``:

.. code:: bash

   >>> from limited_dict import LimitedDict
   >>> my_dict = LimitedDict(max_length=3, cache_mapping=False, reverse_order=False)
   >>> my_dict['a'] = 1
   >>> my_dict['b'] = 10
   >>> my_dict['c'] = 0
   >>> my_dict['d'] = 5
   >>> my_dict['e'] = 7
   >>> print my_dict
   >>> [('c', 0), ('a', 1), ('d', 5)]

It only stores ``max_length`` elements so some elements previously specified may no longer exist in the structure. Trying to access such elements will raise a ``KeyError``:

.. code:: bash

   >>> my_dict['e']
   >>> Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "limited_dict/limited_dict.py", line 48, in __getitem__
       raise KeyError(key)
   KeyError: 'e'
   >>> my_dict['c']
   >>> 0

You can iterate over keys and values in the same way as a dict:

.. code:: bash

   >>> for key, value in my_dict.items():
   ...    print("{key}:{value}".format(key=key, value=value))
   ...
   ...
   c:0
   a:1
   d:5