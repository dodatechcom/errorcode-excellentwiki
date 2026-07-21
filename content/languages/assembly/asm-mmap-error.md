---
title: "[Solution] Assembly MMAP Error -- Memory Mapping Issues"
description: "Fix assembly mmap errors when using the mmap syscall incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly MMAP Error

This error occurs when the mmap syscall is used with incorrect parameters or without proper error handling.

## Common Causes

- Wrong syscall number (9 for mmap on x86-64 Linux)
- Incorrect protection flags (PROT_READ, PROT_WRITE, PROT_EXEC)
- MAP_ANONYMOUS not set for anonymous mappings
- Not checking MAP_FAILED return value

## How to Fix

### Use correct mmap parameters

```asm
; mmap(addr, len, prot, flags, fd, offset)
; RDI = addr (NULL for kernel choice)
; RSI = length
; RDX = PROT_READ|PROT_WRITE
; R10 = MAP_ANONYMOUS|MAP_PRIVATE
; R8 = fd (-1 for anonymous)
; R9 = offset (0)

mmap_anon:
    mov rax, 9          ; sys_mmap
    xor edi, edi        ; addr = NULL
    mov rsi, rdx        ; length in RSI
    mov rdx, 3          ; PROT_READ|PROT_WRITE
    mov r10, 0x22       ; MAP_PRIVATE|MAP_ANONYMOUS
    mov r8, -1          ; fd = -1
    xor r9, r9          ; offset = 0
    syscall
    cmp rax, -4096
    ja .error           ; check for mmap error
    ret
```

## Examples

```asm
; Allocate 4096 bytes
alloc_page:
    push rbx
    mov rax, 9
    xor edi, edi
    mov esi, 4096
    mov edx, 3          ; PROT_READ|PROT_WRITE
    mov r10, 0x22       ; MAP_PRIVATE|MAP_ANONYMOUS
    mov r8, -1
    xor r9, r9
    syscall
    pop rbx
    cmp rax, -4096
    ja .error
    ret
```
