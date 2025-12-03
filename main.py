
def summarize_adoptions(adoptions):
    """
    Given a list of animal type strings, return a dictionary mapping each
    distinct animal type to how many times it appears in the list.

    Example:
    summarize_adoptions(["cat", "dog", "cat"]) -> {"cat": 2, "dog": 1}
    """
    counts = {}
    for animal in adoptions:
        # Animal can be any string (including ""), and case is preserved
        counts[animal] = counts.get(animal, 0) + 1
    return counts
