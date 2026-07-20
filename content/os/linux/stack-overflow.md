---
title: "[Solution] Linux: stack-overflow — stack overflow error"
description: "Fix Linux stack-overflow errors. stack overflow error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---
# Linux: Stack Overflow

A stack overflow occurs when a program's call stack exceeds its allocated size, causing a crash.

## Common Causes

- Infinite recursion without a base case
- Very deep function call chains (e.g., deep directory traversal)
- Large stack-allocated variables (arrays, structs) on the stack
- Thread created with insufficient stack size
- Signal handling causing recursive signal delivery

## How to Fix

### 1. Check Stack Size Limit

```bash
ulimit -s
# Default is usually 8192 (8MB)
```

### 2. Increase Stack Size

```bash
# Increase to 16MB
ulimit -s 16384

# For a specific program
ulimit -s 65536 && ./myprogram

# Change system-wide limit
echo "* soft stack 65536" | sudo tee -a /etc/security/limits.conf
```

### 3. Debug with GDB

```bash
gdb ./myprogram
(gdb) run
(gdb) bt  # Shows the call stack
(gdb) info frame
```

### 4. Fix the Code

```bash
# Change large stack arrays to heap allocation
# char buffer[1024*1024];  ->  char *buffer = malloc(1024*1024);
```

## Examples

```bash
$ ./deep_recursion
Segmentation fault (core dumped)

$ ulimit -s
8192

$ ulimit -s 65536
$ ./deep_recursion
# Now works

$ gdb ./deep_recursion core
(gdb) bt
#0  0x00007ffff7a3a1a7 in __GI_raise () from /lib/libc.so.6
#1  0x00007ffff7a3b8b8 in __GI_abort () from /lib/libc.so.6
#2  0x00007ffff7a83228 in __GI____stack_chk_fail () from /lib/libc.so.6
```
