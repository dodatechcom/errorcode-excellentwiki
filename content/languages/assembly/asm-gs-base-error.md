---
title: "[Solution] Assembly GS Base Error -- Per-CPU Data Access"
description: "Fix assembly GS base errors when accessing per-CPU data using GS segment override."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly GS Base Error

This error occurs when GS base is used incorrectly for per-CPU data access, typically in kernel or hypervisor code.

## Common Causes

- GS base not initialized for current CPU
- Accessing wrong offset in per-CPU area
- GS base not set correctly during context switch
- Using GS in user mode when FS is for TLS

## How to Fix

### Initialize GS base correctly

```asm
; WRONG: GS base not set
mov rax, [gs:per_cpu_offset]  ; may crash

; CORRECT: ensure GS base is set
; In kernel, GS points to per-CPU data
; per_cpu_offset is relative to GS base
mov rax, [gs:per_cpu_offset]
```

### Read GS base

```asm
; Get current GS base address
read_gs_base:
    swapgs              ; swap GS base (kernel only)
    mov rax, [gs:0]     ; read GS base
    swapgs
    ret
```

## Examples

```asm
; Per-CPU variable access
section .data
per_cpu_data:
    current_task: dq 0
    irq_count: dq 0

section .text
get_current_task:
    mov rax, [gs:current_task]
    ret
```
