---
title: "[Solution] Go import cycle not allowed — Compile Error Fix"
description: "Fix Go import cycle not allowed error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# import cycle not allowed

The error `import cycle not allowed` occurs when package A imports package B, which imports package A.

## Common Causes

- **Two packages importing each other**
- **Transitive cycle** — A -> B -> C -> A

## How to Fix

### Fix 1: Extract shared types to a third package

```
package types  // no imports
package a      // imports types
package b      // imports types
```

### Fix 2: Use interfaces to break dependency

```go
type Store interface {
    Get(key string) (string, error)
}
```

## Examples

```go
// package a imports b
// package b imports a
```

Output:
```
import cycle not allowed
```

## Related Errors

- [package-not-found]({{< relref "/languages/go/package-not-found" >}}) — package not found.
- [module-not-found]({{< relref "/languages/go/module-not-found" >}}) — module not found.
