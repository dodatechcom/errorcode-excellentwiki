---
title: "[Solution] Assembly SIGFPE Error — How to Fix"
description: "Fix SIGFPE (floating-point exception) errors in assembly caused by integer divide-by-zero or FP exceptions."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1001
---

# SIGFPE — Floating-Point Exception

SIGFPE (signal 8) is raised for integer divide-by-zero (`IDIV` with divisor 0 or `DIV` overflow) and, when unmasked, for x87/SSE floating-point errors. Despite the name, most SIGFPE crashes are integer division issues.

## Common Causes

- `IDIV` or `DIV` with a zero divisor
- `DIV` producing a quotient that does not fit in the destination register
- Unmasked x87 exception via `#MF` (interrupt 16)
- Unmasked SSE exception via `#XF` (interrupt 19) with MXCSR flags

## How to Fix

### Solution 1 — Check divisor before IDIV

```assembly
idiv_safe:
    test rsi, rsi
    jz .divide_by_zero
    cqo
    idiv rsi
    ret
.divide_by_zero:
    mov rax, -1
    ret
```

### Solution 2 — Check DIV overflow (quotient > destination)

```assembly
div_safe:
    ; rdx:rax / rcx — ensure quotient fits in rax
    cmp rdx, rcx
    jae .overflow
    xor rdx, rdx
    div rcx
    ret
.overflow:
    mov rax, -1
    ret
```

### Solution 3 — Mask SSE exceptions

```assembly
mask_sse:
    stmxcsr [old_mxcsr]
    mov eax, [old_mxcsr]
    or eax, 0x1F80           ; mask all 5 SSE exceptions
    mov [new_mxcsr], eax
    ldmxcsr [new_mxcsr]
    ; now FP exceptions are masked — invalid ops return NaN
```

### Solution 4 — Handle x87 exceptions with control word

```assembly
mask_x87:
    fnstcw [old_cw]
    mov ax, [old_cw]
    or ax, 0x003F            ; mask all 6 x87 exceptions
    mov [new_cw], ax
    fldcw [new_cw]
```

## Examples

A division routine receives user-supplied divisor values. Without a zero check, `IDIV` triggers SIGFPE. Adding the guard from Solution 1 prevents the crash.

## Related Errors

- [Floating-Point Error](/languages/assembly/asm-fpu-error) — x87 exception details
- [Division by Zero](/languages/assembly/asm-divide-error) — integer divide-by-zero
- [SSE Error](/languages/assembly/asm-sse-error) — alignment and SIMD faults
