---
title: "[Solution] Out of memory: failed malloc in assembly"
description: "Fix assembly out of memory errors when malloc fails to allocate requested memory."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["memory", "malloc", "allocation", "heap", "brk", "assembly"]
weight: 5
---

## What This Error Means

Out of memory in assembly occurs when malloc (or mmap/brk system calls) fails to allocate memory, typically returning NULL. This happens when the system is low on memory or the allocation size is too large.

## Common Causes

- Requesting too much memory
- System memory exhausted
- Memory leaks accumulating
- Large arrays without checking available memory
- Multiple allocations not freed

## How to Fix

```asm
; WRONG: Not checking malloc return
section .text
    mov rdi, 1048576     ; 1MB
    call malloc
    mov qword [rax], 0   ; Crash if malloc returned NULL

; CORRECT: Check malloc return value
    mov rdi, 1048576
    call malloc
    test rax, rax
    jz .malloc_failed
    mov qword [rax], 0
    jmp .done
.malloc_failed:
    ; Handle allocation failure
    mov rdi, error_msg
    call puts
.done:
```

```asm
; WRONG: Allocating huge amount
section .text
    mov rdi, 0x7FFFFFFFFFFFFFFF  ; Too large
    call malloc
    ; Likely returns NULL

; CORRECT: Reasonable allocation with check
    mov rdi, 1048576     ; 1MB - reasonable
    call malloc
    test rax, rax
    jz .handle_error
```

```asm
; CORRECT: Realloc with fallback
section .text
    ; Try to realloc to larger size
    mov rdi, [rel buffer]
    mov rsi, 2097152     ; 2MB new size
    call realloc
    test rax, rax
    jz .realloc_failed
    
    mov [rel buffer], rax
    jmp .done
    
.realloc_failed:
    ; Keep using old buffer
    mov rax, [rel buffer]
.done:
```

```asm
; CORRECT: Memory pool pattern
section .bss
    pool resb 1048576    ; Pre-allocate 1MB pool
    pool_ptr resq 1

section .text
    ; Bump allocator - no malloc needed
    global pool_alloc
pool_alloc:
    mov rax, [rel pool_ptr]
    add rax, rdi
    cmp rax, pool + 1048576
    ja .pool_exhausted
    
    mov [rel pool_ptr], rax
    sub rax, rdi
    ret
    
.pool_exhausted:
    xor rax, rax
    ret
```

## Related Errors

- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [Stack Overflow](asm-stack-overflow-v2) - stack issues
- [Out of Memory](/languages/fortran/fortran-allocate-error-v2) - allocation errors
