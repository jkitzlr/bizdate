from datetime import date
from typing import Self

class BusinessCalendar:
    """Business calendar. TBD."""

    def __init__(self: Self, holidays: list[date], weekmask: str) -> Self: ...
    def is_weekday(self: Self, dt: date) -> bool:
        """Check whether ``dt`` is a weekday.

        Args:
            dt: The date to check.

        Returns:
            Whether ``dt`` is a weekday.
        """

    def is_holiday(self: Self, dt: date) -> bool:
        """Check whether ``dt`` is a holiday.

        Args:
            dt: The date to check.

        Returns:
            Whether ``dt`` is a holiday.
        """

    def is_busday(self: Self, dt: date) -> bool:
        """Check whether ``dt`` is a busday, i.e. a weekday that's not a holiday.

        Args:
            dt: The date to check.

        Returns:
            Whether ``dt`` is a business day.
        """
