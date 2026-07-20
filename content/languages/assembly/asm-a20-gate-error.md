---
title: "[Solution] Assembly A20 Gate Error — How to Fix"
description: "Fix A20 gate errors in assembly when the 20th address line is not enabled, causing memory address wrapping."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1021
---

# A20 Gate Error

The A20 gate controls whether the 20th address line (bit 20) of the memory address bus is active. When disabled, addresses above 1MB wrap around to zero. Bootloaders must enable A20 before accessing memory above 1MB.

## Common Causes

- Bootloader accessing memory >1MB without enabling A20 first
- BIOS did not enable A20 automatically (older BIOSes)
- Fast A20 gate (port 0x92) not supported on all hardware
- Keyboard controller A20 method is slow but universally supported

## How to Fix

### Solution 1 — Enable A20 via port 0x92 (fast A20)

```assembly
enable_a20_fast:
    in al, 0x92
    or al, 2              ; set bit 1 (A20 enable)
    out 0x92, al
    ret
```

### Solution 2 — Enable A20 via keyboard controller

```assembly
enable_a20_kbd:
    ; Wait for keyboard controller to be ready
    call .wait_input
    mov al, 0xAD          ; disable keyboard
    out 0x64, al

    call .wait_input
    mov al, 0xD0          ; read output port
    out 0x64, al

    call .wait_output
    in al, 0x60
    or al, 2              ; set A20 bit
    push rax

    call .wait_input
    mov al, 0xD1          ; write output port
    out 0x64, al

    call .wait_input
    pop rax
    out 0x60, al

    call .wait_input
    mov al, 0xAE          ; enable keyboard
    out 0x64, al
    ret

.wait_input:
    in al, 0x64
    test al, 2
    jnz .wait_input
    ret

.wait_output:
    in al, 0x64
    test al, 1
    jz .wait_output
    ret
```

### Solution 3 — Verify A20 is enabled

```assembly
check_a20:
    mov al, [0x7DFE]      ; boot sector signature location
    mov bl, [0x107DFE]    ; same physical address if A20 disabled
    cmp al, bl
    je .a20_disabled
    ret
.a20_disabled:
    ; A20 is off — enable it
    call enable_a20_fast
    ret
```

### Solution 4 — Use BIOS interrupt to query A20

```assembly
check_a20_bios:
    mov ax, 0x2403        ; QUERY A20 GATE STATUS
    int 0x15
    jc .not_supported
    test ah, ah
    jnz .a20_enabled
    ; enable via int 0x15, ax=0x2401
    mov ax, 0x2401
    int 0x15
.a20_enabled:
.not_supported:
    ret
```

## Examples

A bootloader loads a kernel to address 0x100000 (1MB). Without enabling A20, writes wrap to 0x00000, corrupting the IVT. The bootloader must enable A20 before copying the kernel image.

## Related Errors

- [Long Mode Switch](/languages/assembly/asm-long-mode-switch-error) — mode transitions
- [Page Fault](/languages/assembly/asm-page-fault-error) — memory mapping
- [General Protection Fault](/languages/assembly/asm-general-protection-fault) — protection
