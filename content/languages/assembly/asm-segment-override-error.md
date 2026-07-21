---
title: "[Solution] Assembly Segment Override Error -- Incorrect FS/GS Usage"
description: "Fix assembly segment override errors when using FS or GS segment registers incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Segment Override Error

This error occurs when segment override prefixes (FS, GS) are used incorrectly for memory access.

## Common Causes

- Using FS/GS without understanding TLS layout
- Accessing wrong offset in TLS block
- Using segment overrides in 32-bit mode differently than 64-bit
- Not initializing segment registers properly

## How to Fix

### Understand segment register usage

```asm
; In 64-bit mode:
; FS = Thread Local Storage (Linux)
; GS = Per-CPU data (Linux)

; WRONG: using DS: for TLS access
mov rax, [my_tls_var]  ; accesses DS, not TLS

; CORRECT: use FS: for TLS
mov rax, [fs:my_tls_offset]
```

### Check segment base

```asm
; Get TLS base address
rdfsbase rax  ; if FSGSBASE support
; or
mov rax, [fs:0]  ; first qword is pointer to TLS block
```

## Examples

```asm
; Access thread-specific data
get_pid:
    mov rax, [fs:gs:@tpoff]  ; access thread ID
    ret
```
