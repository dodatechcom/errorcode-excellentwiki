---
title: "[Solution] Go assignment to entry in map — Runtime Error Fix"
description: "Fix Go map assignment errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# assignment to entry in map

The error `panic: assignment to entry in map` can occur when writing to a nil map.

## How to Fix

### Fix 1: Initialize maps with make

```go
m := make(map[string]int)
m["key"] = 1
```

## Examples

```go
package main

func main() {
    var m map[string]int
    m["key"] = 1
}
```

Output:
```
panic: assignment to entry in nil map
```

## Related Errors

- [concurrent-map]({{< relref "/languages/go/concurrent-map" >}}) — concurrent map access.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — nil pointer dereference.
