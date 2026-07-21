---
title: "Groovy Range Index Out Of Bounds Error"
description: "Fix Groovy range index out of bounds errors when accessing list elements via range notation beyond valid indices."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Groovy range expressions like `list[0..5]` or `list[0..<5]` raise `IndexOutOfBoundsException` when the range extends beyond the collection's actual size.

## Common Causes

- Range end index exceeds list size
- Using `..` (inclusive) when `..<` (exclusive) was intended
- Negative indices without proper bounds checking
- Range on empty list always fails
- Miscalculated dynamic range boundaries

## How to Fix

```groovy
// WRONG: Range beyond list size
def list = [1, 2, 3]
def subset = list[0..5]  // IndexOutOfBoundsException

// CORRECT: Clamp range to list size
def list = [1, 2, 3]
def subset = list[0..<Math.min(5, list.size())]
```

```groovy
// WRONG: Negative index without bounds
def list = [1, 2, 3]
def last = list[-1]     // 3, works
def far = list[-5]      // IndexOutOfBoundsException

// CORRECT: Safe negative access
def list = [1, 2, 3]
def far = list.size() >= 5 ? list[-5] : null
```

## Examples

```groovy
// Example 1: Basic range operations
def list = [0, 1, 2, 3, 4]
println list[1..3]      // [1, 2, 3]
println list[0..<3]     // [0, 1, 2]
println list[-2..-1]    // [3, 4]

// Example 2: Dynamic range
def data = (1..100).toList()
def page = 2
def pageSize = 20
def start = (page - 1) * pageSize
def end = Math.min(start + pageSize, data.size()) - 1
println data[start..end]

// Example 3: Safe slice method
def safeSlice(list, from, to) {
    list[Math.max(0, from)..Math.min(to, list.size() - 1)]
}
```

## Related Errors

- [Index out of bounds error](groovy-index-out-of-bounds) -- element access issues
- [String index error](groovy-stringindex) -- string range problems
