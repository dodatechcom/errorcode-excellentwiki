---
title: "[Solution] Python collections Error — Module Usage and Data Structure Errors"
description: "Fix Python collections errors including defaultdict, OrderedDict, Counter, namedtuple, deque, and more. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 221
---

# Python collections Error — Module Usage and Data Structure Errors

The `collections` module provides specialized container data types. Errors arise from incorrect usage of defaultdict, Counter, OrderedDict, namedtuple, deque, ChainMap, and UserDict.

## Common Causes

```python
from collections import defaultdict

# Error: Calling a defaultdict with a non-callable default
d = defaultdict("missing")
d["key"]
# TypeError: first argument must be callable or None
```

```python
from collections import namedtuple

# Error: Invalid field names in namedtuple
Point = namedtuple("Point", ["class", "return", "123invalid"])
# ValueError: Field names cannot be keywords or start with a number
```

```python
from collections import deque

# Error: deque with negative maxlen
dq = deque(maxlen=-1)
# ValueError: deque max size must be non-negative
```

```python
from collections import Counter

# Error: Counter with non-iterable argument
c = Counter(42)
# TypeError: 'int' object is not iterable
```

```python
from collections import OrderedDict

# Error: Mutating OrderedDict during iteration
od = OrderedDict([("a", 1), ("b", 2)])
for k in od:
    del od[k]
# RuntimeError: dictionary changed size during iteration
```

## How to Fix

### Fix 1: Use a Callable as the Default Factory

```python
from collections import defaultdict

# Correct: pass a callable (e.g., int, list, str)
d = defaultdict(int)         # default value: 0
d = defaultdict(list)        # default value: []
d = defaultdict(lambda: "N/A")  # custom default

d["key"] += 1  # Works: d["key"] is now 1
```

### Fix 2: Use Valid Field Names for namedtuple

```python
from collections import namedtuple

# Field names must be valid identifiers and not Python keywords
Point = namedtuple("Point", ["x", "y", "z"])

# If you need invalid-looking names, pass a list of strings
# that are valid identifiers
Fields = namedtuple("Fields", ["_x", "data", "value"])
```

### Fix 3: Use a Positive maxlen for deque

```python
from collections import deque

# Correct: non-negative maxlen or None for unlimited
dq = deque(maxlen=10)   # bounded deque
dq = deque()             # unbounded deque
dq = deque(maxlen=0)     # valid but always empty
```

### Fix 4: Pass an Iterable to Counter

```python
from collections import Counter

# Correct: pass an iterable, dict, or keyword args
c = Counter([1, 2, 2, 3])          # from iterable
c = Counter({"a": 4, "b": 2})      # from mapping
c = Counter(a=4, b=2)              # from kwargs
```

## Examples

```python
from collections import defaultdict, Counter, deque

# Build a word frequency counter
text = "the cat sat on the mat the cat"
words = text.split()
freq = Counter(words)
print(freq.most_common(3))
# [('the', 3), ('cat', 2), ('sat', 1)]

# Group items with defaultdict
students = [("A", 90), ("B", 85), ("A", 95), ("B", 88)]
grade_groups = defaultdict(list)
for grade, score in students:
    grade_groups[grade].append(score)
# {'A': [90, 95], 'B': [85, 88]}

# Sliding window with deque
window = deque(maxlen=3)
for val in [1, 2, 3, 4, 5]:
    window.append(val)
    print(list(window))
```

## Related Errors

- [Python dict Error](/languages/python/python-dict-error/)
- [Python TypeError](/languages/python/python-typeerror/)
- [Python ValueError](/languages/python/python-valueerror/)
