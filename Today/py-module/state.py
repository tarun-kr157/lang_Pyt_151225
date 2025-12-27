import govt
print(f'Tax = {govt.tax}%')
govt.login()
instance = govt.Emp()
print()

import govt as modulefinder
print(f'Tax = {modulefinder.tax}%')
modulefinder.login()
instance = modulefinder.Emp()
print()

from govt import tax, login, Emp
print(f'Tax = {tax}%')
login()
instance = Emp()
print()

from govt import tax as tx, login as lgn, Emp as emp
print(f'Tax = {tx}%')
lgn()
instance = emp()
print()








   