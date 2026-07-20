---
title: "[Solution] Assembly Segment Override Error — How to Fix"
description: "Fix segment override prefix errors in assembly when using CS, DS, ES, FS, or GS to override default segment selection."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1038
---

# Segment Override Error

Segment override prefixes (CS=0x2E, DS=0x3E, ES=0x26, FS=0x64, GS=0x65) change the default segment for memory accesses. In 64-bit mode, only FS and GS overrides are meaningful; CS/DS/ES/SS overrides are treated as prefixes to other instructions.

## Common Causes

- Using DS override in 64-bit mode (ignored, may cause wrong instruction)
- FS/GS base not set via MSR (FSBASE/GSBASE)
- Stack accesses with wrong segment override
- Segment override on instructions that don't accept it (PUSH/POP)

## How to Fix

### Solution 1 — Use FS/GS for thread-local storage in 64-bit mode

```assembly
; Set GS base for per-CPU data (kernel)
set_gs_base:
    mov ecx, 0xC0000101   ; IA32_GS_BASE MSR
    mov eax, rdi           ; low 32 bits of base
    shr rdi, 32
    mov edx, edi           ; high 32 bits
    wrmsr
    ret

; Access per-CPU data via GS override
    mov rax, gs:[0]        ; read first field of per-CPU struct
```

### Solution 2 — Set FS base for user-space TLS

```assembly
set_fs_base:
    mov ecx, 0xC0000100   ; IA32_FS_BASE MSR
    mov eax, rdi
    shr rdi, 32
    mov edx, edi
    wrmsr
    ret

; Access TLS via FS override
    mov rax, fs:[0]        ; first TLS slot
```

### Solution 3 — Avoid CS/DS overrides in 64-bit mode

```assembly
; WRONG in 64-bit: CS: is ignored and may confuse assemblers
    ; cs:mov eax, [rbx]    ; meaningless in long mode

; CORRECT: use RIP-relative or explicit addressing
    mov rax, [rbx]         ; normal memory access
```

### Solution 4 — Use segment override for kernel data access

```assembly
; In kernel mode, use GS to access current task struct
current_task:
    mov rax, gs:[current_task_offset]
    ret

section .data
current_task_offset: dq 0  ; set at boot
```

## Examples

A kernel sets up GS base to point to per-CPU data. During an interrupt, GS is not saved/restored. The handler reads stale GS data and accesses the wrong CPU's stack. Saving/restoring GS in the interrupt frame fixes the issue.

## Related Errors

- [GDT Error](/languages/assembly/asm-gdt-error) — segment descriptor setup
- [Page Fault](/languages/assembly/asm-page-fault-error) — memory access
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — ring transitions
