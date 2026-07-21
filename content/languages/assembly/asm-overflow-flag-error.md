---
title: "[Solution] Assembly Overflow Flag Error -- Integer Overflow Detection"
description: "Fix assembly overflow flag errors when using JO/JNO incorrectly after arithmetic."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Overflow Flag Error

This error occurs when overflow conditions are not properly detected or handled after arithmetic operations.

## Common Causes

- Not checking overflow after ADD/SUB/MUL
- Using JO when overflow flag is not set by the preceding instruction
- Signed vs unsigned overflow confusion
- IMUL overflow not being checked

## How to Fix

### Check overflow after arithmetic

```asm
; WRONG: no overflow check
add eax, ebx
; may have overflowed

; CORRECT: check overflow
add eax, ebx
jo .overflow_handler

; Or use INTO for automatic trap
add eax, ebx
into  ; triggers exception if OF=1
```

### Check after IMUL

```asm
; TWO-operand IMUL sets OF and CF on overflow
imul eax, ebx
jo .overflow

; ONE-operand IMUL stores result in EDX:EAX
imul ecx  ; EAX * ECX -> EDX:EAX
; Check if EDX is sign extension of EAX
cdq
cmp edx, 0
je .no_overflow
cmp edx, -1
je .no_overflow
; overflow occurred
```

## Examples

```asm
safe_add:
    add rdi, rsi
    jc .overflow
    mov rax, rdi
    ret
.overflow:
    mov rax, -1
    ret
```
