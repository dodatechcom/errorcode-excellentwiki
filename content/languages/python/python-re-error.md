---
title: "[Solution] Python re Error — Regular Expression Issues"
description: "Fix re errors by doing X, Y, Z. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 612
---

# Python re Error — Regular Expression Issues

Regular expression errors include pattern syntax errors, catastrophic backtracking, incorrect group indexing, and infinite match loops. These can cause hangs, crashes, or incorrect results.

## Common Causes

```python
# Cause 1: Unclosed bracket or parenthesis in pattern
import re

pattern = r"[a-z"  # Unclosed character class
re.search(pattern, "hello")  # re.error: unterminated character set at position 0
```

```python
# Cause 2: Catastrophic backtracking with nested quantifiers
import re

# Pattern with overlapping alternatives causes exponential time
pattern = r"(a+)+b"
input_str = "a" * 30  # 30 'a's without a 'b'
re.match(pattern, input_str)  # Hangs — catastrophic backtracking
```

```python
# Cause 3: Using group index that doesn't exist
import re

pattern = r"(\w+) (\w+)"
match = re.search(pattern, "Hello World")
print(match.group(3))  # IndexError: no such group
```

```python
# Cause 4: Infinite match with zero-width pattern
import re

# Pattern that matches empty string infinitely
pattern = r"a*"
result = re.findall(pattern, "aaa")
print(result)  # ['', 'a', '', 'a', '', 'a', '', ''] — many empty matches
```

```python
# Cause 5: Escaping issues with special characters
import re

# Treating user input as raw regex without escaping
user_input = "price is $10.00"
pattern = user_input  # $ and . are special regex characters
re.search(pattern, "price is $10.00")  # re.error: nothing to repeat
```

## How to Fix

### Fix 1: Use re.escape for User-Provided Patterns

```python
import re

user_input = "price is $10.00"
safe_pattern = re.escape(user_input)  # 'price\\ is\\ \\$10\\.00'
result = re.search(safe_pattern, "the price is $10.00 today")
print(result.group())  # 'price is $10.00'
```

### Fix 2: Avoid Catastrophic Backtracking

```python
import re

# BAD — catastrophic backtracking
bad_pattern = r"(a+)+b"

# GOOD — atomic grouping or possessive quantifiers (Python 3.11+)
# Use possessive quantifier
good_pattern = r"a++b"  # a++ is possessive, prevents backtracking

# Or rewrite without nested quantifiers
good_pattern = r"a+b"

# Or use a non-backtracking regex engine
import regex  # pip install regex
pattern = regex.compile(r"(?:a{1,})b", regex.V1)  # regex module handles this better
```

### Fix 3: Validate Group Count Before Accessing

```python
import re

def safe_group(match, group_num, default=None):
    """Safely access a regex group with default."""
    if match is None:
        return default
    try:
        return match.group(group_num)
    except IndexError:
        return default

pattern = r"(\w+) (\w+)"
match = re.search(pattern, "Hello World")

first = safe_group(match, 1)    # "Hello"
second = safe_group(match, 2)   # "World"
third = safe_group(match, 3)    # None (no error)
```

### Fix 4: Use Word Boundaries to Prevent Partial Matches

```python
import re

# BAD — matches "cat" inside "concatenate"
pattern = r"cat"
match = re.search(pattern, "concatenate")
print(match.group())  # "cat" — unintended match

# GOOD — use word boundaries for whole-word matching
pattern = r"\bcat\b"
match = re.search(pattern, "concatenate")
print(match)  # None — correct, no whole word "cat"

# Match "cat" as a whole word
match = re.search(r"\bcat\b", "the cat sat")
print(match.group())  # "cat"
```

### Fix 5: Compile Patterns for Reuse and Debugging

```python
import re

# Compile for reuse — catches syntax errors early
EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

# Debug complex patterns with re.VERBOSE
PHONE_PATTERN = re.compile(r"""
    ^                           # Start of string
    (\+?\d{1,3})?               # Optional country code
    [\s.-]?                     # Optional separator
    (\(?\d{2,4}\)?)             # Area code, optionally parenthesized
    [\s.-]?                     # Optional separator
    (\d{3,4})                   # First part of number
    [\s.-]?                     # Optional separator
    (\d{3,4})                   # Second part of number
    $                           # End of string
""", re.VERBOSE)

# Test the pattern
match = PHONE_PATTERN.match("+1 (555) 123-4567")
if match:
    print(f"Country: {match.group(1)}, Area: {match.group(2)}")
```

## Examples

```python
# Production-grade input validation with compiled patterns
import re
from dataclasses import dataclass

@dataclass
class ValidationPatterns:
    EMAIL = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    PHONE = re.compile(r"^\+?[\d\s\-()]{7,15}$")
    UUID4 = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")
    IP_ADDR = re.compile(r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$")

def validate_input(data: dict) -> dict:
    errors = {}
    if 'email' in data and not ValidationPatterns.EMAIL.match(data['email']):
        errors['email'] = "Invalid email format"
    if 'phone' in data and not ValidationPatterns.PHONE.match(data['phone']):
        errors['phone'] = "Invalid phone format"
    return errors

# Handle regex errors gracefully
def safe_search(pattern, string, flags=0):
    try:
        return re.search(pattern, string, flags)
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        return None
```

## Related Errors

- [Python ValueError](/languages/python/valueerror/) — Value errors
- [Python TypeError](/languages/python/typeerror/) — Type errors
- [Python RecursionError](/languages/python/recursionerror/) — Maximum recursion depth
- [Python TimeoutError](/languages/python/timeouterror/) — Timeout errors
