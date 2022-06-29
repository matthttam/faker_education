
# Education provider for Faker


## Acknowlegements


`faker_education` is a provider for the `Faker` Python package, and a fork of https://github.com/kennethwsmith/faker_airtravel.  I would like to thank the maintainer of that repository, since I used their structure to create this one.


## Description

`faker_education` provides education related fake data for testing purposes.  The definition of "fake" in this context really means "random," as the public institutions including names, districts, states, and other information are real.  However, I make no claims about accuracy, so do not use this as location data!

The data was provided for free from the authoritative source https://data-nces.opendata.arcgis.com/ published May 2, 2022.

## Installation

Install with pip:

``` bash
pip install faker_education
```

Add as a provider to your Faker instance:

``` python
from faker import Faker
from faker_education import SchoolProvider
fake.add_provider(SchoolProvider)
```

If you already use faker, you probably know the conventional use is:

```python
fake = Faker()
```


### School Object

``` python
>>> fake.school_object()
{
    "school": "Craig Elementary",
    "district": "Craig City School District",
    "level": "Elementary",
    "type": "Regular school",
    "state": "AK",
    "nces_id": "20009000629",
}

>>> fake.school_name()
'Glendening Elementary School'
```

### School NCES IDs

``` python
>>> fake.school_nces_id()
'390469702730'
```

### Districts

``` python
>>> fake.district()
'Sichuan Airlines'
```

### Level

``` python
>>> fake.school_level()
'Elementary'
```

### Type

``` python
>>> fake.school_type()
'Career and Technical School'
```

### State

``` python
>>> fake.school_state()
'KY'
```