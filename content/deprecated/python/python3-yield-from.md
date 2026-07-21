---
title: "[Solution] Deprecated Function Migration: manual iteration to yield from"
description: "Migrate from deprecated manual iteration patterns to yield from."
deprecated_function: "for x in iterable: yield x"
replacement_function: "yield from iterable"
languages: ["python"]
deprecated_since: "Python 3.3+"
---

# [Solution] Deprecated Function Migration: manual iteration to yield from

The `for x in iterable: yield x` has been deprecated in favor of `yield from iterable`.

## Migration Guide

yield from is more efficient and concise

yield from replaces manual iteration with simple delegation.

## Before (Deprecated)

```python
def chain(*iterables):
    for it in iterables:
        for item in it:
            yield item
```

## After (Modern)

```python
def chain(*iterables):
    for it in iterables:
        yield from it
```

## Key Differences

- yield from delegates to sub-iterator
- More efficient than manual for loop
- Clean delegation pattern
- Works with any iterable
