---
title: "[Solution] Assembly Register Clobbering Error -- ABI Violation"
description: "Fix assembly register clobbering errors when functions modify caller-saved registers without saving."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Register Clobbering Error

This error occurs when assembly functions modify registers that the calling convention expects to be preserved.

## Common Causes

- Modifying callee-saved registers (RBX, RBP, R12-R15) without saving
- Not preserving RAX for return value in System V ABI
- Corrupting RSP before RET
- Caller-saved registers not saved before calling other functions

## How to Fix

### Save callee-saved registers

```asm
; WRONG: modifies RBX without saving
my_func:
    mov rbx, rdi  ; clobbers RBX
    ; ...
    ret

; CORRECT: save and restore
my_func:
    push rbx
    mov rbx, rdi
    ; ...
    pop rbx
    ret
```

### Preserve caller-saved registers across calls

```asm
; Calling external function, must save R12-R15
call_external:
    push r12
    push r13
    push r14
    push r15
    call other_function
    pop r15
    pop r14
    pop r13
    pop r12
    ret
```

## Examples

```asm
; System V ABI: must preserve RBX, RBP, R12-R15
process_data:
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
