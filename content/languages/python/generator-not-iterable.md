---
title: "[Solution] Python TypeError — 'generator' object is not iterable"
description: "Fix Python TypeError: 'generator' object is not iterable. Learn why generators can only be consumed once and how to iterate them correctly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 701
---

# Python TypeError — 'generator' object is not iterable

A `TypeError` with the message `'generator' object is not iterable` is raised when you try to iterate over a generator that has already been exhausted, or when you use a generator in a context that requires an `__iter__` method but the generator protocol doesn't provide one in the expected way. Generators implement the iterator protocol (`__next__`), not the full iterable protocol (`__iter__` that returns a new iterator).

## Common Causes

```python
# Cause 1: Iterating a generator twice
def my_gen():
    yield 1
    yield 2
    yield 3

gen = my_gen()
list(gen)  # [1, 2, 3] — generator is now exhausted
list(gen)  # TypeError: 'generator' object is not iterable

# Cause 2: Using generator in a for loop twice
gen = my_gen()
for x in gen:
    print(x)  # works fine

for x in gen:
    print(x)  # TypeError: 'generator' object is not iterable

# Cause 3: Passing generator to a function that iterates multiple times
gen = my_gen()
sorted(gen)  # First call works
sorted(gen)  # TypeError: 'generator' object is not iterable

# Cause 4: Using list() on an already-exhausted generator
gen = (x for x in range(5))
for _ in gen:
    pass
result = list(gen)  # TypeError: 'generator' object is not iterable

# Cause 5: Trying to len() or index a generator
gen = my_gen()
len(gen)  # TypeError: object of type 'generator' has no len()
gen[0]    # TypeError: 'generator' object is not subscriptable
```

## How to Fix

### Fix 1: Store the generator results in a list

```python
def my_gen():
    yield 1
    yield 2
    yield 3

gen = my_gen()
results = list(gen)  # Consume once, store results
print(results)        # [1, 2, 3]
print(results)        # [1, 2, 3] — safe to reuse

# Or iterate the stored list
for x in results:
    print(x)
```

### Fix 2: Recreate the generator when needed

```python
def my_gen():
    yield 1
    yield 2
    yield 3

# Wrong — exhausted generator
gen = my_gen()
list(gen)  # [1, 2, 3]
list(gen)  # TypeError

# Correct — recreate each time
list(my_gen())  # [1, 2, 3]
list(my_gen())  # [1, 2, 3]
```

### Fix 3: Use itertools.tee for multiple iterations

```python
import itertools

def my_gen():
    yield 1
    yield 2
    yield 3

gen = my_gen()
gen1, gen2, gen3 = itertools.tee(gen, 3)

print(list(gen1))  # [1, 2, 3]
print(list(gen2))  # [1, 2, 3]
print(list(gen3))  # [1, 2, 3]
```

### Fix 4: Use send() for generator communication

```python
def my_gen():
    value = yield 1
    value = yield 2
    yield 3

gen = my_gen()
print(next(gen))       # 1 — use __next__() / next() to advance
print(gen.send(None))  # 2 — send() also advances the generator
print(next(gen))       # 3

# Don't use for-loop iteration on a generator you're sending to
gen = my_gen()
gen.send(10)  # TypeError if generator hasn't started
next(gen)     # Must prime the generator first
gen.send(10)  # Now this works
```

## Examples

```python
# Real-world: Processing a database cursor (which is a generator)
import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.execute("SELECT * FROM users")

# Wrong — cursor can only be iterated once
users_first = list(cursor)
users_second = list(cursor)  # TypeError: 'generator' object is not iterable

# Correct — fetch all results first
users = cursor.fetchall()
users_first = users
users_second = users  # Safe to reuse

# Real-world: Using generator with zip
def fetch_ids():
    yield 1
    yield 2
    yield 3

def fetch_names():
    yield "Alice"
    yield "Bob"
    yield "Charlie"

# Wrong — zip exhausts the generators
pairs = list(zip(fetch_ids(), fetch_names()))
print(pairs)  # [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]

# Correct — zip is lazy and consumes both generators
gen_ids = fetch_ids()
gen_names = fetch_names()
pairs = list(zip(gen_ids, gen_names))
print(pairs)  # Works fine

# Real-world: Using itertools.islice for partial consumption
import itertools

def infinite_gen():
    n = 0
    while True:
        yield n
        n += 1

gen = infinite_gen()
first_five = list(itertools.islice(gen, 5))  # [0, 1, 2, 3, 4]
next_five = list(itertools.islice(gen, 5))   # [5, 6, 7, 8, 9]
```

## Related Errors

- [StopIteration](stopiteration) — generator exhausted during next().
- [GeneratorExit](generatorexit) — generator closed prematurely.
- [Generator close](generator-close) — generator closed by close().
- [Object not iterable](object-not-iterable) — non-iterable object used in for loop.
