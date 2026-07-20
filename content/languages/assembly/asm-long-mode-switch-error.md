---
title: "[Solution] Assembly Long Mode Switch Error — How to Fix"
description: "Fix long mode switch errors in assembly when transitioning between protected mode and 64-bit long mode."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1020
---

# Long Mode Switch Error

Switching between protected mode (IA-32) and 64-bit long mode requires enabling PAE, setting CR4.PAE, loading a valid PML4 table into CR3, and setting IA32_EFER.LME. Errors during this sequence cause a triple fault and reboot.

## Common Causes

- Setting EFER.LME without enabling CR4.PAE first
- CR3 not pointing to a valid 4-level page table (PML4)
- Attempting to enable long mode from real mode without PAE paging
- Disabling paging (CR0.PG=0) while in long mode

## How to Fix

### Solution 1 — Enable long mode step by step

```assembly
enable_long_mode:
    ; Step 1: Enable PAE
    mov eax, cr4
    or eax, 1 << 5         ; CR4.PAE
    mov cr4, eax

    ; Step 2: Load PML4 into CR3
    mov eax, pml4_table
    mov cr3, eax

    ; Step 3: Set LME in EFER
    mov ecx, 0xC0000080    ; IA32_EFER MSR
    rdmsr
    or eax, 1 << 8         ; LME
    wrmsr

    ; Step 4: Enable paging
    mov eax, cr0
    or eax, 1 << 31        ; CR0.PG
    mov cr0, eax
    ; Now in compatibility mode — far jump to 64-bit code segment
    jmp 0x08:long_mode_entry
```

### Solution 2 — Disable long mode correctly

```assembly
disable_long_mode:
    ; Step 1: Jump to 32-bit code segment
    jmp 0x18:compat_mode

compat_mode:
    ; Step 2: Clear LME
    mov ecx, 0xC0000080
    rdmsr
    and eax, ~(1 << 8)
    wrmsr

    ; Step 3: Disable paging, then PAE
    mov eax, cr0
    and eax, ~(1 << 31)
    mov cr0, eax
    mov eax, cr4
    and eax, ~(1 << 5)
    mov cr4, eax
    ret
```

### Solution 3 — Verify PML4 before enabling

```assembly
check_pml4:
    mov eax, [pml4_table]
    test eax, 1            ; check present bit
    jz .invalid
    mov eax, [pml4_table + 4]
    test eax, 1            ; check second entry
    jz .invalid
    ret
.invalid:
    ; halt with error
    cli
    hlt
```

## Examples

A bootloader enables long mode by setting EFER.LME but forgets PAE. The CPU generates a page fault during the mode switch, which cannot be handled (no IDT set up), causing a triple fault and reboot. Adding the PAE step fixes the boot sequence.

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault-error) — invalid PML4 entries
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — ring transitions
- [A20 Gate](/languages/assembly/asm-a20-gate-error) — address line issues
