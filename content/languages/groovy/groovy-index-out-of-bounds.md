---
title: "[Solution] Groovy Index Out of Bounds Error"
description: "Fix Groovy StringIndexOutOfBoundsException and ArrayIndexOutOfBoundsException. Handle bounds checking properly."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `IndexOutOfBoundsException` occurs when accessing an element at an index that is outside the valid range of a string, array, or collection. This includes string character access, list element access, and array indexing.

## Why It Happens

- Index is negative or exceeds collection size: The index is outside the valid range.
- Off-by-one error in loop boundaries: Loop iterates one too many times.
- String character access with invalid index: The index exceeds the string length.
- Removing elements while iterating: Modifying the collection during iteration changes indices.
- Hardcoded index values after data changes: The data structure changed but indices were not updated.

## How to Fix It

Check bounds before accessing elements:

```groovy
def list = [1, 2, 3, 4, 5]
def index = 10

// WRONG: No bounds check
def value = list[index]

// CORRECT: Check bounds first
if (index >= 0 && index < list.size()) {
    def value = list[index]
} else {
    println "Index $index out of range 0..${list.size() - 1}"
}
```

Use safe access for strings:

```groovy
def str = "Hello"
def idx = 10

// CORRECT: Safe string access
if (idx < str.length()) {
    char c = str.charAt(idx)
}

// Or use getAt with bounds check
def c = idx < str.length() ? str[idx] : null
```

Use range-based iteration:

```groovy
def items = ['a', 'b', 'c']
0.upto(items.size() - 1) { i ->
    println items[i]
}

// Or use eachWithIndex
items.eachWithIndex { item, i ->
    println "$i: $item"
}
```

Handle null collections safely:

```groovy
def result = myList?.getAt(0) ?: defaultValue
```

Use collect instead of indexed access:

```groovy
// WRONG: Manual indexing
def results = []
for (int i = 0; i < list.size(); i++) {
    results.add(transform(list[i]))
}

// CORRECT: Functional approach
def results = list.collect { transform(it) }
```

## Common Mistakes

- Not checking collection size before index access.
- Using wrong boundary condition in loops. Remember that indices are 0-based.
- Accessing string by index without length check.
- Modifying collection size during indexed iteration. Use iterators or collect instead.
- Assuming `.getAt()` throws a specific exception. It may return null for out-of-bounds indices on certain types.

## Related Pages

- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer error
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-io-error]({{< relref "/languages/groovy/groovy-io-error" >}}) - I/O exception
- [groovy-classcast-error-v2]({{< relref "/languages/groovy/groovy-casterror-v2" >}}) - class cast error
