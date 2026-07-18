---
title: "[Solution] C AddressSanitizer Error — How to Fix"
description: "Fix ASan errors including buffer overflows, use-after-free, and double frees."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C AddressSanitizer Error — How to Fix

AddressSanitizer detects memory errors at runtime with detailed stack traces.

## Common Error Messages

- `heap-buffer-overflow`
- `use-after-free`
- `stack-buffer-overflow`
- `double-free`

## How to Fix It

### Enable ASan

```bash
gcc -fsanitize=address -g -o p p.c
./p
```

### Fix heap overflow

```c
char *buf = malloc(10);
memset(buf, 0, 10);  // correct size
```

### Fix use-after-free

```c
int *p = malloc(sizeof(int));
free(p);
p = NULL;
```

### Leak detection

```bash
ASAN_OPTIONS=detect_leaks=1 ./p
```

## Common Scenarios

### Scenario 1: Heap buffer overflow from wrong allocation

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Use-after-free from freed memory access

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Double free from calling free twice

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Compile with -fsanitize=address -g
- **Tip 2:** Fix all ASan errors before shipping
- **Tip 3:** Enable detect_leaks=1
