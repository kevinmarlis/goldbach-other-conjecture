# goldbach-other-conjecture
Haskell and Python versions disproving Goldbach's other conjecture

PythonVersionA attempts is Haskell inspired, but deals with infinite lists 
in an inelegant way - by stopping them at 6000.

PythonVersionB is slightly faster than VersionA and works by incrementing through
odd numbers, checking if they are prime and if not, checking if they satisfy the
Goldbach condition (if odd-prime/2 is a perfect square).

The two Lists files compare how infinite lists work in both Haskell and Python.
