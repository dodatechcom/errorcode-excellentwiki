---
title: "[Solution] Assembly NASM vs GAS Syntax Error — How to Fix"
description: "Fix NASM vs GAS assembler syntax errors when code written for one assembler is assembled with the other."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1034
---

# NASM vs GAS Syntax Error

NASM (Netwide Assembler) and GAS (GNU Assembler) use different syntax conventions. NASM uses Intel syntax with no `%` prefixes for directives, while GAS uses AT&T syntax by default with different operand ordering.

## Common Causes

- Operand order reversed: GAS is `src, dst`; NASM is `dst, src`
- GAS uses `%` for registers (`%eax`); NASM uses bare names (`eax`)
- GAS uses `$` for immediates (`$42`); NASM uses bare numbers (`42`)
- GAS uses `()` and `()` for memory; NASM uses `[]`

## How to Fix

### Solution 1 — Convert GAS Intel syntax

```bash
# Assemble with Intel syntax in GAS
as --syntax=intel -o output.o input.s
```

### Solution 2 — GAS to NASM translation reference

```assembly
; GAS AT&T:                    ; NASM Intel:
; movl $42, %eax               mov eax, 42
; movl %eax, (%ebx)            mov [ebx], eax
; addl $8, %esp                add esp, 8
; pushl %eax                   push eax
```

### Solution 3 — Use .intel_syntax in GAS

```assembly
.intel_syntax noprefix
mov eax, 42
mov [ebx], eax
add esp, 8
```

### Solution 4 — Convert NASM to GAS automatically

```bash
# Using asmtool or manual conversion
# Or compile with NASM directly:
nasm -f elf64 -o output.o input.asm
```

## Examples

A developer writes `MOV EAX, [EBP+8]` in NASM syntax but assembles with GAS without `.intel_syntax`. GAS interprets this as AT&T, reversing operands and interpreting registers differently, producing garbage code. Adding `.intel_syntax noprefix` at the top fixes the assembly.

## Related Errors

- [AT&T Syntax Error](/languages/assembly/asm-att-syntax-error) — AT&T specific issues
- [COM File Error](/languages/assembly/asm-com-file-error) — output format
- [MZ/PE Error](/languages/assembly/asm-mz-pe-error) — Windows format
