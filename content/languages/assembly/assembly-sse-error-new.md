---
title: "[Solution] Assembly: SSE or SSE2 illegal instruction"
description: "Fix Assembly SSE illegal instructions by detecting CPU features with CPUID and using proper alignment."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An SSE or SSE2 illegal instruction error occurs when the program executes an SSE instruction on a CPU that does not support the required instruction set extension. On Linux, this produces a SIGILL signal. SSE requires at minimum a Pentium III or AMD Athlon processor. SSE2 requires a Pentium 4 or AMD Opteron/Athlon 64. Using SSE3, SSSE3, SSE4.1, SSE4.2, or later extensions on CPUs that lack support triggers the same error. The error can also occur when SSE instructions are used on data that is not properly aligned to 16-byte boundaries.

## Why It Happens

SSE illegal instructions occur when the code is compiled or assembled for a target architecture that is newer than the actual hardware. Distributing binaries compiled with `-march=native` on a machine with AVX2 to a machine without it causes SIGILL. Using aligned SSE instructions like `movaps` on unaligned data does not cause SIGILL but may cause SIGSEGV on some systems. Mixing x87 FPU and SSE code without proper state management can produce unexpected behavior. Using SSE instructions without first enabling the OS to save/restore XMM registers (via CR4.OSFXSR) causes faults. On older Linux systems, the kernel may not have set up SSE support, causing instruction faults.

## How to Fix It

**Check for SSE support using CPUID:**

```asm
section .text
global check_sse

check_sse:
    push rbx

    ; Check for SSE
    mov eax, 1
    cpuid
    test edx, 0x02000000   ; SSE bit in EDX
    jz .no_sse

    ; Check for SSE2
    test edx, 0x04000000   ; SSE2 bit in EDX
    jz .no_sse2

    ; Both SSE and SSE2 available
    pop rbx
    mov rax, 2             ; SSE2 available
    ret

.no_sse2:
    pop rbx
    mov rax, 1             ; SSE only
    ret

.no_sse:
    pop rbx
    xor rax, rax           ; No SSE
    ret
```

**Ensure proper alignment for SSE operations:**

```asm
section .data
    align 16               ; 16-byte alignment required
    vector_a: dd 1.0, 2.0, 3.0, 4.0
    align 16
    vector_b: dd 5.0, 6.0, 7.0, 8.0
    align 16
    result: dd 0.0, 0.0, 0.0, 0.0

section .text
sse_add:
    ; WRONG: unaligned data
    ; movaps xmm0, [un_aligned_data]

    ; CORRECT: aligned data
    movaps xmm0, [vector_a]     ; Load aligned
    movaps xmm1, [vector_b]
    addps xmm0, xmm1            ; Add packed singles
    movaps [result], xmm0       ; Store aligned
    ret
```

**Use unaligned instructions when alignment is not guaranteed:**

```asm
; When data might not be 16-byte aligned
; Use movups instead of movaps
safe_load:
    movups xmm0, [rdi]      ; Unaligned load (works anywhere)
    ret

; Use movupd instead of movapd for doubles
safe_load_double:
    movupd xmm0, [rdi]      ; Unaligned double load
    ret
```

**Compile with appropriate target settings:**

```bash
# NASM: target specific architecture
nasm -f elf64 -o program.o program.asm

# If using GCC to assemble .S files
gcc -msse2 -o program program.s    # Enable SSE2
gcc -mno-sse -o program program.s  # Disable SSE

# For portable binaries, avoid SSE in assembly or check at runtime


## Common Mistakes

- Not checking CPUID for SSE support before executing SSE instructions
- Using `movaps` (aligned) when data may not be 16-byte aligned
- Forgetting that SSE support must be enabled by the OS (CR4.OSFXSR)
- Not providing a fallback path for older CPUs
- Assuming all x86-64 CPUs support SSE2 (they do, but 32-bit code may run on older CPUs)

## Related Pages

- [x87 FPU exception in Assembly](/languages/assembly/assembly-fpu-error-new)
- [Invalid opcode in Assembly](/languages/assembly/assembly-invalid-opcode-new)
- [General protection fault in Assembly](/languages/assembly/assembly-alignment-fault-new)
- [Stack smashing in Assembly](/languages/assembly/assembly-stack-smashing-new)
