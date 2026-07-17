---
title: "[Solution] C Stack overflow from infinite recursion"
description: "Fix C stack overflow from infinite recursion. Add base cases to prevent unbounded recursion."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Stack overflow from infinite recursion

A stack overflow from recursion occurs when a function calls itself without a proper base case, exhausting the stack space.

## Common Causes

```c
// Cause 1: Missing base case
void recurse(void) {
    recurse(); // infinite recursion
}

// Cause 2: Wrong base case
void countDown(int n) {
    printf("%d\n", n);
    countDown(n + 1); // goes wrong direction
}

// Cause 3: Mutual recursion without base
void a(void) { b(); }
void b(void) { a(); }
```

## How to Fix

### Fix 1: Add proper base case

```c
void recurse(int n) {
    if (n <= 0) return; // base case
    recurse(n - 1);
}
```

### Fix 2: Verify base case is reachable

```c
void countDown(int n) {
    if (n < 0) return;
    printf("%d\n", n);
    countDown(n - 1); // reaches 0
}
```

### Fix 3: Convert to iteration

```c
void printNumbers(int n) {
    for (int i = n; i >= 0; i--) {
        printf("%d\n", i);
    }
}
```

## Examples

```c
#include <stdio.h>

unsigned long fibonacci(unsigned int n) {
    if (n <= 1) return n; // base case
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main(void) {
    printf("fib(10) = %lu\n", fibonacci(10));
    return 0;
}
```

## Related Errors

- [Infinite loop]({{< relref "/languages/c/infinite-loop" >}}) — loop hang.
- [Deadlock]({{< relref "/languages/c/dead-lock-thread" >}}) — threads stuck.
- [Segmentation fault]({{< relref "/languages/c/segmentation-fault-null" >}}) — crash from stack overflow.
