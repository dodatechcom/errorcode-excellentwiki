---
title: "[Solution] Assembly Zero Flag Error — How to Fix"
description: "Fix zero flag errors in assembly when conditional jumps misinterpret the ZF state after non-arithmetic operations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1018
---

# Zero Flag Error

The zero flag (ZF, EFLAGS bit 6) is set when an operation produces a zero result. Misreading ZF after operations that do not set flags, or after operations that modify flags unexpectedly, causes incorrect branching.

## Common Causes

- Testing ZF after `MOV` (which does not modify flags)
- Using JZ/JNZ after `POP` or `LEA` (flags not affected)
- Interrupt between flag-setting and conditional jump modifying EFLAGS
- Confusing ZF with CF after unsigned comparisons

## How to Fix

### Solution 1 — Use TEST or CMP before conditional jumps

```assembly
; WRONG: MOV does not set flags
    mov eax, [rdi]
    jz .zero_value         ; ZF is stale!

; CORRECT: use TEST
    mov eax, [rdi]
    test eax, eax
    jz .zero_value         ; ZF set correctly
```

### Solution 2 — Preserve flags across calls

```assembly
    cmp eax, ebx
    pushfq                 ; save flags
    call some_function     ; may clobber flags
    popfq                  ; restore flags
    je .equal              ; ZF is now correct
```

### Solution 3 — Use LAHF/SAHF for flag preservation

```assembly
    test eax, eax
    lahf                   ; store flags in AH
    call clobber_fn
    sahf                   ; restore flags
    jz .was_zero
```

### Solution 4 — Use CMOVcc instead of branching

```assembly
; Conditional move avoids the ZF interpretation problem
    test eax, eax
    setz cl                ; cl = 1 if zero
    movzx ecx, cl
    ; use ecx directly instead of branching
```

## Examples

A loop counter is decremented with `DEC` and then `JNZ` is used. If the counter is loaded with `MOV` (which does not set flags) instead of `DEC`, the branch always takes the wrong path. Using `TEST` before the jump fixes the logic.

## Related Errors

- [Carry Flag](/languages/assembly/asm-carry-flag-error) — unsigned overflow detection
- [Overflow Flag](/languages/assembly/asm-overflow-flag-error) — signed overflow
- [EFLAGS](/languages/assembly/asm-eflags-error) — register state issues
