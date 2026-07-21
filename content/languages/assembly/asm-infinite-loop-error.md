---
title: "[Solution] Assembly Infinite Loop Error -- Never-Terminating Loop"
description: "Fix assembly infinite loop errors when loop conditions are never satisfied."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Infinite Loop Error

This error occurs when assembly loops run indefinitely because the exit condition is never met.

## Common Causes

- Loop counter not decremented/incremented
- Comparison using wrong flags or registers
- Jump condition inverted (JE instead of JNE)
- Missing BREAK or RET instruction inside loop

## How to Fix

### Ensure loop variable changes

```asm
; WRONG: ECX never decrements
.loop:
    ; ... body ...
    jmp .loop  ; infinite loop

; CORRECT: decrement counter
.loop:
    dec ecx
    jnz .loop  ; exits when ECX = 0
```

### Use correct jump conditions

```asm
; Process array until NULL terminator
lea rsi, [array]
.loop:
    lodsb
    test al, al
    jz .done     ; jump if zero (NULL found)
    ; process byte
    jmp .loop
.done:
    ret
```

## Examples

```asm
; Loop with proper termination
count_down:
    mov ecx, 10
.loop:
    push rcx
    ; do work
    pop rcx
    dec ecx
    jnz .loop
    ret
```
