---
title: "[Solution] SIGSEGV: page fault in assembly"
description: "Fix assembly page fault errors when accessing unmapped or protected memory pages."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A page fault (SIGSEGV) occurs when assembly code attempts to access a memory page that is not mapped in the process's address space, or attempts a disallowed access (writing to read-only page).

## Common Causes

- Accessing freed memory
- Writing to read-only data section
- Jumping to unmapped memory
- Stack overflow into guard page
- Using mmap'd memory after munmap

## How to Fix

```asm
; WRONG: Accessing freed memory
section .text
    call malloc
    mov [rax], 42
    call free         ; Memory now freed
    mov rbx, [rax]    ; SIGSEGV: accessing freed memory

; CORRECT: Don't use memory after free
section .text
    call malloc
    mov [rax], 42
    mov rbx, [rax]    ; Access while still allocated
    call free         ; Free after use
    ; Don't access rax after this
```

```asm
; WRONG: Writing to read-only section
section .rodata
    message db "Hello", 0

section .text
    mov byte [rel message], 'h'  ; SIGSEGV: .rodata is read-only

; CORRECT: Use writable section for modifiable data
section .data
    message db "Hello", 0

section .text
    mov byte [rel message], 'h'  ; Safe: .data is writable
```

```asm
; CORRECT: Proper mmap usage
section .text
    ; mmap memory
    mov rdi, 0
    mov rsi, 4096
    mov rdx, 3        ; PROT_READ | PROT_WRITE
    mov r10, 0x22     ; MAP_PRIVATE | MAP_ANONYMOUS
    mov r8, -1
    mov r9, 0
    mov rax, 9        ; SYS_mmap
    syscall
    
    test rax, -1
    jz .mmap_failed
    
    ; Use memory
    mov [rax], 42
    
    ; Unmap when done
    mov rdi, rax
    mov rsi, 4096
    mov rax, 11       ; SYS_munmap
    syscall
```

```asm
; CORRECT: Check pointer validity
section .text
    ; Validate pointer before dereference
    test rax, rax
    jz .null_pointer
    cmp rax, 0x7FFFFFFFFFFFFFFF  ; Above valid range
    ja .invalid_pointer
    mov rbx, [rax]
    jmp .done
.null_pointer:
.invalid_pointer:
    ; Handle error
.done:
```

## Related Errors

- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [Stack Overflow](asm-stack-overflow-v2) - stack issues
- [Out of Memory](asm-out-of-memory-v2) - allocation failures
