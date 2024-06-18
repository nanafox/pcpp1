import pytest

from advanced_oop.oop_advanced.labs.lab_time_interval import (
    TimeData,
    TimeInterval,
)


@pytest.mark.parametrize(
    "hours, minutes, seconds, expected_str",
    [
        (1, 30, 45, "01:30:45"),
        (0, 0, 0, "00:00:00"),
        (23, 59, 59, "23:59:59"),
    ],
    ids=["normal_time", "zero_time", "max_time"],
)
def test_time_interval_str(hours, minutes, seconds, expected_str):
    time_interval = TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    assert str(time_interval) == expected_str


@pytest.mark.parametrize(
    "hours, minutes, seconds, expected_total_seconds",
    [
        (1, 0, 0, TimeData.seconds_in_hour),
        (0, 1, 0, TimeData.seconds_in_minute),
        (0, 0, 1, 1),
        (1, 1, 1, TimeData.seconds_in_hour + TimeData.seconds_in_minute + 1),
    ],
    ids=["one_hour", "one_minute", "one_second", "mixed_time"],
)
def test_time_interval_total_seconds(
    hours, minutes, seconds, expected_total_seconds
):
    time_interval = TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    assert (
        time_interval._TimeInterval__total_seconds() == expected_total_seconds
    )


@pytest.mark.parametrize(
    "hours1, minutes1, seconds1, hours2, minutes2, seconds2, expected_result",
    [
        (1, 0, 0, 1, 0, 0, "02:00:00"),
        (0, 30, 0, 0, 30, 0, "01:00:00"),
        (0, 0, 30, 0, 0, 30, "00:01:00"),
    ],
    ids=["add_hours", "add_minutes", "add_seconds"],
)
def test_time_interval_add(
    hours1, minutes1, seconds1, hours2, minutes2, seconds2, expected_result
):
    time_interval1 = TimeInterval(
        hours=hours1, minutes=minutes1, seconds=seconds1
    )
    time_interval2 = TimeInterval(
        hours=hours2, minutes=minutes2, seconds=seconds2
    )

    result = time_interval1 + time_interval2

    assert str(result) == expected_result


@pytest.mark.parametrize(
    "hours1, minutes1, seconds1, hours2, minutes2, seconds2, expected_result",
    [
        (2, 0, 0, 1, 0, 0, "01:00:00"),
        (1, 0, 0, 0, 30, 0, "00:30:00"),
        (0, 1, 0, 0, 0, 30, "00:00:30"),
    ],
    ids=["subtract_hours", "subtract_minutes", "subtract_seconds"],
)
def test_time_interval_subtract(
    hours1, minutes1, seconds1, hours2, minutes2, seconds2, expected_result
):
    time_interval1 = TimeInterval(
        hours=hours1, minutes=minutes1, seconds=seconds1
    )
    time_interval2 = TimeInterval(
        hours=hours2, minutes=minutes2, seconds=seconds2
    )

    result = time_interval1 - time_interval2

    assert str(result) == expected_result


@pytest.mark.parametrize(
    "hours, minutes, seconds, factor, expected_result",
    [
        (1, 0, 0, 2, "02:00:00"),
        (0, 30, 0, 2, "01:00:00"),
        (0, 0, 30, 2, "00:01:00"),
    ],
    ids=["multiply_hours", "multiply_minutes", "multiply_seconds"],
)
def test_time_interval_multiply(
    hours, minutes, seconds, factor, expected_result
):
    time_interval = TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    result = time_interval * factor

    assert str(result) == expected_result


@pytest.mark.parametrize(
    "hours, minutes, seconds, expected_exception",
    [
        ("1", 0, 0, TypeError),
        (1, "0", 0, TypeError),
        (1, 0, "0", TypeError),
    ],
    ids=["invalid_hours", "invalid_minutes", "invalid_seconds"],
)
def test_time_interval_invalid_initialization(
    hours, minutes, seconds, expected_exception
):
    with pytest.raises(expected_exception):
        TimeInterval(hours=hours, minutes=minutes, seconds=seconds)


@pytest.mark.parametrize(
    "other, expected_exception",
    [
        ("1", TypeError),
        (1.5, TypeError),
        (None, TypeError),
    ],
    ids=["invalid_add_str", "invalid_add_float", "invalid_add_none"],
)
def test_time_interval_invalid_addition(other, expected_exception):
    time_interval = TimeInterval(hours=1, minutes=0, seconds=0)

    with pytest.raises(expected_exception):
        time_interval + other


@pytest.mark.parametrize(
    "other, expected_exception",
    [
        ("1", TypeError),
        (1.5, TypeError),
        (None, TypeError),
    ],
    ids=[
        "invalid_subtract_str",
        "invalid_subtract_float",
        "invalid_subtract_none",
    ],
)
def test_time_interval_invalid_subtraction(other, expected_exception):
    time_interval = TimeInterval(hours=1, minutes=0, seconds=0)

    with pytest.raises(expected_exception):
        time_interval - other


@pytest.mark.parametrize(
    "factor, expected_exception",
    [
        ("2", TypeError),
        (1.5, TypeError),
        (None, TypeError),
    ],
    ids=[
        "invalid_multiply_str",
        "invalid_multiply_float",
        "invalid_multiply_none",
    ],
)
def test_time_interval_invalid_multiplication(factor, expected_exception):
    time_interval = TimeInterval(hours=1, minutes=0, seconds=0)

    with pytest.raises(expected_exception):
        time_interval * factor
