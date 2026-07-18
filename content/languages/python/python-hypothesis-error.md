---
title: "Solved Python Hypothesis Error — How to Fix"
date: 2026-03-15T11:20:30+00:00
description: "Learn how to resolve Python Hypothesis property-based testing errors, shrinking failures, and flaky tests."
categories: ["python"]
keywords: ["python hypothesis", "hypothesis error", "property-based testing", "hypothesis shrinking", "flaky test"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

Hypothesis errors occur when property-based tests find edge cases that violate your specified properties. Unlike traditional tests, Hypothesis explores a vast input space and reports the smallest failing example it can find after "shrinking."

Common causes include:
- Test functions violate their `@given` invariants for certain inputs
- Strategies generate inputs outside the expected domain
- Stateful testing reveals invalid state transitions
- Tests are not idempotent and produce different results per run
- Decorator ordering conflicts with pytest fixtures

## Common Error Messages

```python
from hypothesis import given, strategies as st

@given(st.integers(min_value=1, max_value=100))
def test_division(x):
    result = 100 / x
    assert result > 0

# hypothesis.errors.Flaky: Hypothesis found a different example
```

```python
@given(st.text())
def test_encode_decode(s):
    encoded = s.encode("utf-8").decode("utf-8")
    assert encoded == s

# hypothesis.errors.InvalidArgument: invalid text strategy
```

```python
# Deadline exceeded
from hypothesis import given, settings

@given(st.integers())
@settings(deadline=100)  # 100ms
def test_slow(x):
    import time
    time.sleep(0.2)
    assert True

# Hypothesis: test exceeded deadline of 100ms
```

## How to Fix It

### 1. Fix Flaky Tests with Proper Settings

Configure Hypothesis settings to handle nondeterminism.

```python
from hypothesis import given, settings, HealthCheck
from hypothesis import strategies as st

@settings(
    suppress_health_check=[HealthCheck.too_slow],
    deadline=None,
    max_examples=500
)
@given(st.integers(min_value=1, max_value=1000))
def test_is_positive(x):
    result = abs(x)
    assert result >= 0

@settings(database=None)  # Disable database for deterministic tests
@given(st.lists(st.integers(), min_size=1, max_size=100))
def test_sort_preserves_length(lst):
    sorted_lst = sorted(lst)
    assert len(sorted_lst) == len(lst)
    assert all(sorted_lst[i] <= sorted_lst[i+1] for i in range(len(sorted_lst)-1))
```

### 2. Define Custom Strategies for Domain-Specific Input

Create strategies that generate valid inputs for your domain.

```python
from hypothesis import given, strategies as st
from hypothesis.stateful import RuleBasedStateMachine, rule

class PositiveNumberStrategy(st.SearchStrategy):
    def __init__(self, min_val=0, max_val=1000):
        self.min_val = min_val
        self.max_val = max_val
    
    def do_draw(self, data):
        return data.draw(st.floats(min_value=self.min_val, max_value=self.max_val))

# Or simpler: use composite
@st.composite
def valid_email(draw):
    user = draw(st.text(
        alphabet=st.characters(whitelist_categories=('L', 'N'), whitelist_characters='._-'),
        min_size=1, max_size=64
    ))
    domain = draw(st.sampled_from(["example.com", "test.org", "mail.dev"]))
    return f"{user}@{domain}"

@given(email=valid_email())
def test_email_format(email):
    assert "@" in email
    assert "." in email.split("@")[1]

# Stateful testing
class CalculatorMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.value = 0
    
    @rule(x=st.integers(min_value=1, max_value=100))
    def add(self, x):
        self.value += x
        assert self.value > 0
    
    @rule(x=st.integers(min_value=1, max_value=50))
    def subtract(self, x):
        self.value -= x

TestCalculator = CalculatorMachine.TestCase
```

### 3. Handle Shrinking and Debugging

Use Hypothesis output to debug minimal failing examples.

```python
from hypothesis import given, settings, Verbosity
from hypothesis import strategies as st

@settings(
    verbosity=Verbosity.verbose,  # Show detailed output
    max_examples=100,
    database=None  # Don't save to database during debugging
)
@given(st.dictionaries(
    keys=st.text(min_size=1, max_size=10),
    values=st.integers(),
    min_size=1
))
def test_dict_operations(data):
    merged = {**data, **data}
    assert len(merged) == len(data)

# Run with: hypothesis --verbose test_file.py
# Or use profile for different settings

from hypothesis import settings, Phase

@settings(
    phases=[Phase.generate, Phase.shrink],  # Skip target and decorate
    max_examples=200
)
@given(st.binary(min_size=1, max_size=100))
def test_binary_decode(data):
    try:
        decoded = data.decode("utf-8")
        assert isinstance(decoded, str)
    except UnicodeDecodeError:
        pass  # Expected for invalid UTF-8
```

## Common Scenarios

### Scenario 1: API Input Validation Testing

Testing that an API rejects invalid inputs:

```python
from hypothesis import given, settings
from hypothesis import strategies as st

@st.composite
def invalid_api_payload(draw):
    payload_type = draw(st.sampled_from(["empty", "oversized", "invalid_type"]))
    
    if payload_type == "empty":
        return {}
    elif payload_type == "oversized":
        return {"data": "x" * (1024 * 1024)}
    else:
        return {"data": draw(st.none())}

@settings(max_examples=100)
@given(payload=invalid_api_payload())
def test_api_rejects_invalid(payload):
    response = validate_api_input(payload)
    assert response.status_code == 400

def validate_api_input(payload):
    class MockResponse:
        def __init__(self, status):
            self.status_code = status
    
    if not payload or "data" not in payload:
        return MockResponse(400)
    if isinstance(payload["data"], str) and len(payload["data"]) > 1024:
        return MockResponse(400)
    if payload["data"] is None:
        return MockResponse(400)
    return MockResponse(200)
```

## Prevent It

- Use `@settings(database=None)` during development to avoid stale failures
- Set `deadline=None` for tests involving I/O or complex computation
- Define custom strategies for domain-specific valid inputs
- Run Hypothesis with `--hypothesis-seed` for reproducible failures
- Use `@settings(suppress_health_check=[])` to catch performance issues early