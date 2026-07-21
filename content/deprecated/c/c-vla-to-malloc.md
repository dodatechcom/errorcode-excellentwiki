---
title: "[Solution] Deprecated Function Migration: VLAs to dynamic allocation"
description: "Migrate from deprecated VLAs to malloc/calloc."
deprecated_function: "int arr[n]"
replacement_function: "malloc(n * sizeof(int))"
languages: ["c"]
deprecated_since: "C11 optional"
---

# [Solution] Deprecated Function Migration: VLAs to dynamic allocation

The `int arr[n]` has been deprecated in favor of `malloc(n * sizeof(int))`.

## Migration Guide

VLAs are optional in C11

VLAs allocate on stack (may overflow).

## Before (Deprecated)

```c
int n = get_size();
int arr[n];
```

## After (Modern)

```c
int n = get_size();
int *arr = malloc(n * sizeof(int));
if (arr == NULL) { return -1; }
// ...
free(arr);
```

## Key Differences

- VLAs allocate on stack
- malloc allocates on heap
- Always check malloc return
