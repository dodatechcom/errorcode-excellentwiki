---
title: "[Solution] C Infinite loop detected"
description: "Fix C infinite loop. Prevent unbounded loops with proper termination conditions."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["infinite-loop", "loop", "termination", "hang", "timeout"]
weight: 5
---

# Infinite loop detected

An infinite loop occurs when a loop's termination condition is never met, causing the program to run indefinitely. This can hang the program or consume 100% CPU.

## Common Causes

```c
// Cause 1: Missing increment
int i = 0;
while (i < 10) {
    printf("%d\n", i);
    // forgot i++
}

// Cause 2: Wrong condition
int i = 0;
while (i >= 0) { // unsigned overflow
    i++;
}

// Cause 3: Break condition unreachable
while (1) {
    if (impossible_condition) {
        break;
    }
}
```

## How to Fix

### Fix 1: Ensure loop variable changes

```c
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}
```

### Fix 2: Use proper termination condition

```c
int i = 0;
while (i < 10) {
    printf("%d\n", i);
    i++;
}
```

### Fix 3: Add timeout mechanism

```c
#include <time.h>

time_t start = time(NULL);
while (1) {
    if (time(NULL) - start > 5) {
        fprintf(stderr, "Timeout\n");
        break;
    }
    // ... work ...
}
```

## Examples

```c
#include <stdio.h>

int main(void) {
    int count = 0;
    while (count < 100) {
        printf("Iteration %d\n", count);
        count++;
    }
    printf("Done\n");
    return 0;
}
```

## Related Errors

- [Stack overflow from recursion]({{< relref "/languages/c/stack-overflow-recursive" >}}) — recursive infinite call.
- [Deadlock]({{< relref "/languages/c/dead-lock-thread" >}}) — threads stuck waiting.
- [CPU 100%]({{< relref "/languages/c/infinite-loop" >}}) — resource exhaustion.
