'''
python_implementation()→ returns a string denoting the Python implementation (expect 'CPython' here, unless you decide to use any non-canonical Python branch)
python_version_tuple()→ returns a three-element tuple filled with:
the major part of Python’s version;
the minor part;
the patch level number.
'''
from platform import *
print(python_implementation())
for atr in python_version_tuple():
    print(atr)
