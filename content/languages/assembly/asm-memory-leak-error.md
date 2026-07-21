---
title: "[Solution] Assembly Memory Leak Error -- Unfreed Allocations"
description: "Fix assembly memory leak errors when heap allocations are not properly freed."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Memory Leak Error

This error occurs when memory allocated via mmap/brk or malloc is not freed, causing the program to consume increasing memory.

## Common Causes

- Forgetting to call free/munmap after use
- Early return skipping cleanup code
- Mismatched malloc/free pairs
- Not handling error paths with cleanup

## How to Fix

### Always free allocated memory

```asm
; WRONG: memory leaked
malloc_and_use:
    call malloc
    ; use memory...
    ret  ; forgot to free!

; CORRECT: free before return
malloc_and_use:
    push rbx
    call malloc
    mov rbx, rax      ; save pointer
    ; use memory...
    mov rdi, rbx
    call free
    pop rbx
    ret
```

### Use RAII-style patterns

```asm
; Allocate and free in same scope
    call mmap
    mov [ptr], rax
    ; ... use memory ...
    mov rdi, [ptr]
    mov rsi, [size]
    call munmap
```

## Examples

```asm
safe_malloc:
    push rbx
    call malloc
    test rax, rax
    jz .error
    mov rbx, rax
    ; ... use memory ...
    mov rdi, rbx
    call free
    xor eax, eax
    pop rbx
    ret
.error:
    pop rbx
    ret
```
