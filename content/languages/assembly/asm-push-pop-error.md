---
title: "[Solution] Assembly PUSH POP Error -- Stack Imbalance"
description: "Fix assembly push/pop errors when the stack becomes imbalanced during function execution."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly PUSH POP Error

This error occurs when PUSH and POP instructions are not balanced, causing the stack pointer to be incorrect.

## Common Causes

- Conditional code paths with different PUSH/POP counts
- Forgetting to POP before function return
- Using PUSH for temporary storage without corresponding POP
- Mixing 32-bit and 64-bit PUSH/POP

## How to Fix

### Balance stack in all code paths

```asm
; WRONG: only one path cleans stack
    push rbx
    test rdi, rdi
    jz .done
    ; ... code ...
    pop rbx
.done:
    ret  ; stack imbalanced if jumped

; CORRECT: ensure all paths clean stack
    push rbx
    test rdi, rdi
    jz .done
    ; ... code ...
.done:
    pop rbx
    ret
```

### Use SUB for large allocations

```asm
; Instead of many PUSHes
    sub rsp, 64  ; allocate 64 bytes at once
    ; ... body ...
    add rsp, 64
    ret
```

## Examples

```asm
my_func:
    push rbp
    mov rbp, rsp
    push rbx
    push r12
    ; ... body ...
    pop r12
    pop rbx
    pop rbp
    ret
```
