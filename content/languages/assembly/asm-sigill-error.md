---
title: "[Solution] Assembly SIGILL Error — How to Fix"
description: "Fix SIGILL (illegal instruction) errors in assembly caused by executing invalid or unsupported CPU instructions."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1000
---

# SIGILL — Illegal Instruction

The kernel delivers SIGILL (signal 4) when the CPU encounters an opcode it cannot decode. This usually means the binary was assembled for a different architecture, or a stray byte landed in the .text section.

## Common Causes

- Executing data embedded in .text instead of code
- Running AVX-512 code on a CPU that only supports SSE4
- Compiler/assembler emitting instructions for a newer ISA level
- Corrupted function pointer jumping into the middle of an instruction

## How to Fix

### Solution 1 — Check CPUID before using advanced instructions

```assembly
check_avx:
    mov eax, 1
    cpuid
    test ecx, 1 << 28        ; check OSXSAVE
    jz .no_avx
    xor ecx, ecx
    xgetbv
    test eax, 1 << 1         ; check AVX state
    jz .no_avx
    ; AVX available — safe to use VEX-encoded instructions
    ret
.no_avx:
    ; fall back to SSE2 path
    ret
```

### Solution 2 — Guard against stray data in .text

```assembly
section .text
    jmp start
    dq 0xDEADBEEFCAFEBABE    ; data accidentally in .text → SIGILL if hit
start:
    mov rax, 1
    ret
```

### Solution 3 — Verify assembler target

```bash
# NASM: specify correct CPU level
nasm -f elf64 -O2 -g file.asm

# If using AVX-512, ensure the CPU supports it
grep -o 'avx512' /proc/cpuinfo
```

### Solution 4 — Decode the faulting instruction

```bash
# Find RIP at crash, then disassemble around it
objdump -d -M intel binary | grep -A5 "fault_address"
```

## Examples

Running an AVX2 `vpaddd` on an Atom processor without AVX support triggers SIGILL. The fix is to add a CPUID check and provide an SSE2 fallback path.

## Related Errors

- [General Protection Fault](/languages/assembly/asm-general-protection) — privilege violations
- [Page Fault](/languages/assembly/asm-page-fault-error) — invalid memory access
- [Invalid Instruction](/languages/assembly/asm-invalid-instruction) — assembler encoding errors
