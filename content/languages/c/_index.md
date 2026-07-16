---
title: "[Solution] C Language Errors — Compiler, Runtime & errno Fixes"
description: "Find solutions for C language errors including segmentation faults, stack overflow, and ENOMEM. Copy-paste C code fixes."
languages: ["c"]
---

C gives you full control over the machine, which also means C errors can be subtle — from strict compiler diagnostics to silent undefined behavior that manifests as segmentation faults. This section covers runtime faults and the `errno` codes set by standard library functions.

## Error Codes

| Error | Description | Fix |
|-------|-------------|-----|
| [malloc() Returns NULL (ENOMEM)](/languages/c/errno-enomem/) | Memory allocation failure — `malloc` cannot allocate requested memory | Check the return value for `NULL`, reduce allocation size, and verify no memory leaks with Valgrind |
| [Segmentation Fault (SIGSEGV)](/languages/c/segmentation-fault/) | Memory access violation — writing to invalid or read-only memory | Use a debugger (`gdb`), enable AddressSanitizer, and check for null pointer dereferences |
| [Stack Overflow](/languages/c/stack-overflow/) | Recursion exceeds stack limit — infinite or too-deep recursive calls | Add a base case to stop recursion, convert to iteration, or increase stack size with `-Wl,--stack` |

## Quick Debug

```bash
# Compile with all warnings and debug info
gcc -Wall -Wextra -g -o myprogram myprogram.c

# Run under AddressSanitizer
gcc -fsanitize=address -g -o myprogram myprogram.c
./myprogram
```
