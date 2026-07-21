---
title: "[Solution] Assembly Division Error -- Division by Zero and Overflow"
description: "Fix assembly division errors when DIV or IDIV encounters zero divisor or overflow."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Division Error

This error occurs when DIV or IDIV instructions divide by zero or when the quotient overflows the destination register.

## Common Causes

- Divisor register/memory contains zero
- Quotient too large for destination (e.g., EDX:EAX / small number)
- Uninitialized divisor variable
- Signed division overflow (-2^31 / -1)

## How to Fix

### Check divisor before division

```asm
; WRONG: no zero check
mov eax, [dividend]
cdq
idiv ecx  ; ECX may be zero

; CORRECT: check divisor
mov eax, [dividend]
mov ecx, [divisor]
test ecx, ecx
jz .div_by_zero
cdq
idiv ecx
jmp .done

.div_by_zero:
    mov eax, -1  ; error code
.done:
    ret
```

### Use shift for power-of-2 division

```asm
; Faster than DIV for power-of-2
mov eax, [value]
sar eax, 3  ; divide by 8 (2^3)
```

## Examples

```asm
; Safe division function
; Input: EAX = dividend, ECX = divisor
; Output: EAX = quotient, EDX = remainder, CF set on error
safe_div:
    test ecx, ecx
    jz .error
    cdq
    idiv ecx
    clc
    ret
.error:
    stc
    ret
```
