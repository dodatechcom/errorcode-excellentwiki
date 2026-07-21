---
title: "[Solution] Assembly Float Error -- FPU Stack Overflow"
description: "Fix assembly FPU errors when the x87 FPU stack overflows or underflows."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Float Error

This error occurs when the x87 FPU register stack overflows (more than 8 values) or underflows.

## Common Causes

- Pushing more than 8 values onto FPU stack without popping
- Forgetting to free FPU registers after use
- Incorrect FPU instruction sequence
- FPU exceptions not being handled

## How to Fix

### Manage FPU stack properly

```asm
; WRONG: FPU stack overflow
fld qword [val1]  ; ST(0) = val1
fld qword [val2]  ; ST(0) = val2, ST(1) = val1
fld qword [val3]  ; continues pushing...

; CORRECT: pop after use
fld qword [val1]
fld qword [val2]
faddp st1, st0    ; ST(0) = val1 + val2, stack freed
```

### Check FPU stack with FXAM

```asm
fxam               ; examine top of stack
fnstsw ax          ; store status
sahf               ; transfer to CPU flags
jc .is_nan         ; check for NaN
```

## Examples

```asm
; Safe FPU operation
compute_average:
    fld qword [sum]
    fild dword [count]
    fdivp st1, st0    ; divide and pop
    ret
```
