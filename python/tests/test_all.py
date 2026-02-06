from datetime import date

import pytest

from datecalc import BusdayConvention, BusinessCalendar


@pytest.fixture
def holidays() -> list[date]:
    return [
        date(2026, 1, 1),
        date(2026, 1, 19),
        date(2026, 2, 16),
        date(2026, 5, 25),
        date(2026, 6, 19),
        date(2026, 7, 3),
        date(2026, 9, 7),
        date(2026, 10, 12),
        date(2026, 11, 11),
        date(2026, 11, 26),
        date(2026, 12, 25),
    ]


@pytest.fixture
def calendar(holidays: list[date]) -> BusinessCalendar:
    return BusinessCalendar(holidays=holidays, weekmask="1111100")


def test_no_op_cal() -> None:
    cal = BusinessCalendar()
    assert cal.holidays == []
    assert cal.weekmask == "1111100"


def test_is_holiday(calendar: BusinessCalendar, holidays: list[date]) -> None:
    rslt = [calendar.is_holiday(dt) for dt in holidays]
    assert all(rslt)


@pytest.mark.parametrize(
    argnames=["dt", "rslt"],
    argvalues=[
        (date(2026, 2, 5), date(2026, 2, 6)),
        (date(2026, 2, 6), date(2026, 2, 9)),
        (date(2026, 11, 10), date(2026, 11, 12)),
        (date(2026, 2, 13), date(2026, 2, 17)),
    ],
)
def test_succ(dt: date, rslt: date, calendar: BusinessCalendar) -> None:
    assert calendar.succ(dt) == rslt


@pytest.mark.parametrize(
    argnames=["dt", "conv", "rslt"],
    argvalues=[
        (date(2026, 2, 7), BusdayConvention.Following, date(2026, 2, 9)),
        (date(2026, 2, 7), BusdayConvention.Preceding, date(2026, 2, 6)),
        (date(2026, 1, 31), BusdayConvention.ModifiedFollowing, date(2026, 1, 30)),
        (date(2026, 2, 1), BusdayConvention.ModifiedPreceding, date(2026, 2, 2)),
    ],
)
def test_adjust(
    dt: date, conv: BusdayConvention, rslt: date, calendar: BusinessCalendar
) -> None: ...
