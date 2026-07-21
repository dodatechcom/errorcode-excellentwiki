---
title: "[Solution] Assembly NASM vs GAS Error -- Syntax Confusion"
description: "Fix assembly NASM vs GAS syntax errors when mixing Intel and AT&T syntax."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly NASM vs GAS Error

This error occurs when Intel syntax (NASM) and AT&T syntax (GAS) are mixed or used with the wrong assembler.

## Common Causes

- Using % registers in Intel syntax
- Source and destination operand order reversed
- Immediates prefixed with $ in wrong syntax
- Section directives differ between assemblers

## How to Fix

### Use consistent syntax

```asm
; NASM (Intel syntax):
mov rax, rbx       ; dest, src
add eax, 10        ; no $ prefix
section .text

; GAS (AT&T syntax):
movq %rbx, %rax    ; src, dest
addl $10, %eax     ; $ prefix for immediates
.section .text
```

### Choose one assembler per file

```bash
# NASM
nasm -f elf64 file.asm

# GAS
as --64 file.s
```

## Examples

```asm
; NASM syntax (Intel)
section .text
global _start
_start:
    mov rax, 60
    xor rdi, rdi
    syscall
```
