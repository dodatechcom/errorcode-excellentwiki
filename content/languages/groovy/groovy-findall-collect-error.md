---
title: "Groovy FindAll Collect Chain Error"
description: "Fix Groovy findAll and collect chain errors when chained collection operations produce unexpected null or empty results."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Chaining findAll and collect operations can produce unexpected results when the intermediate collection is empty, when collect returns null elements, or when the chain produces a different data structure than expected.

## Common Causes

- findAll returns empty list, causing collect to produce empty result
- collect returns null elements that break downstream operations
- Chaining produces nested lists instead of flat list
- Closure in collect throws exception, stopping iteration
- findAll predicate has side effects that change iteration state

## How to Fix

```groovy
// WRONG: collect returning null breaks sum
def result = [1, 2, 3, null, 5]
    .findAll { it != null }
    .collect { it > 3 ? it : null }
    .sum()  // null in list causes issues

// CORRECT: Filter nulls after collect
def result = [1, 2, 3, null, 5]
    .findAll { it != null }
    .collect { it > 3 ? it : null }
    .findAll { it != null }
    .sum()
```

```groovy
// WRONG: Nested list from collect
def result = ["a,b", "c,d"]
    .collect { it.split(",") }
// result is [["a","b"], ["c","d"]] not ["a","b","c","d"]

// CORRECT: Use flatten
def result = ["a,b", "c,d"]
    .collect { it.split(",") }
    .flatten()
```

## Examples

```groovy
// Example 1: Basic chain
def result = (1..20).toList()
    .findAll { it % 2 == 0 }
    .collect { it * it }
    .findAll { it > 50 }
println result  // [64, 100, 144, 196, 256, 324, 400]

// Example 2: String processing
def words = ["Hello", "World", "Groovy", "is", "fun"]
def result = words
    .findAll { it.length() > 3 }
    .collect { it.toLowerCase() }
    .sort()
println result  // [groovy, hello, world]

// Example 3: Grouping after filtering
def result = (1..100).toList()
    .findAll { it % 3 == 0 }
    .groupBy { it % 10 }
println result.size()  // number of groups
```

## Related Errors

- [List error](groovy-list-error) -- list operation issues
- [Map error](groovy-map-error) -- map operation problems
