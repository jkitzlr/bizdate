# Home

`bizdate` is a python package, written in Rust, providing business calendar and business date functionality.

The primary interface for this functionality is the `BusinessCalendar` class. This class stores holiday and weekday information and exposes methods related to business date functionality.

## Usage

The two classes exposed by the library are BusinessCalendar and BusdayConvention:

```python
from bizdate import BusdayConvention, BusinessCalendar
```

To create a BusinessCalendar, provide a [Sequence](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) of holidays and a weekmask. The weekmask is a 7-digit bitstring indicating whether a given day of the week is a week (i.e., working) day, from Mon-Sun. For example, "1111100" is the default value and indicates that Monday-Friday are working days, Saturday and Sunday are not.

```python
>>> from datetime import date
>>> # create a sequence of dates representing holidays
>>> holidays = [
...     date(2026, 1, 1),
...     date(2026, 1, 19),
...     date(2026, 2, 16),
...     date(2026, 5, 25),
...     date(2026, 6, 19),
... ]
>>> # Mon-Fri are working days
>>> weekmask = "1111100"
>>> cal = BusinessCalendar(holidays=holidays, weekmask=weekmask)
>>> cal.is_holiday(date(2026, 1, 1))
True
```

The business calendar supports a variety of common business date-related tasks, including

### Adjusting non-business days

```python
>>> # a weekend date with a Monday holiday
>>> cal.adjust(date(2026, 2, 14), BusdayConvention.Following)
datetime.date(2026, 2, 17)
>>> cal.adjust(date(2026, 2, 28), BusdayConvention.ModifiedFollowing)
datetime.date(2026, 2, 27)
```

BusdayConvention supports following, modified following, preceding, modified preceding, or none conventions.

### Adding and subtracting business days

```python
>>> cal.add_busdays(date(2026, 1, 1), 20)
datetime.date(2026, 1, 30)
>>> # if starting dt isn't a business day, can adjust
>>> cal.add_busdays(date(2026, 1, 3), 20, BusdayConvention.Following)
datetime.date(2026, 2, 2)
>>> cal.sub_busdays(date(2026, 2, 2), 20, BusdayConvention.Following)
datetime.date(2026, 1, 2)
```

### Counting business days

```python
>>> cal.busday_count(date(2026, 1, 1), date(2026, 6, 30))
123
```
