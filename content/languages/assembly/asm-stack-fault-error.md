---
title: "[Solution] Assembly Stack Fault — How to Fix"
description: "Fix stack fault exceptions in assembly caused by stack segment limit violations or invalid stack operations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1006
---

# Stack Fault (#SS)

Interrupt 12 fires when a stack operation exceeds the stack segment limit or accesses an invalid stack address. In 64-bit long mode, #SS is rare but can occur via IST (Interrupt Stack Table) misconfiguration.

## Common Causes

- Stack pointer below the stack segment base in protected mode
- PUSH/POP exceeding the SS.limit boundary
- Invalid IST index in the IDT causing a stack switch to a bad address
- Nested interrupts exhausting the IST stack

## How to Fix

### Solution 1 — Expand the stack segment limit

```assembly
; Update the TSS stack limit for ring 0
    mov word [tss + 4], STACK_BOTTOM  ; SS0:limit
    mov dword [tss + 8], STACK_TOP   ; SS0:base
```

### Solution 2 — Use a proper IST stack for interrupts

```assembly
; Set up IST entry 1 in the TSS for double-fault handler
    mov qword [tss + 36], ist1_top   ; IST1 pointer
    mov word [tss + 36 + 2], 0       ; reserved
    mov word [tss + 36 + 4], 0x10    ; kernel stack segment
```

### Solution 3 — Verify RSP before push in kernel code

```assembly
kernel_entry:
    cmp rsp, STACK_MIN
    jb .stack_fault
    push rax
    push rbx
    ret
.stack_fault:
    ; switch to IST stack
    mov rsp, [ist1_top]
    call handle_stack_fault
```

## Examples

An interrupt handler without IST configured switches to the same kernel stack already in use. A deep interrupt nest exceeds SS.limit, triggering #SS. Configuring IST for critical handlers provides a guaranteed valid stack.

## Related Errors

- [Stack Overflow](/languages/assembly/asm-stack-overflow) — stack exhaustion
- [Page Fault](/languages/assembly/asm-page-fault-error) — invalid stack page access
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — segment violations
