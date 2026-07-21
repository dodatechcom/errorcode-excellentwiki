---
title: "[Solution] Assembly WRMSR Error -- Model-Specific Register Access"
description: "Fix assembly WRMSR errors when writing to Model-Specific Registers incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly WRMSR Error

This error occurs when WRMSR is used with incorrect MSR addresses or from user mode (Ring 3).

## Common Causes

- WRMSR requires Ring 0 privilege level
- Invalid MSR address for the current CPU
- Not reading MSR first with RDMSR
- Clobbering ECX (MSR address) without preserving

## How to Fix

### Access MSRs from kernel mode only

```asm
; WRONG: WRMSR from user mode (general protection fault)
mov ecx, 0x1A0    ; IA32_MISC_ENABLE
rdmsr
; modify edx:eax
wrmsr             ; fault if Ring 3

; CORRECT: only from kernel
; Use RDMSR to read first
mov ecx, 0x1A0
rdmsr             ; result in EDX:EAX
; modify value
wrmsr             ; OK from Ring 0
```

### Validate MSR address

```asm
; Check if MSR is valid for this CPU
check_msr:
    mov ecx, 0x1A0
    rdmsr
    ; if no #GP, MSR is valid
    ret
```

## Examples

```asm
; Read IA32_TSC (time stamp counter)
read_tsc:
    rdtsc           ; or use RDMSR with MSR 0x10
    ret
```
