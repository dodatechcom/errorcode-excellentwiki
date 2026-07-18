---
title: "[Solution] Assembly: invalid opcode or illegal instruction"
description: "Fix Assembly invalid opcode errors by checking CPU compatibility and verifying instruction encoding."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An invalid opcode error in Assembly occurs when the CPU encounters a byte sequence that does not correspond to any valid instruction. On Linux, this produces a SIGILL (Illegal Instruction) signal. On Windows, it triggers an ACCESS_VIOLATION exception with an invalid instruction fault. The error means the processor cannot decode the instruction at the program counter, typically resulting in immediate program termination.

## Why It Happens

Invalid opcode errors stem from several causes. Using CPU-specific instructions on a processor that does not support them is the most common source. For example, using AVX-512 instructions on a CPU that only supports SSE4.2 will trigger this error. Jumping to an address that contains data rather than code causes the CPU to interpret data bytes as instructions. Corrupted executable files, whether from disk errors, incomplete writes, or memory corruption, can produce invalid byte sequences. Assembler bugs that generate incorrect instruction encodings are another cause. Mixing 16-bit, 32-bit, and 64-bit code inappropriately can produce instructions that the current operating mode does not recognize. Self-modifying code that writes incorrect bytes into executable memory also triggers this error.

## How to Fix It

**Check CPU features before using advanced instructions:**

```asm
; WRONG: using AVX without checking support
; vaddps ymm0, ymm1, ymm2  ; Requires AVX support

; CORRECT: check CPUID first
section .text
global _start

_start:
    ; Check for AVX support
    mov eax, 1
    cpuid
    test ecx, 0x10000000  ; Check AVX bit
    jz .no_avx

    ; AVX is supported, use it safely
    vaddps ymm0, ymm1, ymm2
    jmp .done

.no_avx:
    ; Fall back to SSE
    addps xmm0, xmm1

.done:
    mov eax, 60
    xor edi, edi
    syscall
```

**Ensure jumps target valid code:**

```asm
section .data
    mydata dq 0x1234567890ABCDEF  ; Data, not code

section .text
    ; WRONG: jumping to data
    ; jmp mydata  ; Invalid instruction!

    ; CORRECT: jump to code label
    jmp my_function

my_function:
    mov rax, 42
    ret
```

**Verify instruction encoding with objdump:**

```bash
# Disassemble the binary to check encoding
objdump -d myprogram

# Check for unknown bytes between instructions
objdump -d -M intel myprogram | less
```

**Handle SIGILL with a signal handler:**

```asm
section .text
global _start

_start:
    ; Set up SIGILL handler
    mov eax, 2    ; SYS_signal (or use rt_sigaction)
    mov edi, 11   ; SIGILL
    mov esi, handler
    syscall

    ; Code that might have invalid instruction
    nop
    ud2            ; This intentionally triggers SIGILL

.done:
    mov eax, 60
    xor edi, edi
    syscall

handler:
    ; Handle the illegal instruction
    mov rdi, msg
    mov rsi, msg_len
    call print_string
    jmp .done
```

## How to Debug

- Use `gdb` to run the program and examine the instruction at the crash point
- Use `strace` to see the SIGILL signal delivery
- Run `objdump -d` to disassemble and find invalid bytes
- Check `dmesg` for kernel-reported illegal instruction messages

## Common Mistakes

- Not checking CPUID before using SSE, AVX, or AVX-512 instructions
- Assembling with -f elf64 when the code uses 32-bit instructions
- Jumping to data labels instead of code labels
- Using instructions from newer ISA extensions on older hardware
- Mixing NASM and GAS syntax, producing incorrect instruction encodings

## Related Pages

- [Stack smashing detected in Assembly](/languages/assembly/assembly-stack-smashing-new)
- [Segmentation fault null pointer in Assembly](/languages/assembly/assembly-segfault-null-new)
- [SSE illegal instruction in Assembly](/languages/assembly/assembly-sse-error-new)
- [General protection fault in Assembly](/languages/assembly/assembly-alignment-fault-new)
