def remove_duplicates(items):
    """
    Remove duplicate items from a list while preserving their original order.

    Args:
        items (list): Array of any items (any type). Comparison is case-sensitive.

    Returns:
        list: A new list with duplicates removed, preserving original sequence.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
