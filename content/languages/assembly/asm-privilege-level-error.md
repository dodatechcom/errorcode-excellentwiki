---
title: "[Solution] Assembly Privilege Level Error -- Ring 0 vs Ring 3"
description: "Fix assembly privilege level errors when executing privileged instructions in user mode."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Privilege Level Error

This error occurs when privileged instructions (Ring 0) are executed from user mode (Ring 3), causing a general protection fault.

## Common Causes

- Executing IN/OUT instructions from user mode
- Accessing control registers (CR0, CR3, CR4)
- Using LGDT/LIDT from user mode
- CLI/STI instructions require Ring 0

## How to Fix

### Use syscalls instead of privileged instructions

```asm
; WRONG: IN instruction from user mode
in al, 0x60  ; general protection fault

; CORRECT: use syscall for port access
; or use /dev/input for keyboard
mov rax, 0   ; sys_read
mov rdi, 0   ; stdin
lea rsi, [buffer]
mov rdx, 1
syscall
```

### Enter kernel mode via syscall

```asm
; Access hardware via kernel syscalls
get_time:
    mov rax, 201    ; sys_gettimeofday
    lea rdi, [timeval]
    xor esi, esi
    syscall
    ret
```

## Examples

```asm
; User-mode I/O using syscalls
read_port:
    ; Not possible directly, must use kernel
    ; Use ioperm() via syscall if needed
    mov rax, 173    ; sys_ioperm
    mov rdi, 0x60   ; port
    mov rsi, 1      ; enable
    mov rdx, 1      ; for input
    syscall
    ret
```
