---
title: "[Solution] Assembly Coprocessor Error — How to Fix"
description: "Fix coprocessor errors in assembly when the x87 FPU or numeric coprocessor is not available or not responding."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1010
---

# Coprocessor Not Available (INT 7)

Interrupt 7 fires when an x87 FPU instruction is executed but the coprocessor is not present, the EM (Error Mask) bit in CR0 is set, or the TS (Task Switched) bit is set while waiting for the FPU.

## Common Causes

- CR0.EM = 1: FPU emulation mode — all x87 instructions trap
- CR0.TS = 1: lazy FPU context switch — trap until FXSAVE/FXRSTOR
- Running FPU code on hardware without a math coprocessor
- Incorrectly configured CR0 after a context switch

## How to Fix

### Solution 1 — Clear EM and TS bits in CR0

```assembly
enable_fpu:
    mov rax, cr0
    and eax, ~(1 << 3)     ; clear EM
    and eax, ~(1 << 8)     ; clear TS
    mov cr0, rax
    fninit                  ; initialize FPU
    ret
```

### Solution 2 — Use CLTS to clear TS before FPU instructions

```assembly
fpu_context_restore:
    clts                   ; clear TS flag in CR0
    fxrstor [fpu_state]    ; restore FPU context
    ; FPU instructions are now safe
```

### Solution 3 — Check for FPU hardware at boot

```assembly
check_fpu:
    mov eax, cr0
    test eax, 1 << 4       ; check NE (Numeric Error) bit
    jnz .fpu_present
    ; FPU not present — enable emulation in software
    or eax, 1 << 3         ; set EM
    mov cr0, eax
.fpu_present:
    ret
```

### Solution 4 — Use emulated FPU for old hardware

```assembly
; Software float library fallback
soft_float_add:
    ; Add two 64-bit floats in software when no FPU
    ; (simplified — real implementation is complex)
    call fp_lib_add
    ret
```

## Examples

An OS kernel sets CR0.TS during task switches for lazy FPU context saving. When a new task first executes an FPU instruction, INT 7 fires. The handler saves the previous task's FPU state, restores the current task's state, and clears TS before returning.

## Related Errors

- [FPU Error](/languages/assembly/asm-fpu-error) — floating-point exceptions
- [SIGFPE](/languages/assembly/asm-sigfpe-error) — divide by zero
- [SSE Error](/languages/assembly/asm-sse-error) — SIMD exceptions
