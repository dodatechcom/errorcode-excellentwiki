---
title: "[Solution] Go cannot assign to value — Type Error Fix"
description: "Fix Go cannot assign to value error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# cannot assign to value

The error `cannot assign to value` occurs when you try to modify a non-addressable value.

## Common Causes

- **Modifying range variable** — changes don't affect original
- **Assigning to map value** — `m[key].Field = x` is not allowed

## How to Fix

### Fix 1: Use index to modify slice elements

```go
for i := range s {
    s[i] = s[i] * 2
}
```

### Fix 2: Store map value in temp variable

```go
v := m[key]
v.Field = newValue
m[key] = v
```

## Related Errors

- [cannot-take-address]({{< relref "/languages/go/cannot-take-address" >}}) — cannot take address.
- [cannot-use-type]({{< relref "/languages/go/cannot-use-type" >}}) — type mismatch.
