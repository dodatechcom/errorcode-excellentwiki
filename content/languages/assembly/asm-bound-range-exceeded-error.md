---
title: "[Solution] Assembly BOUND Range Exceeded — How to Fix"
description: "Fix BOUND range exceeded errors in assembly when array index falls outside the declared bounds."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1008
---

# BOUND Range Exceeded (INT 5)

The `BOUND` instruction (introduced with 80186) checks whether a register value falls within a specified upper/lower bound pair. If the value is outside the range, interrupt 5 fires. The instruction is removed in 64-bit mode.

## Common Causes

- Array index below lower bound or above upper bound
- Using the legacy BOUND instruction in 16/32-bit code
- Compiler-generated bounds checks for debug builds
- Signed overflow producing a value outside expected range

## How to Fix

### Solution 1 — Manual bounds check (64-bit compatible)

```assembly
; BOUND is not available in long mode — emulate it
bound_check:
    cmp eax, [rbx]        ; lower bound
    jl .below
    cmp eax, [rbx + 4]    ; upper bound
    jg .above
    ret
.below:
.above:
    ; raise interrupt 5 or handle error
    int 5
    ret
```

### Solution 2 — Use CMOV for branchless bounds check

```assembly
bounds_check_fast:
    cmp eax, [rbx]        ; < lower?
    setl cl
    cmp eax, [rbx + 4]    ; > upper?
    setg ch
    or cl, ch
    jnz .out_of_bounds
    ret
.out_of_bounds:
    ; handle error
    ret
```

### Solution 3 — Disable BOUND checking in compiler

```bash
# GCC: remove -fbounds-checking
gcc -O2 -o program program.c

# NASM: avoid generating BOUND instructions
nasm -f elf64 file.asm
```

## Examples

A bounds-checked array access in 32-bit mode uses BOUND. If the index is -1, it falls below the lower bound, triggering INT 5. The fix is to use a manual bounds check or switch to 64-bit mode.

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault-error) — out-of-bounds memory access
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — segment limit violation
- [Integer Overflow](/languages/assembly/asm-integer-overflow-asm) — arithmetic overflow
