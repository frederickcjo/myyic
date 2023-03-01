# MyyIC
This is a simple Python package to validate and generate random Malaysia's National Registration Identity Card (NRIC) 
which also known as MyKad or simply IC (Identity Card).

# Installation
You can simply install it via Python's PIP:
```python
pip install -i https://test.pypi.org/simple/ myyic
```

# Validate MyKad
You can check the validity of MyKad / NRIC number.  
```python
from myyic import validate_myyic

input_mykad = '870120127991'

if (validate_myyic.nric(input_mykad)):
    print('Valid MyKad')
```

# Generate MyKad
You can generate random, valid MyKad with self-defined Gender, Birthplace or Separator.
```python
from myyic import random_myyic

# Generate Random MyKad
random_myyic.generate()

# Generate Random MyKad for Female
random_myyic.generate(gender='F')
# Generate Random MyKad for Male
random_myyic.generate(gender='M')

# Generate Random MyKad with Specific Birthplace Abbreviation
# You can check below for the all available birthplace
random_myyic.generate(state='SGR')

# Generate Random MyKad with Specific Separator. 
# By default, it will be dash '-'
random_myyic.generate()              # Output : 870120-12-7991 
random_myyic.generate(separator='-') # Output : 870120-12-7991 
random_myyic.generate(separator='')  # Output : 870120127991 
```

## Birthplace Available
Birthplace is only limited to actual state in Malaysia.

| State           | Abbreviation |
|-----------------|--------------|
| Johor           | JHR          |
| Kedah           | KDH          |
| Kelantan        | KTN          |
| Kuala Lumpur    | KUL          |
| Labuan          | LBN          |
| Melaka          | MLK          |
| Negeri Sembilan | NSN          |
| Pahang          | PHG          |
| Penang          | PNG          |
| Perak           | PRK          |
| Perlis          | PLS          |
| Putrajaya       | PJY          |
| Sabah           | SBH          |
| Sarawak         | SWK          |
| Selangor        | SGR          |
| Terengganu      | TRG          |





# Reference
https://www.jpn.gov.my/my/kod-negeri
