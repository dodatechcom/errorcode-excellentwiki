---
title: "Out of memory in Assembly"
description: "Out of memory errors in Assembly occur when mmap, brk, or stack allocation requests exceed available system memory."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["memory", "mmap", "brk", "allocation", "oom"]
weight: 5
---

## What This Error Means

Assembly programs allocate memory through syscalls (mmap, brk/sbrk). When the system cannot fulfill the allocation request, the syscall returns an error code (ENOMEM) or the program receives SIGKILL from the OOM killer.

## Common Causes

- Requesting too much memory in a single mmap
- Memory leak (allocating without freeing)
- System out of physical + swap memory
- Virtual address space exhaustion (32-bit)

## How to Fix

```asm
; WRONG: Requesting excessive memory
mov rax, 9          ; sys_mmap
mov rdi, 0          ; addr = NULL
mov rsi, 0xFFFFFFFF ; 4GB - may fail
mov rdx, 3          ; PROT_READ|PROT_WRITE
mov r10, 0x22       ; MAP_PRIVATE|MAP_ANONYMOUS
mov r8, -1
mov r9, 0
syscall             ; May return ENOMEM

; CORRECT: Request reasonable amount
mov rax, 9
mov rdi, 0
mov rsi, 4096       ; One page at a time
mov rdx, 3
mov r10, 0x22
mov r8, -1
mov r9, 0
syscall
```

## Examples

```asm
; Check mmap return value
mov rax, 9
; ... setup mmap args ...
syscall
cmp rax, -4096      ; Check for error
ja .mmap_failed     ; If > -4096, it's an error code
```

## How to Debug

- Monitor memory with `top` or `htop`
- Check `/proc/meminfo` for available memory
- Use `valgrind` to detect memory leaks

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault) - invalid memory access
- [Segmentation Fault](/languages/assembly/segmentation-fault) - memory violations
