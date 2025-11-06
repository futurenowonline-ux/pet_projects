def total_seconds(hours, minutes):
    """
    Convert hours and minutes to seconds, add them together, and return the total seconds.

    Args:
        hours (int): Number of hours (must be non-negative).
        minutes (int): Number of minutes (must be non-negative).

    Returns:
        int: Total seconds.

    Raises:
        TypeError: If hours or minutes are not integers.
        ValueError: If hours or minutes are negative.
    """
    if not isinstance(hours, int) or not isinstance(minutes, int):
        raise TypeError("Hours and minutes must be integers.")
    if hours < 0 or minutes < 0:
        raise ValueError("Hours and minutes must be non-negative.")
    return hours * 3600 + minutes * 60
