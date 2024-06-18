"""
Lab 1 - A time interval app

Scenario

    - Create a class representing a time interval;
    - the class should implement its own method for addition, subtraction on
      time interval class objects;
    - the class should implement its own method for multiplication of time
      interval class objects by an integer-type value;
    - the __init__ method should be based on keywords to allow accurate and
      convenient object initialization, but limit it to hours, minutes, and
      seconds parameters;
    - the __str__ method should return an HH:MM:SS string, where HH represents
      hours, MM represents minutes and SS represents the seconds attributes of
      the time interval object;
    - check the argument type, and in case of a mismatch, raise a TypeError
      exception.

Lab 2 - An improvement of existing solution

Scenario

    - Extend the class implementation prepared in the previous lab to support
      the addition and subtraction of integers to time interval objects;
    - to add an integer to a time interval object means to add seconds;
    - to subtract an integer from a time interval object means to remove
      seconds.
"""

import operator
from typing import Union


class TimeData:
    """
    Represents a class for storing time data.

    Attributes:
        seconds_in_hour (int): The number of seconds in an hour.
        seconds_in_minute (int): The number of seconds in a minute.
    """

    seconds_in_hour: int = 3600
    seconds_in_minute: int = 60


class TimeInterval:
    """
    Represents a time interval in hours, minutes, and seconds.
    """

    __slots__ = ["hours", "minutes", "seconds"]

    def __init__(self, *, hours: int, minutes: int, seconds: int) -> None:
        """
        Initializes a TimeInterval object.

        Args:
            hours (int): The number of hours.
            minutes (int): The number of minutes.
            seconds (int): The number of seconds.

        Raises:
            TypeError: If any of the arguments are not of type int.
        """
        for arg in [hours, minutes, seconds]:
            self.check_type(arg=arg, expected_type=int)

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @staticmethod
    def check_type(*, arg, expected_type):
        """
        Checks if the given argument is of the expected type.

        Args:
            arg: The argument to check.
            expected_type: The expected type of the argument.

        Raises:
            TypeError: If the argument is not of the expected type.
        """
        if not isinstance(arg, expected_type):
            raise TypeError(
                "invalid value provided, expected an object of type "
                f"{expected_type.__name__}."
            )

    def __add__(self, other: "TimeInterval") -> "TimeInterval":
        """
        Adds two TimeInterval objects together.

        Args:
            other (TimeInterval): The TimeInterval object to add.

        Returns:
            TimeInterval: The sum of the two TimeInterval objects.

        Raises:
            TypeError: If the other argument is not of type TimeInterval or
            int.
        """
        self.check_type(arg=other, expected_type=Union[TimeInterval, int])
        return self.__perform_operation(other=other, operator=operator.add)

    def __sub__(self, other: "TimeInterval") -> "TimeInterval":
        """
        Subtracts one TimeInterval object from another.

        Args:
            other (TimeInterval): The TimeInterval object to subtract.

        Returns:
            TimeInterval: The difference between the two TimeInterval objects.

        Raises:
            TypeError: If the other argument is not of type TimeInterval or
            int.
        """
        self.check_type(arg=other, expected_type=Union[TimeInterval, int])
        return self.__perform_operation(other=other, operator=operator.sub)

    def __mul__(self, factor: int) -> "TimeInterval":
        """
        Multiplies a TimeInterval object by a factor.

        Args:
            factor (int): The factor to multiply by.

        Returns:
            TimeInterval: The product of the TimeInterval object and the factor.

        Raises:
            TypeError: If the factor argument is not of type int.
        """
        self.check_type(arg=factor, expected_type=int)
        return self.__perform_operation(other=factor, operator=operator.mul)

    def __perform_operation(
        self, *, other: Union[int, "TimeInterval"], operator: operator
    ) -> "TimeInterval":
        """
        Performs the specified operation on the TimeInterval object.

        Args:
            other (int or TimeInterval): The other operand for the operation.
            operator (operator): The operator to perform the operation.

        Returns:
            TimeInterval: The result of the operation.

        Raises:
            TypeError: If the other argument is not of type int or
            TimeInterval.
        """
        if isinstance(other, int):
            total_seconds = operator(self.__total_seconds(), other)
        else:
            total_seconds = operator(
                self.__total_seconds(), other.__total_seconds()
            )
        hours, minutes, seconds = self.__convert_seconds_to_hms(
            total_seconds=total_seconds
        )
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def __total_seconds(self) -> int:
        """
        Calculates the total number of seconds in the TimeInterval object.

        Returns:
            int: The total number of seconds.
        """
        return (
            (self.hours * TimeData.seconds_in_hour)
            + (self.minutes * TimeData.seconds_in_minute)
            + self.seconds
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the TimeInterval object.

        Returns:
            str: The string representation of the TimeInterval object.
        """
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    @staticmethod
    def __convert_seconds_to_hms(*, total_seconds: int) -> tuple:
        """
        Converts the total number of seconds to hours, minutes, and seconds.

        Args:
            total_seconds (int): The total number of seconds.

        Returns:
            tuple: A tuple containing the hours, minutes, and seconds.
        """
        hours = total_seconds // TimeData.seconds_in_hour
        remaining_seconds = total_seconds % TimeData.seconds_in_hour
        minutes = remaining_seconds // TimeData.seconds_in_minute
        seconds = remaining_seconds % TimeData.seconds_in_minute

        return hours, minutes, seconds


if __name__ == "__main__":
    interval1 = TimeInterval(hours=21, minutes=58, seconds=50)
    interval2 = TimeInterval(hours=1, minutes=45, seconds=22)

    assert str(interval1 + interval2) == "23:44:12"
    assert str(interval1 - interval2) == "20:13:28"
    assert str(interval1 * 2) == "43:57:40"
    assert str(interval1 + 62) == "21:59:52"
    assert str(interval1 - 62) == "21:57:48"
