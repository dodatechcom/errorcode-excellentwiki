---
title: "[Solution] Linux EFAULT (errno 14) — Bad Address Fix"
description: "Fix Linux EFAULT (errno 14) Bad address error. Solutions for invalid pointer and memory access issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EFAULT (errno 14) — Bad Address

EFAULT (errno 14) means the system detected an invalid memory address in a system call argument. This error occurs when a pointer references memory outside the process's address space, such as a NULL pointer, an uninitialized pointer, or a pointer to freed memory. It is distinct from EACCES (errno 13) because EFAULT indicates a memory access violation, not a permission issue.

## Common Causes

- Passing a NULL or uninitialized pointer to a system call
- Attempting to access memory that has been freed or unmapped
- Buffer overflow causing pointer corruption
- Accessing memory beyond the stack or heap boundaries

## How to Fix EFAULT

### 1. Validate Pointers Before Use

Always check that pointers are valid before passing them to system calls:

```c
if (ptr == NULL) {
    fprintf(stderr, "Error: NULL pointer\n");
    return -1;
}
```

### 2. Use Valgrind to Detect Memory Errors

Run your program under Valgrind to identify memory issues:

```bash
valgrind --tool=memcheck ./program
```

### 3. Compile with AddressSanitizer

Enable AddressSanitizer for runtime memory error detection:

```bash
gcc -fsanitize=address -g -o program source.c
./program
```

### 4. Check for Use-After-Free

Ensure pointers are not used after the memory they reference has been freed:

```c
free(ptr);
ptr = NULL;  // Set to NULL after freeing
```

## Verification

After fixing memory issues, run Valgrind again to confirm no errors remain:

```bash
valgrind --leak-check=full ./program
```

## Related Error Codes

- [ENOMEM (errno 12)](/os/linux/errno-12/) — Out of memory
- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
- [EEXIST (errno 17)](/os/linux/errno-17/) — File exists
