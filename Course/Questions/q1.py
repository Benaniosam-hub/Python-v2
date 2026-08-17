'''
What are the three distinct numeric types
supported in Python, and how do they differ 
from Python 2 to Python 3?
'''
int = 12
float = 2.5
complex = 4j

from decimal import Decimal
print (Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))

print(round(2.6))
print(round(4.8))

print(bool(0.5))
print(bool(-2.0))

