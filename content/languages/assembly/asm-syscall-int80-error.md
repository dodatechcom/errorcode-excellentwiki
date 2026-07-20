---
title: "[Solution] Assembly Syscall vs Int 0x80 Error — How to Fix"
description: "Fix syscall interface errors in assembly when mixing the SYSCALL instruction with the legacy INT 0x80 calling convention."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1024
---

# Syscall vs Int 0x80 Error

Linux provides two mechanisms for system calls: the modern `SYSCALL` instruction (64-bit fast path) and the legacy `INT 0x80` (32-bit compatibility). Mixing them or using the wrong register conventions causes wrong system call numbers, incorrect arguments, or crashes.

## Common Causes

- Using INT 0x80 with 64-bit registers — only low 32 bits are passed, sign-extending
- Using SYSCALL in 32-bit mode (SYSCALL is 64-bit only)
- Not preserving RCX/R11 (clobbered by SYSCALL)
- Wrong syscall number: SYSCALL uses RAX, INT 0x80 uses EAX

## How to Fix

### Solution 1 — Use SYSCALL for 64-bit programs

```assembly
; 64-bit write() — SYSCALL convention
sys_write:
    mov rax, 1             ; sys_write (64-bit number)
    mov rdi, 1             ; stdout
    lea rsi, [message]
    mov rdx, 13            ; length
    syscall
    ret

section .data
message: db "Hello, world", 10
```

### Solution 2 — Use INT 0x80 for 32-bit programs only

```assembly
; 32-bit write() — INT 0x80 convention
sys_write32:
    mov eax, 4             ; sys_write (32-bit number)
    mov ebx, 1             ; stdout
    mov ecx, message
    mov edx, 13
    int 0x80
    ret
```

### Solution 3 — Preserve registers clobbered by SYSCALL

```assembly
sys_read_safe:
    push rcx               ; SYSCALL clobbers RCX (return address)
    push r11               ; SYSCALL clobbers R11 (RFLAGS)
    mov rax, 0             ; sys_read
    mov rdi, 0             ; stdin
    lea rsi, [buffer]
    mov rdx, 256
    syscall
    pop r11
    pop rcx
    ret

section .bss
buffer: resb 256
```

### Solution 4 — Check architecture before choosing method

```assembly
    ; For 32-bit compatibility layer
    cmp word [cs:0], 0x33  ; check if in 64-bit mode
    je .use_syscall
    int 0x80
    ret
.use_syscall:
    syscall
    ret
```

## Examples

A 64-bit program uses `INT 0x80` with `RDI` set to a 64-bit pointer. The kernel only reads the lower 32 bits and sign-extends, causing the pointer to point to an address in the upper canonical half. Switching to SYSCALL fixes the pointer truncation.

## Related Errors

- [Syscall Error](/languages/assembly/asm-syscall-error) — syscall number issues
- [Calling Convention](/languages/assembly/asm-calling-convention-error) — ABI mismatches
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — ring transitions
