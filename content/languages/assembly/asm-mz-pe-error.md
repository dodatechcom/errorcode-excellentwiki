---
title: "[Solution] Assembly MZ/PE Format Error — How to Fix"
description: "Fix MZ and PE executable format errors in assembly when building Windows executables."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1037
---

# MZ/PE Format Error

The MZ header (DOS stub) and PE (Portable Executable) header define a Windows executable's layout. Incorrect header fields, missing section alignment, or wrong entry point offset cause "not a valid Win32 application" errors.

## Common Causes

- PE signature not at the correct offset (0x3C in MZ header)
- NumberOfSections mismatch with actual section count
- EntryPoint RVA pointing outside the .text section
- Section alignment or file alignment set to 0

## How to Fix

### Solution 1 — Minimal MZ/PE header for NASM

```assembly
; MZ Header
bits 16
    db "MZ"                 ; signature
    times 58 db 0           ; reserved
    dd pe_header            ; offset to PE header

pe_header:
    dd 0x00004550           ; "PE\0\0"
    dw 0x014C               ; machine: i386
    dw 1                    ; NumberOfSections
    dd 0                    ; TimeDateStamp
    dd 0                    ; PointerToSymbolTable
    dd 0                    ; NumberOfSymbols
    dw optional_header_size ; SizeOfOptionalHeader
    dw 0x0102               ; Characteristics: executable, no relocations
```

### Solution 2 — 64-bit PE (PE32+)

```assembly
    dd 0x00004550           ; PE signature
    dw 0x8664               ; machine: AMD64
    dw 1                    ; NumberOfSections
    ; ... rest of optional header ...
```

### Solution 3 — Align sections correctly

```assembly
; File alignment: typically 0x200 (512 bytes)
; Section alignment: typically 0x1000 (4KB)
section_align equ 0x1000
file_align equ 0x200
```

### Solution 4 — Verify PE with dumpbin/objdump

```bash
# Check PE structure
objdump -x program.exe | head -30
# Verify entry point is within .text section
```

## Examples

A PE executable is assembled with the wrong entry point offset. Windows loads the image but jumps to the wrong address, causing an immediate crash. Setting the EntryPoint RVA to the correct .text offset fixes the boot.

## Related Errors

- [COM File Error](/languages/assembly/asm-com-file-error) — flat binary format
- [ELF Error](/languages/assembly/asm-elf-error) — Linux executable format
- [Relocation Error](/languages/assembly/asm-relocation-error) — address fixups
