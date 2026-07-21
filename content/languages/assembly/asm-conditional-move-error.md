---
title: "[Solution] Assembly Conditional Move Error -- Incorrect CMOV Usage"
description: "Fix assembly conditional move errors when using CMOV instructions incorrectly."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly Conditional Move Error

This error occurs when conditional move (CMOV) instructions are used with incorrect conditions or operands.

## Common Causes

- Using wrong condition code for the intended logic
- CMOV source is memory and destination is register (correct) but size mismatch
- Not setting flags before CMOVcc
- Using CMOV where branch would be more efficient

## How to Fix

### Set flags before CMOV

```asm
; WRONG: no flags set
cmovne rax, rbx  ; flags not set by previous instruction

; CORRECT: set flags first
test rdi, rdi
cmovz rax, rbx   ; move if zero (ZF=1)
```

### Use correct condition codes

```asm
; Signed conditions
cmovl  rax, rbx  ; move if less (SF!=OF)
cmovg  rax, rbx  ; move if greater
cmovle rax, rbx  ; move if less or equal
cmovge rax, rbx  ; move if greater or equal

; Unsigned conditions
cmovb  rax, rbx  ; move if below (CF=1)
cmova  rax, rbx  ; move if above
```

## Examples

```asm
; abs(x): return x if positive, -x if negative
abs_value:
    mov rax, rdi
    mov rbx, rdi
    neg rbx
    test rdi, rdi
    cmovns rax, rbx  ; use negated if negative
    ret
```
