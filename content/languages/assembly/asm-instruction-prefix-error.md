---
title: "[Solution] Assembly Instruction Prefix Error -- Invalid Prefix Combinations"
description: "Fix assembly instruction prefix errors when using invalid prefix combinations."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly Instruction Prefix Error

This error occurs when instruction prefixes are used incorrectly or in invalid combinations.

## Common Causes

- Using LOCK prefix with non-atomic instructions
- REP prefix with non-string instructions
- Segment override prefixes with wrong instructions
- REX prefix in 32-bit mode

## How to Fix

### Use prefixes correctly

```asm
; WRONG: LOCK with non-atomic instruction
lock add eax, 1  ; LOCK only works with read-modify-write

; CORRECT: LOCK with atomic operation
lock xadd [counter], eax  ; atomic increment
```

### REP with string instructions only

```asm
; WRONG: REP with non-string instruction
rep mov eax, ebx

; CORRECT: REP with MOVS/STOS/CMPS/SCAS/LODS
cld
rep movsb  ; copy ECX bytes from [RSI] to [RDI]
```

## Examples

```asm
; Atomic increment
atomic_inc:
    mov eax, 1
    lock xadd [rdi], eax
    ret
```
