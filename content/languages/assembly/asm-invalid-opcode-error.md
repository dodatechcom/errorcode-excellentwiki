---
title: "[Solution] Assembly Invalid Opcode Error -- Undefined Instruction"
description: "Fix assembly invalid opcode errors when the CPU encounters an undefined instruction."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Invalid Opcode Error

This error occurs when the CPU encounters an instruction that is not defined in its instruction set, typically triggering interrupt 6 (#UD).

## Common Causes

- Executing data bytes as code due to incorrect control flow
- Using instructions not supported by the current CPU
- Corrupted instruction pointer (EIP/RIP)
- Mixing 32-bit and 64-bit code incorrectly

## How to Fix

### Verify instruction support

```asm
; WRONG: AVX instruction on non-AVX CPU
vaddps ymm0, ymm1, ymm2

; CORRECT: check CPUID first
cpuid
test ecx, 1 << 28  ; check AVX bit
jz .no_avx
vaddps ymm0, ymm1, ymm2
.no_avx:
```

### Ensure proper alignment

```asm
; Align code to prevent partial instruction fetch
section .text
align 16
my_function:
    push rbp
    mov rbp, rsp
    pop rbp
    ret
```

## Examples

```asm
; Safe instruction execution
section .text
global _start

_start:
    ; Check for CPUID support
    pushfd
    pop eax
    mov ecx, eax
    xor eax, 1 << 21
    push eax
    popfd
    pushfd
    pop eax
    xor eax, ecx
    jz .no_cpuid
    ; CPUID available
.no_cpuid:
    mov eax, 60
    xor edi, edi
    syscall
```
