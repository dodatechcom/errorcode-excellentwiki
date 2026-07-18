---
title: "[Solution] C Valgrind Error — How to Fix"
description: "Fix Valgrind memory error reports including leaks, invalid reads/writes."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Valgrind Error — How to Fix

Valgrind detects memory errors at runtime with detailed stack traces.

## Common Error Messages

- `Invalid read of size N`
- `Invalid write of size N`
- `Use of uninitialised value`
- `definitely lost: X bytes`

## How to Fix It

### Full leak check

```bash
gcc -g -o p p.c
valgrind --leak-check=full --show-leak-kinds=all ./p
```

### Fix invalid read

```c
int *arr = malloc(10*sizeof(int));
if (idx >= 0 && idx < 10)
    printf("%d\n", arr[idx]);
```

### Fix uninit

```c
int x = 0;  // always initialize
```

### Suppressions

```bash
valgrind --suppressions=my.supp ./p
```

## Common Scenarios

### Scenario 1: Invalid read/write from out-of-bounds

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Uninitialized value causing wrong results

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Memory leak from forgotten free

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Run Valgrind during development
- **Tip 2:** Fix all Valgrind errors before deploy
- **Tip 3:** Use suppressions for known third-party issues
