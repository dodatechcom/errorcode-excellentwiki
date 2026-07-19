---
title: "[Solution] Go invalid operation: cannot slice — Compile Error Fix"
description: "Fix Go cannot slice error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# invalid operation: cannot slice

The error `invalid operation: cannot slice X` occurs when using slice syntax on a non-sliceable type.

## Common Causes

- **Slicing a map** — maps don't support slicing
- **Slicing an integer** — wrong type

## How to Fix

### Fix 1: Convert to slice first

```go
m := map[string]int{"a": 1}
keys := make([]string, 0, len(m))
for k := range m {
    keys = append(keys, k)
}
sub := keys[:2]
```

## Examples

```go
package main

func main() {
    m := map[string]int{"a": 1}
    _ = m[:1]
}
```

Output:
```
invalid operation: cannot slice m (type map[string]int)
```

## Related Errors

- [slice-bounds]({{< relref "/languages/go/slice-bounds" >}}) — slice bounds.
- [invalid-selector]({{< relref "/languages/go/invalid-selector" >}}) — invalid selector.
