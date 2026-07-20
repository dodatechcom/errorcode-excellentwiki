---
title: "[Solution] Python random Error — Random Module Errors"
description: "Fix Python random errors including SystemRandom, seed errors, choice IndexError, and sample population too large. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 226
---

# Python random Error — Random Module Errors

The `random` module generates pseudo-random numbers. Errors involve seed initialization, index errors when choosing from empty sequences, and sample population size mismatches.

## Common Causes

```python
import random

# Error: choice from an empty sequence
random.choice([])
# IndexError: Cannot choose from an empty sequence
```

```python
import random

# Error: sample population smaller than sample size
random.sample(range(5), k=10)
# ValueError: Sample larger than population or is negative
```

```python
import random

# Error: Invalid seed type (in some Python versions)
random.seed([1, 2, 3])
# TypeError: an integer is required
```

```python
import random

# Error: uniform with inverted range
random.uniform(10, 5)  # This actually works but may confuse
# No error, but behavior may be unexpected — returns value in [5, 10]
```

```python
import random

# Error: SystemRandom cannot be seeded
sr = random.SystemRandom()
sr.seed(42)
# AttributeError: 'SystemRandom' object has no attribute 'seed'
```

## How to Fix

### Fix 1: Check Sequence Is Non-Empty Before choice

```python
import random

def safe_choice(seq):
    if not seq:
        raise ValueError("Cannot choose from an empty sequence")
    return random.choice(seq)

items = [1, 2, 3]
print(safe_choice(items))  # random item from list

# Or use a default
items = []
result = random.choice(items) if items else None
```

### Fix 2: Ensure Sample Size Does Not Exceed Population

```python
import random

population = list(range(5))
k = min(10, len(population))
sample = random.sample(population, k=k)
print(sample)  # up to 5 items

# Or use choices (with replacement) for large samples
random.choices(population, k=10)
```

### Fix 3: Use a Valid Seed Type

```python
import random

# Use int, bytes, or None as seed
random.seed(42)          # int
random.seed(b"seed")     # bytes
random.seed(None)        # system time (default)

# For reproducibility with complex seeds, hash them
seed_value = hash(("experiment", 1, 2))
random.seed(seed_value)
```

### Fix 4: Don't Seed SystemRandom

```python
import random

# SystemRandom uses OS entropy — no seed needed
sr = random.SystemRandom()
value = sr.random()  # cryptographically secure random
items = [1, 2, 3, 4, 5]
secure_choice = sr.choice(items)
```

## Examples

```python
import random

# Reproducible experiment
random.seed(42)
results = [random.randint(1, 100) for _ in range(5)]
print(results)  # same every time with seed 42

# Weighted random choices
colors = ["red", "green", "blue"]
weights = [0.5, 0.3, 0.2]
chosen = random.choices(colors, weights=weights, k=10)
print(chosen)

# Shuffle in place
deck = list(range(1, 53))
random.shuffle(deck)
print(deck[:5])  # first 5 cards
```

## Related Errors

- [Python IndexError](/languages/python/python-indexerror/)
- [Python ValueError](/languages/python/python-valueerror/)
- [Python AttributeError](/languages/python/python-attributeerror/)
