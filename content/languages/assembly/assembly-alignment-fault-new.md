---
title: "[Solution] Assembly: general protection fault or alignment check"
description: "Fix Assembly general protection faults by aligning data access and respecting operand size rules."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A general protection fault (#GP) in Assembly is a processor exception that occurs when the CPU detects a protection violation. This includes unaligned memory access when alignment checking is enabled, segment limit violations, accessing privileged registers or instructions from user mode, and invalid operand combinations. On Linux, this produces a SIGSEGV signal with a different fault code than null pointer dereference. The error indicates that the instruction violated the processor's protection rules rather than simply accessing unmapped memory.

## Why It Happens

General protection faults occur from several violation types. Unaligned memory access on architectures that enforce alignment (or when AC flag is set) causes #GP when accessing a multi-byte value at an address not divisible by its size. For example, loading a 32-bit value from an address that is not 4-byte aligned can trigger this. Using incorrect operand size combinations, such as loading a 64-bit value into a 32-bit segment, produces #GP. Attempting to execute privileged instructions (like `cli`, `sti`, `lgdt`, `mov cr0`) from ring 3 (user mode) causes a protection fault. Accessing memory beyond segment limits, using invalid segment selectors, or writing to read-only code segments all trigger #GP. Incorrect use of the `iret` instruction or returning to an invalid code segment also produces this fault.

## How to Fix It

**Ensure proper memory alignment:**

```asm
section .data
    ; WRONG: unaligned data
    ; value_at_odd db 0, 0, 0, 0
    ; align 1  ; Not aligned

    ; CORRECT: align data properly
    align 4
    aligned_value dd 42

    align 8
    aligned_qword dq 0x1234567890ABCDEF

section .text
    ; WRONG: accessing unaligned data
    ; mov eax, [unaligned_addr]

    ; CORRECT: use aligned addresses
    mov eax, [aligned_value]
```

**Use proper segment registers:**

```asm
; WRONG: using wrong segment
; mov ax, ds
; mov es, ax  ; If DS is invalid, this faults

; CORRECT: ensure segments are properly set up
; In 64-bit mode, segment registers are mostly ignored
; but FS and GS are used for thread-local storage

; For 32-bit code, set up segments properly
section .text
global _start
_start:
    ; Set up data segment
    mov ax, 0x10       ; Data segment selector
    mov ds, ax
    mov es, ax
```

**Avoid privileged instructions in user mode:**

```asm
; WRONG: privileged instructions from ring 3
; cli              ; Clear interrupts - requires ring 0
; sti              ; Set interrupts - requires ring 0
; hlt              ; Halt processor - requires ring 0
; in al, 0x60      ; Port I/O - may require ring 0

; CORRECT: use system calls instead
; For I/O, use syscalls or /dev/port
; For halt, use the exit syscall
    mov rax, 60     ; SYS_exit
    xor rdi, rdi
    syscall
```

**Check alignment with compiler directives:**

```bash
# NASM: enforce alignment
nasm -f elf64 program.asm

# GAS: use .align directive
as --64 program.s

# GCC: link with alignment checking
gcc -o program program.o


## Common Mistakes

- Not aligning data to the required boundary for the data type size
- Using `movaps` (aligned) instead of `movups` (unaligned) for potentially unaligned addresses
- Attempting I/O port access from user mode without proper privileges
- Not setting up segment registers correctly in 32-bit code
- Mixing 32-bit and 64-bit operations inappropriately

## Related Pages

- [Segmentation fault null pointer in Assembly](/languages/assembly/assembly-segfault-null-new)
- [Invalid opcode in Assembly](/languages/assembly/assembly-invalid-opcode-new)
- [Page fault in Assembly](/languages/assembly/assembly-page-fault-new)
- [Stack smashing in Assembly](/languages/assembly/assembly-stack-smashing-new)
