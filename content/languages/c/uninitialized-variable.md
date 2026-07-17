---
title: "[Solution] C Use of uninitialized variable"
description: "Fix C use of uninitialized variable. Initialize all variables before use to prevent undefined behavior."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["uninitialized", "undefined-behavior", "variable", "garbage-value"]
weight: 5
---

# Use of uninitialized variable

Using an uninitialized variable leads to undefined behavior. The variable contains whatever garbage value happened to be at that memory location.

## Common Causes

```c
// Cause 1: Local variable not initialized
int x;
printf("%d\n", x); // undefined behavior

// Cause 2: Uninitialized pointer
int *ptr;
*ptr = 10; // crash

// Cause 3: Partial initialization
int arr[10];
arr[0] = 1;
printf("%d\n", arr[5]); // undefined behavior
```

## How to Fix

### Fix 1: Initialize at declaration

```c
int x = 0;
printf("%d\n", x); // safe
```

### Fix 2: Use calloc for arrays

```c
int *arr = calloc(10, sizeof(int)); // zero-initialized
printf("%d\n", arr[5]); // safe — 0
free(arr);
```

### Fix 3: Initialize all struct members

```c
struct Point {
    int x, y;
};
struct Point p = { 0, 0 }; // initialize all members
```

## Examples

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int count = 0; // initialize
    double values[100] = {0}; // zero-initialize array
    
    for (int i = 0; i < 100; i++) {
        values[i] = (double)i;
        count++;
    }
    
    printf("Count: %d\n", count);
    return 0;
}
```

## Related Errors

- [Segmentation fault]({{< relref "/languages/c/segmentation-fault-null" >}}) — crash from uninitialized pointer.
- [Integer overflow]({{< relref "/languages/c/integer-overflow" >}}) — arithmetic overflow.
- [Format string vulnerability]({{< relref "/languages/c/format-string-vulnerability" >}}) — format string issue.
