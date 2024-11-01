import re

def regex(value, pattern):
    """Check if the value matches the given regex pattern."""
    return bool(re.match(pattern, value))