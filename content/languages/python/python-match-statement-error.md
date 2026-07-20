---
title: "[Solution] Python 3.10 Match/Case Statement Error — Pattern Syntax and Usage"
description: "Fix Python 3.10+ match/case statement errors including pattern syntax errors, capture vs OR patterns, guard clauses, and subject type mismatches."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 507
---

# Python 3.10 Match/Case Statement Error — Pattern Syntax and Usage

Python 3.10 introduced structural pattern matching with `match`/`case` statements. Common errors include confusing capture patterns with OR patterns, incorrect guard clause syntax, and type mismatch issues when the subject doesn't support the pattern type.

## Common Causes

```python
# Cause 1: Confusing capture pattern with OR pattern
match command:
    case "quit" | "exit":  # This is correct OR pattern
        print("Exiting")
    case str(x):  # Error — str() is not a valid pattern
        print(f"Got string: {x}")

# Cause 2: Wrong guard clause syntax
match value:
    case x if x > 0:  # Fine, but common mistake: case x where x > 0
        print("positive")

# Cause 3: Matching on unsupported subject types
match 42:
    case {"key": value}:  # Error — can't match dict pattern on int
        print(value)

# Cause 4: Duplicate capture patterns
match value:
    case x:
        print("first")
    case x:  # Error — x already captured
        print("second")

# Cause 5: Incorrect class pattern usage
match obj:
    case Point(x, y):  # Error if Point doesn't have __match_args__
        print(x, y)
```

## How to Fix

### Fix 1: Use correct pattern syntax for strings

```python
# Wrong — trying to use str() as pattern constructor
match command:
    case str(x):  # This tries to match str objects, not capture string content
        print(x)

# Correct — use capture pattern directly
match command:
    case str() as s:  # Matches any str, binds to s
        print(f"Got string: {s}")
    case int() as n:  # Matches any int
        print(f"Got int: {n}")

# For specific values
match command:
    case "quit" | "exit":
        print("Exiting")
    case "help":
        print("Available commands: quit, exit, help")
    case other:
        print(f"Unknown: {other}")
```

### Fix 2: Use correct guard clause syntax

```python
# Wrong — guard clause with "where"
match value:
    case x where x > 0:  # SyntaxError
        print("positive")

# Correct — use "if" keyword
match value:
    case x if x > 0:
        print("positive")
    case x if x < 0:
        print("negative")
    case 0:
        print("zero")
```

### Fix 3: Match the subject type to the pattern

```python
# Wrong — dict pattern on non-dict subject
match 42:
    case {"key": value}:  # TypeError or just won't match
        print(value)

# Correct — ensure subject is a dict
data = {"key": "value", "other": 123}
match data:
    case {"key": value, "other": int(n)}:
        print(f"key={value}, n={n}")
    case {"key": value}:
        print(f"key={value}")
    case _:
        print("Unknown structure")
```

### Fix 4: Avoid duplicate capture patterns

```python
# Wrong — duplicate variable names in patterns
match value:
    case x:
        print("first match")
    case x:  # Error — x is already bound
        print("second match")

# Correct — use different names or wildcards
match value:
    case x if isinstance(x, str):
        print(f"String: {x}")
    case x if isinstance(x, int):
        print(f"Int: {x}")
    case _:
        print("Other")

# Or restructure with elif-style logic
match value:
    case str(s):
        print(f"String: {s}")
    case int(n):
        print(f"Int: {n}")
```

### Fix 5: Define __match_args__ for class patterns

```python
# Wrong — class without __match_args__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

match Point(1, 2):
    case Point(x, y):  # Error — Point has no __match_args__
        print(x, y)

# Correct — define __match_args__
class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

match Point(1, 2):
    case Point(x, y):  # Works — x=1, y=2
        print(x, y)
    case Point(x=x_val, y=0):  # Keyword pattern
        print(f"x={x_val}, on x-axis")
```

## Examples

```python
# HTTP status code matching
def handle_status(code):
    match code:
        case 200:
            return "OK"
        case 301 | 302:
            return "Redirect"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case c if 200 <= c < 300:
            return f"Success ({c})"
        case c if 400 <= c < 500:
            return f"Client Error ({c})"
        case _:
            return f"Unknown: {c}"

# Nested pattern matching with data structures
def process_message(msg):
    match msg:
        case {"type": "text", "content": str(text), "user": str(user)}:
            print(f"{user}: {text}")
        case {"type": "image", "url": str(url)}:
            print(f"Image: {url}")
        case {"type": "system", "action": "join"}:
            print("User joined")
        case _:
            print("Unknown message type")

# Class pattern matching with inheritance
class Success:
    __match_args__ = ("value",)
    def __init__(self, value):
        self.value = value

class Error:
    __match_args__ = ("message",)
    def __init__(self, message):
        self.message = message

def handle_result(result):
    match result:
        case Success(value) if value > 0:
            print(f"Positive success: {value}")
        case Success(value):
            print(f"Success: {value}")
        case Error(msg) if "timeout" in msg:
            print(f"Timeout error: {msg}")
        case Error(msg):
            print(f"Error: {msg}")
```

## Related Errors

- [SyntaxError](../syntaxerror) — Syntax errors when using invalid pattern syntax
- [TypeError](../typeerror) — Type mismatches in pattern matching
- [python-positional-only-params](../python-positional-only-params) — Positional-only parameter syntax
- [python310-deprecation](../python310-deprecation) — Python 3.10 deprecation changes
