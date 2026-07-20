---
title: "[Solution] Assembly REX Prefix Error — How to Fix"
description: "Fix REX prefix errors in assembly when 64-bit operand size or extended register encoding is incorrect."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1030
---

# REX Prefix Error

The REX prefix (0x40-0x4F) in x86-64 encodes 64-bit operand size (REX.W), extends the ModRM reg field (REX.R), extends the r/m field (REX.X), and extends the SIB base (REX.B). Incorrect REX usage causes wrong register selection or operand size.

## Common Causes

- Missing REX.W when accessing 64-bit registers (RAX-15)
- REX prefix on instructions that don't accept it (e.g., PUSH/POP)
- Using REX.R to extend into invalid registers
- REX prefix with operand-size override (0x66) causing unpredictable behavior

## How to Fix

### Solution 1 — Use correct REX for 64-bit operations

```assembly
; WRONG: 32-bit operation (no REX.W)
    mov eax, [rdi]         ; zero-extends to RAX

; CORRECT: 64-bit operation (REX.W = 0x48)
    mov rax, [rdi]         ; full 64-bit load
```

### Solution 2 — Extend to R8-R15 with REX.B/R/RX

```assembly
; Access R8: REX.B = 1 (r/m field) or REX.R = 1 (reg field)
    mov rax, r8            ; REX.R: 49 89 C0
    add r8, rax            ; REX.RB: 4C 01 C0
```

### Solution 3 — Avoid invalid REX combinations

```assembly
; WRONG: REX.W on 8-bit instruction (most are invalid)
    add al, cl             ; OK: no REX
    ; add al, r8b          ; needs REX.R, but REX.W is invalid here

; CORRECT: use REX.R without REX.W for byte registers
    add al, r8b            ; 41 00 C0
```

### Solution 4 — NASM auto-generates REX — verify output

```bash
# Check REX encoding in assembled output
ndisasm -b 64 -o 0x1000 output.bin | head -20
```

## Examples

A developer writes `MOV EAX, R8D` expecting a 32-bit move. R8D requires REX.R=1 to access, but the assembler may generate the wrong encoding without explicit syntax. Using NASM's `r8d` register name automatically adds the correct REX byte.

## Related Errors

- [MODRM Error](/languages/assembly/asm-modrm-error) — addressing mode encoding
- [SIB Error](/languages/assembly/asm-sib-byte-error) — scale-index-base encoding
- [RIP Relative Error](/languages/assembly/asm-rip-relative-error) — RIP-relative addressing
