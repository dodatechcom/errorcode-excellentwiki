---
title: "[Solution] Assembly ELF Header Error -- Invalid Executable Format"
description: "Fix assembly ELF header errors when creating invalid ELF executables."
languages: ["assembly"]
error-types: ["link-time"]
severities: ["error"]
---

# Assembly ELF Header Error

This error occurs when ELF headers are malformed, causing the kernel to reject the executable.

## Common Causes

- Incorrect e_phoff or e_shoff values
- Wrong e_machine value for target architecture
- Missing or invalid program headers
- Incorrect e_entry point address

## How to Fix

### Create correct ELF header

```asm
; Minimal ELF64 header
section .header
elf_header:
    db 0x7f, "ELF"     ; magic number
    db 2                ; ELFCLASS64
    db 1                ; ELFDATA2LSB
    db 1                ; EV_CURRENT
    db 0, 0, 0, 0, 0, 0, 0, 0  ; padding
    dw 2                ; ET_EXEC
    dw 0x3e             ; EM_X86_64
    dd 1                ; EV_CURRENT
    dq _start           ; e_entry
    dq phdr - $$        ; e_phoff
    dq 0                ; e_shoff
    dd 0                ; e_flags
    dw ehdrsize         ; e_ehsize
    dw phdrsize         ; e_phentsize
    dw 1                ; e_phnum
```

### Verify with readelf

```bash
nasm -f elf64 myfile.asm -o myfile.o
ld myfile.o -o myfile
readelf -h myfile
```

## Examples

```asm
section .text
global _start
_start:
    mov rax, 60
    xor edi, edi
    syscall
```
