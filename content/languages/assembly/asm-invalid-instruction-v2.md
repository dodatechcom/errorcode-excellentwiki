---
title: "[Solution] SIGILL: illegal instruction in assembly"
description: "Fix assembly illegal instruction errors when the CPU encounters an opcode it cannot decode or execute."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["illegal-instruction", "sigill", "opcode", "cpu", "ud2", "assembly"]
weight: 5
---

## What This Error Means

SIGILL (illegal instruction) occurs when the processor encounters a byte sequence that doesn't correspond to any valid instruction. This can happen from corrupted code, incorrect assembler output, or jumping to wrong address.

## Common Causes

- Corrupt executable (bad memory, disk error)
- Jumped to wrong address (corrupt function pointer)
- Using CPU-specific instructions on incompatible CPU
- Assembler produced wrong encoding
- Data interpreted as code

## How to Fix

```asm
; WRONG: Jumping to data section
section .data
    mydata dq 0x1234567890ABCDEF

section .text
    jmp mydata   ; Invalid instruction - data is not code

; CORRECT: Jump to code
    jmp my_function
```

```asm
; WRONG: Using AVX-512 on old CPU
; vaddps zmm0, zmm1, zmm2   ; requires AVX-512

; CORRECT: Use CPUID to check features
    cpuid
    test ecx, 1 << 16    ; Check AVX-512F bit
    jz .no_avx512
    ; Safe to use AVX-512 instructions
.no_avx512:
```

```asm
; CORRECT: Proper function pointer table
section .data
    func_table dq func1, func2, func3

section .text
    ; Safe indirect call
    mov rax, [func_table + rdi*8]
    test rax, rax
    jz .invalid
    call rax
.invalid:
```

```asm
; CORRECT: Use ud2 for intentional traps
section .text
    ; Software breakpoint / intentional crash
    ud2  ; Generates SIGILL - use for debugging
```

## How to Debug

- Use `gdb`: `disassemble` to check instruction encoding
- Run with `strace` to see signal delivery
- Check `dmesg` for SIGILL reports

## Related Errors

- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [General Protection](asm-general-protection-v2) - protection faults
- [Alignment Error](asm-alignment-error-v2) - alignment issues
