---
title: "[Solution] Assembly Alignment Check Error — How to Fix"
description: "Fix alignment check exceptions in assembly caused by unaligned memory access when AC flag is set."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1005
---

# Alignment Check Exception (#AC)

Interrupt 17 fires when an unaligned memory access is made with the AC (Alignment Check, EFLAGS bit 18) flag set in ring 0, or on architectures that enforce alignment for SSE instructions.

## Common Causes

- `MOVAPS`/`MOVAPD` on a 16-byte unaligned address
- Accessing packed structures at non-natural alignment on ARM
- Setting EFLAGS.AC in ring 0 enables alignment checking
- Compiler generating aligned loads for unaligned stack layouts

## How to Fix

### Solution 1 — Use unaligned-safe instructions

```assembly
; WRONG: requires 16-byte alignment
    movaps xmm0, [rdi]     ; #AC if RDI % 16 != 0

; CORRECT: unaligned variant
    movups xmm0, [rdi]     ; works at any address
```

### Solution 2 — Align data in BSS/stack

```assembly
section .bss
    alignb 16
    buffer resb 256

section .text
    movaps xmm0, [buffer]  ; guaranteed aligned
```

### Solution 3 — Align stack for SSE

```assembly
my_func:
    push rbp
    mov rbp, rsp
    and rsp, -16           ; force 16-byte alignment
    sub rsp, 64
    movaps [rsp], xmm0     ; safe
```

### Solution 4 — Check alignment before using strict instructions

```assembly
check_align_16:
    test rdi, 0xF
    jnz .unaligned
    movaps xmm0, [rdi]
    ret
.unaligned:
    movups xmm0, [rdi]
    ret
```

## Examples

A matrix library uses `MOVAPS` for vectorized multiplication. When the matrix is dynamically allocated with `malloc` (which may not return 16-byte-aligned memory), unaligned accesses trigger #AC. Switching to `MOVUPS` or ensuring 16-byte alignment fixes the issue.

## Related Errors

- [SSE Error](/languages/assembly/asm-sse-error) — SIMD exception details
- [Stack Fault](/languages/assembly/asm-stack-error) — stack alignment issues
- [Page Fault](/languages/assembly/asm-page-fault-error) — memory mapping
