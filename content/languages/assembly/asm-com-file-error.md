---
title: "[Solution] Assembly COM File Error — How to Fix"
description: "Fix COM file format errors in assembly when building flat binary executables for DOS."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1036
---

# COM File Error

A COM file is a flat binary with no headers — the CPU starts executing at offset 0x100. All code and data must fit in 64KB, and there are no relocations. Errors occur when the binary exceeds these limits or uses segment assumptions incorrectly.

## Common Causes

- Code + data exceeds 64KB (COM file limit)
- Using external symbols or relocations (not supported)
- ORG not set to 0x100 (COM entry point)
- Using instructions that require addresses > 0xFFFF

## How to Fix

### Solution 1 — Proper COM file structure

```assembly
org 0x100                 ; COM files start at CS:0100h

section .text
start:
    mov ah, 0x09          ; DOS print string
    mov dx, msg
    int 0x21
    mov ax, 0x4C00        ; DOS exit
    int 0x21

section .data
msg: db "Hello from COM$", 10, 0
```

### Solution 2 — Keep within 64KB

```bash
# Check binary size after assembly
nasm -f bin -o program.com program.asm
ls -la program.com
# Must be ≤ 65535 bytes
```

### Solution 3 — Use tiny model for NASM flat binary

```assembly
; All sections in one flat binary
bits 16
org 0x100

start:
    call print_string
    int 0x20              ; DOS terminate

print_string:
    ; use int 21h ah=09h
    ret

section .data
msg: db "COM file$", 0
```

### Solution 4 — Convert COM to EXE when size exceeds 64KB

```bash
# Use a linker to create MZ EXE instead
nasm -f obj -o file.obj file.asm
link /subsystem:dos file.obj
```

## Examples

A COM file grows past 64KB as more features are added. The DOS loader wraps the address, causing code to overlap with data. The fix is to convert to MZ EXE format which supports multiple segments and relocations.

## Related Errors

- [MZ/PE Error](/languages/assembly/asm-mz-pe-error) — MZ/PE executable format
- [Segment Error](/languages/assembly/asm-segment-error) — segment register issues
- [Relocation Error](/languages/assembly/asm-relocation-error) — address fixups
