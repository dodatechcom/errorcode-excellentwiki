---
title: "[Solution] Assembly SIB Byte Error — How to Fix"
description: "Fix SIB (Scale-Index-Base) byte encoding errors in assembly when complex addressing modes are misencoded."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1032
---

# SIB Byte Error

The SIB (Scale-Index-Base) byte follows ModR/M when r/m=100 in 32-bit addressing. It encodes a scaled index register plus a base register. Errors cause incorrect address calculations.

## Common Causes

- Scale factor (1, 2, 4, 8) encoded incorrectly in bits 7-6
- Index=100 (ESP) with SIB is invalid — no index register
- Base=101 with mod=00 means disp32 with no base (special case)
- Not using SIB when addressing [base + index*scale] patterns

## How to Fix

### Solution 1 — NASM handles SIB automatically

```assembly
; SIB is generated for these patterns:
    mov eax, [rbx + rcx*4]       ; SIB: scale=4, index=RCX, base=RBX
    mov eax, [rsp + rdi*8]       ; SIB: scale=8, index=RDI, base=RSP
    mov eax, [rbx + rcx*4 + 8]   ; SIB + disp8
```

### Solution 2 — Understand SIB byte layout

```assembly
; SIB byte: scale(2) | index(3) | base(3)
; Scale: 00=1, 01=2, 10=4, 11=8
; Index: register number (100 = no index)
; Base: register number (101 with mod=00 = disp32 only)
```

### Solution 3 — Avoid invalid index=ESP encoding

```assembly
; WRONG: [ESP + ESP*1] — index=100 is "no index" in SIB
; NASM will use [ESP] instead, ignoring the index

; CORRECT: use a different register
    lea eax, [esp + ecx]    ; uses ecx as index with SIB
```

### Solution 4 — Use LEA for complex address calculation

```assembly
; LEA can calculate addresses without memory access
    lea eax, [rbx + rcx*4 + disp32]
    ; avoids any SIB encoding issues at runtime
```

## Examples

An array access `[base + index*8]` where index=ESP generates a SIB byte with index=100 (no index), silently dropping the index term. The access reads from the wrong address. Using a different register for the index fixes the calculation.

## Related Errors

- [MODRM Error](/languages/assembly/asm-modrm-error) — addressing mode prefix
- [REX Prefix](/languages/assembly/asm-rex-prefix-error) — extended registers
- [RIP Relative Error](/languages/assembly/asm-rip-relative-error) — 64-bit addressing
