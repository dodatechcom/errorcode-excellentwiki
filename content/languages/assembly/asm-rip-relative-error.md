---
title: "[Solution] Assembly RIP-Relative Addressing Error — How to Fix"
description: "Fix RIP-relative addressing errors in assembly when position-independent code uses incorrect offsets."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1033
---

# RIP-Relative Addressing Error

In 64-bit mode, memory operands default to RIP-relative addressing when mod=00 and r/m=101. This is essential for position-independent code (PIC). Errors occur when the offset is calculated incorrectly or absolute addressing is needed but not used.

## Common Causes

- Using `[disp32]` instead of `[rip+disp32]` — NASM syntax confusion
- Offset larger than ±2GB (cannot encode in signed 32-bit displacement)
- Linker placing code/data too far apart for RIP-relative offset
- Using absolute addressing in shared libraries (breaks PIC)

## How to Fix

### Solution 1 — Use NASM's RIP-relative syntax

```assembly
; NASM: explicit [rel symbol] for RIP-relative
    mov eax, [rel my_data]     ; RIP-relative
    lea rdi, [rel my_data]     ; RIP-relative (preferred for PIC)

; Without 'rel', NASM may use absolute addressing:
    mov eax, [my_data]         ; may be absolute (not PIC)
```

### Solution 2 — Place data near code

```assembly
section .text
my_func:
    lea rax, [rel nearby_data]  ; within ±2GB
    mov eax, [rax]
    ret

section .data
nearby_data: dd 42
```

### Solution 3 — Use GOT for far data in shared libraries

```assembly
; In PIC code, access global data through GOT
    mov rax, [rel GOT_base]    ; load GOT address
    mov rax, [rax + symbol_offset]  ; load symbol from GOT
```

### Solution 4 — Verify with objdump

```bash
# Check if addressing is RIP-relative
objdump -d -M intel binary | grep "rip"
```

## Examples

A shared library accesses a global variable using absolute addressing. When loaded at a different address, the absolute address is wrong. Switching to `[rel var]` makes the access RIP-relative and relocatable.

## Related Errors

- [MODRM Error](/languages/assembly/asm-modrm-error) — encoding field
- [REX Prefix](/languages/assembly/asm-rex-prefix-error) — 64-bit registers
- [SIB Byte](/languages/assembly/asm-sib-byte-error) — scale indexing
