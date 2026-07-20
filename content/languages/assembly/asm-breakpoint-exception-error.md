---
title: "[Solution] Assembly Breakpoint Exception — How to Fix"
description: "Fix breakpoint exceptions in assembly caused by INT 3 instructions and software breakpoint handling."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1014
---

# Breakpoint Exception (#BP, INT 3)

The breakpoint exception (interrupt 3) fires when the CPU executes the `INT 3` (0xCC) instruction. It is the standard mechanism for software breakpoints used by debuggers.

## Common Causes

- Debugger inserting INT 3 at function entry for breakpoint
- INT 3 used as a crash/panic trap (e.g., kernel panic)
- Misaligned instruction stream causing 0xCC to appear as data
- Signal handler returning to an address that lands on INT 3

## How to Fix

### Solution 1 — Handle breakpoint in signal handler

```assembly
bp_handler:
    ; SIGTRAP handler — rdi = siginfo_t, rsi = ucontext_t
    push rbp
    mov rbp, rsp
    mov rax, [rsi + 128]    ; get RIP from ucontext
    dec rax                  ; INT 3 is 1-byte instruction
    mov [rsi + 128], rax    ; move RIP back before the INT 3
    ; log breakpoint hit
    pop rbp
    iretq
```

### Solution 2 — Use INT 3 as deliberate trap

```assembly
panic:
    ; intentional crash with stack trace
    push rdi
    push rsi
    push rdx
    mov rdi, panic_msg
    call print_string
    int 3                   ; debugger trap
    jmp halt

section .data
panic_msg: db "PANIC: unrecoverable error", 10, 0
```

### Solution 3 — Check for INT 3 in memory scan

```assembly
scan_for_bp:
    mov al, 0xCC            ; INT 3 opcode
    mov rcx, scan_length
    lea rdi, [scan_start]
    repne scasb
    jnz .not_found
    dec rdi                 ; rdi points to INT 3
    ; found breakpoint
.not_found:
    ret
```

## Examples

A kernel uses INT 3 as a panic trap. When a fatal error occurs, the code prints a message and executes INT 3. The debugger catches the breakpoint and can inspect the kernel state. The handler adjusts RIP back by one byte before returning.

## Related Errors

- [Debug Exception](/languages/assembly/asm-debug-exception-error) — hardware breakpoints
- [Single Step](/languages/assembly/asm-single-step-error) — trap flag stepping
- [Illegal Instruction](/languages/assembly/asm-illegal-instruction-error) — INT in ring 3
