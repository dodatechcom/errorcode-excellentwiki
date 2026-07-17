---
title: "[Solution] Invalid syscall number in assembly"
description: "Fix assembly errors when making system calls with invalid or unsupported syscall numbers."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["syscall", "system-call", "kernel", "linux", "invalid", "assembly"]
weight: 5
---

## What This Error Means

Invalid syscall errors occur when assembly code invokes a system call with a number that the kernel doesn't recognize, or when syscall conventions are violated.

## Common Causes

- Wrong syscall number for architecture
- Incorrect register setup for arguments
- Syscall not available on current kernel
- Wrong ABI (32-bit vs 64-bit syscall)
- Kernel version doesn't support syscall

## How to Fix

```asm
; WRONG: Invalid syscall number
section .text
    mov rax, 9999    ; Invalid syscall number
    syscall           ; Kernel returns -ENOSYS

; CORRECT: Use valid syscall numbers
section .text
    ; Linux x86-64 syscalls
    ; 0 = read, 1 = write, 60 = exit
    mov rax, 1       ; sys_write
    mov rdi, 1       ; stdout
    lea rsi, [rel msg]
    mov rdx, 13      ; length
    syscall

section .data
    msg db "Hello, world", 10
```

```asm
; WRONG: Wrong argument registers
section .text
    mov rax, 60      ; sys_exit
    mov rbx, 0       ; Wrong register! Should be rdi

; CORRECT: Use correct argument registers
section .text
    mov rax, 60      ; sys_exit
    mov rdi, 0       ; exit code in rdi
    syscall
```

```asm
; CORRECT: Complete syscall example
section .text
    global _start
_start:
    ; write(1, "Hello\n", 6)
    mov rax, 1       ; __NR_write
    mov rdi, 1       ; fd = stdout
    lea rsi, [rel msg]
    mov rdx, 6       ; count
    syscall
    
    ; exit(0)
    mov rax, 60      ; __NR_exit
    xor rdi, rdi     ; status = 0
    syscall

section .data
    msg db "Hello", 10
```

```asm
; CORRECT: Check syscall availability
section .text
    ; Try syscall and handle ENOSYS
    mov rax, 302     ; sys_rseq (may not exist)
    syscall
    cmp rax, -ENOSYS ; Check for "function not implemented"
    jne .supported
    ; Syscall not available, use alternative
.supported:
```

## Related Errors

- [Invalid Instruction](asm-invalid-instruction-v2) - CPU errors
- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [Broken Pipe](asm-broken-pipe) - pipe errors
