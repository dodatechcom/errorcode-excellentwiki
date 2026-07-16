---
title: "Illegal instruction"
description: "An illegal instruction error occurs when the CPU encounters an opcode it does not recognize or cannot execute."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cpu", "instruction", "opcode", "illegal"]
weight: 5
---

## What This Error Means

An illegal instruction error (SIGILL) occurs when the processor encounters an instruction opcode that is invalid, reserved, or not supported by the current CPU architecture. This can result from code corruption, incorrect assembler output, or executing data as code.

## Common Causes

- Jumping into the middle of an instruction or data section
- Code compiled for a newer CPU architecture run on an older one (e.g., AVX2 on SSE-only CPU)
- Buffer overflow or memory corruption overwriting code bytes
- Incorrect assembler directives producing wrong opcode encoding

## How to Fix

```asm
; WRONG: Jumping into the middle of a multi-byte instruction
section .text
    mov eax, 0x90909090   ; 4 bytes encoded
    nop                    ; this is within the previous instruction's bytes
    jmp .next              ; may land on a partial instruction

; CORRECT: Use labels that align to instruction boundaries
section .text
    mov eax, 0x90909090
    nop
.next:                    ; label placed at a valid instruction boundary
    jmp .done
.done:
```

```asm
; WRONG: Using CPU-specific instructions without checking support
    vaddps ymm0, ymm1, ymm2   ; requires AVX - illegal on old CPUs

; CORRECT: Use CPUID to check feature support before using extensions
    mov eax, 1
    cpuid
    test ecx, (1 << 28)       ; check AVX bit
    jz .no_avx
    vaddps ymm0, ymm1, ymm2   ; safe to use
.no_avx:
```

## Examples

```asm
section .data
    db 0xFF, 0xFF, 0xFF     ; invalid opcode bytes

section .text
    global _start

_start:
    jmp .data_section        ; jumping into data treated as code

.data_section:
    ; CPU tries to decode 0xFF 0xFF 0xFF as instructions
    ; triggers SIGILL (illegal instruction)

    mov rax, 60
    xor rdi, rdi
    syscall
```

## Related Errors

- [Segmentation fault](/languages/assembly/segmentation-fault)
- [Undefined symbol](/languages/assembly/undefined-symbol)
