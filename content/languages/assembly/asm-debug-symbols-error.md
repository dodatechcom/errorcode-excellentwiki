---
title: "[Solution] Assembly Debug Symbols Error -- Incorrect DWARF Info"
description: "Fix assembly debug symbol errors when DWARF debugging information is incorrect."
languages: ["assembly"]
error-types: ["debug-time"]
severities: ["warning"]
---

# Assembly Debug Symbols Error

This error occurs when DWARF debugging information in assembly is malformed, causing debuggers to display incorrect information.

## Common Causes

- Missing .debug_line sections
- Incorrect line number directives
- DWARF CFI (Call Frame Information) not matching code
- Source file references pointing to wrong files

## How to Fix

### Add debug directives

```asm
; Add line number information
section .text
global my_func
my_func:
    .LFB0:             ; Function begin label
    push rbp
    .LCFI0:
    mov rbp, rsp
    ; ... code ...
    .LFE0:             ; Function end label

section .debug_info
    ; DWARF debug info here
```

### Generate debug info with NASM

```bash
nasm -f elf64 -g -F dwarf myfile.asm -o myfile.o
ld -o myfile myfile.o
gdb ./myfile
```

## Examples

```asm
; Minimal debug-friendly code
section .text
global _start
_start:
    .Lline1:
    mov rax, 60
    .Lline2:
    xor edi, edi
    .Lline3:
    syscall
```
