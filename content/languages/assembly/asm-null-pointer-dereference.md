---
title: "[Solution] Assembly NULL Pointer Dereference -- Segfault on NULL"
description: "Fix assembly NULL pointer dereference errors when accessing memory at address 0."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly NULL Pointer Dereference Error

This error occurs when attempting to read or write to memory address 0 (NULL), causing a segmentation fault.

## Common Causes

- Using uninitialized pointer register
- Dereferencing a pointer returned as NULL from a function
- Incorrect offset calculation pointing to address 0
- Missing NULL check before pointer access

## How to Fix

### Check pointer before dereference

```asm
; WRONG: no NULL check
mov rax, [rdi]  ; rdi may be NULL, causes segfault

; CORRECT: check for NULL
test rdi, rdi
jz .handle_null
mov rax, [rdi]

.handle_null:
    mov rax, -1  ; return error
    ret
```

### Initialize pointers properly

```asm
section .data
    safe_ptr dq 0  ; initialize to known value

section .text
use_pointer:
    mov rax, [safe_ptr]
    test rax, rax
    jz .skip
    ; use pointer safely
.skip:
    ret
```

## Examples

```asm
; Safe pointer dereference function
safe_deref:
    test rdi, rdi
    jz .null_ptr
    mov rax, [rdi]
    ret
.null_ptr:
    xor eax, eax
    ret
```
