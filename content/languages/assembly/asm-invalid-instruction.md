---
title: "Invalid instruction in Assembly"
description: "An invalid instruction error occurs when the CPU encounters an opcode it cannot decode or execute."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

"Invalid instruction" (SIGILL) occurs when the processor encounters a byte sequence that doesn't correspond to any valid instruction. This can happen from corrupted code, incorrect assembler output, or jumping to wrong address.

## Common Causes

- Corrupt executable (bad memory, disk error)
- Jumped to wrong address (corrupt function pointer)
- Using CPU-specific instructions on incompatible CPU
- Assembler produced wrong encoding
- Data interpreted as code

## How to Fix

```asm
; Check for correct instruction encoding
; WRONG: Using AVX-512 on old CPU
; vaddps zmm0, zmm1, zmm2   ; requires AVX-512

; CORRECT: Use compatible instructions
; Use CPUID to check features before using advanced instructions
```

```asm
; WRONG: Jumping to data section
section .data
    mydata dq 0x1234567890ABCDEF

section .text
    jmp mydata   ; Invalid instruction - data is not code

; CORRECT: Jump to code
    jmp my_function
```

## Examples

```asm
; Invalid instruction from corrupted code
section .text
    db 0xFF, 0xFF   ; Not a valid instruction - SIGILL

; Correct: use proper instructions
    nop              ; Valid no-operation
```

## How to Debug

- Use `gdb`: `disassemble` to check instruction encoding
- Run with `strace` to see signal delivery
- Check `dmesg` for SIGILL reports

## Related Errors

- [Segmentation Fault](/languages/assembly/segmentation-fault) - memory access violations
- [General Protection Fault](/languages/assembly/asm-general-protection) - protection violations
