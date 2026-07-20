---
title: "[Solution] Assembly Undefined Opcode — How to Fix"
description: "Fix undefined opcode errors in assembly when the CPU encounters a byte sequence with no valid instruction mapping."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1009
---

# Undefined Opcode

When the CPU decodes a byte that has no valid instruction encoding, it raises an invalid opcode exception (#UD, interrupt 6). This is similar to SIGILL but specifically for genuinely undefined byte patterns rather than privileged instructions.

## Common Causes

- Jumping into data embedded in the code section
- Corrupted binary (bad linker script, truncated object file)
- Mix of 16-bit and 32-bit code with incorrect prefix usage
- Executing a VEX/EVEX-encoded instruction on a pre-VEX CPU

## How to Fix

### Solution 1 — Place data in .data, not .text

```assembly
section .text
    jmp main

section .data
lookup_table:
    dq 0x1234567890ABCDEF   ; data safely in .data

section .text
main:
    mov rax, [lookup_table]
```

### Solution 2 — Verify instruction encoding with ndisasm

```bash
# Disassemble raw bytes to check encoding
echo -n "4889E5C3" | xxd -r -p | ndisasm -b 64 -
```

### Solution 3 — Align function entry points

```assembly
section .text
    align 16
my_function:
    push rbp
    mov rbp, rsp
    ret
```

### Solution 4 — Check VEX prefix compatibility

```assembly
; WRONG: VEX prefix on pre-Sandy Bridge CPU
    vpaddd ymm0, ymm1, ymm2   ; #UD on pre-AVX

; CORRECT: check CPUID first, then use legacy SSE2 fallback
    paddd xmm0, xmm1          ; works everywhere
```

## Examples

A function pointer table has entries pointing to the wrong addresses. After a function is moved, one entry still points to old code that now contains data bytes. The first call through the stale pointer hits an undefined opcode.

## Related Errors

- [Illegal Instruction](/languages/assembly/asm-illegal-instruction-error) — privileged instruction
- [SIGILL](/languages/assembly/asm-sigill-error) — illegal signal
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — protection violations
