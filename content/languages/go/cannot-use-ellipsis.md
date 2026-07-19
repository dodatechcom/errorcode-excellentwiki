---
title: "[Solution] Go cannot use ... with non-slice — Compile Error Fix"
description: "Fix Go cannot use ... with non-slice error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# cannot use ... with non-slice

The error `cannot use ... with non-slice argument` occurs when you use the `...` spread operator on a non-slice value.

## How to Fix

### Fix 1: Convert array to slice

```go
var arr [3]int = [3]int{1, 2, 3}
slice := arr[:]
sum(slice...)
```

## Examples

```go
package main

func sum(nums ...int) int {
    total := 0
    for _, n := range nums { total += n }
    return total
}

func main() {
    arr := [3]int{1, 2, 3}
    _ = sum(arr...)
}
```

Output:
```
invalid use of ... in call to sum
```

## Related Errors

- [too-many-arguments]({{< relref "/languages/go/too-many-arguments" >}}) — wrong argument count.
- [cannot-use-type]({{< relref "/languages/go/cannot-use-type" >}}) — type mismatch.
