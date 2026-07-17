---
title: "Invalid register in Assembly"
description: "Invalid register errors in Assembly occur when using register names incorrectly or accessing registers not available on the target architecture."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["register", "invalid", "syntax", "assembler", "x86"]
weight: 5
---

## What This Error Means

The assembler reports an invalid register when the register name is misspelled, doesn't exist on the target architecture, or is used in an incompatible context (e.g., 64-bit register in 32-bit mode).

## Common Causes

- Typo in register name (e.g., `ecx` as `ecxx`)
- Using 64-bit registers in 32-bit mode
- Using register not available on target CPU
- Wrong register size for instruction

## How to Fix

```asm
; WRONG: Misspelled register
mov eax, ebx    ; correct
mov eax, exx    ; Error: invalid register

; CORRECT: Use valid register names
mov eax, ebx    ; 32-bit registers
mov rax, rbx    ; 64-bit registers
```

```asm
; WRONG: Wrong size for instruction
section .bits 32
    mov rax, rbx   ; Error: rax not available in 32-bit

; CORRECT: Use matching size
section .bits 32
    mov eax, ebx   ; 32-bit registers in 32-bit mode
```

## Examples

```asm
; Valid x86-64 registers:
; rax, rbx, rcx, rdx, rsi, rdi, rbp, rsp
; r8-r15 (64-bit only)
; eax, ebx, etc. (32-bit)
; ax, bx, etc. (16-bit)
; al, bl, etc. (8-bit)

mov eax, r8b   ; Valid: r8 low byte
mov rax, eax   ; Valid: zero-extends 32 to 64
```

## How to Debug

- Check assembler documentation for valid registers
- Verify target architecture flags (e.g., `-f elf64`)
- Use `nasm -v` to check version

## Related Errors

- [Invalid Instruction](/languages/assembly/asm-invalid-instruction) - opcode errors
- [Invalid Operand](/languages/assembly/asm-invalid-operand) - operand errors
