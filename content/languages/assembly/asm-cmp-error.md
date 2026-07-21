---
title: "[Solution] Assembly CMP Error -- Incorrect Comparison Instructions"
description: "Fix assembly CMP errors when using CMP and conditional jumps incorrectly."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly CMP Error

This error occurs when comparisons are performed incorrectly or the wrong conditional jump is used after CMP.

## Common Causes

- Comparing values in wrong order
- Using signed jumps for unsigned comparison
- CMP with immediate value too large for instruction
- Not using TEST for zero/non-zero checks

## How to Fix

### Use correct comparison

```asm
; WRONG: comparing in wrong order
cmp rax, rbx  ; flags set based on rax - rbx

; For "if (a < b)" use JL after CMP
cmp rax, rbx
jl .less_than
```

### Use TEST for zero checks

```asm
; WRONG: CMP with zero
cmp eax, 0

; CORRECT: TEST is faster
test eax, eax
jz .is_zero
```

## Examples

```asm
; Signed comparison
    cmp edi, esi
    jl .less
    jg .greater
    je .equal

; Unsigned comparison
    cmp edi, esi
    jb .below
    ja .above
    je .equal
```
