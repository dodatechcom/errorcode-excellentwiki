---
title: "[Solution] Assembly MODRM Byte Error — How to Fix"
description: "Fix ModR/M byte encoding errors in assembly when the addressing mode field is incorrectly calculated."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1031
---

# ModR/M Byte Error

The ModR/M byte encodes the addressing mode and register operands for most x86 instructions. It has three fields: mod (2 bits), reg/opcode (3 bits), and r/m (3 bits). Incorrect encoding causes the CPU to interpret operands as the wrong registers or addresses.

## Common Causes

- Using mod=00 with r/m=101 (RIP-relative in 64-bit, disp32 only)
- Not specifying SIB byte when R/M=100 (ESP/RSP as base)
- Off-by-one in displacement size selection (mod=01 for byte, mod=10 for dword)
- Mixing up reg and r/m fields in two-operand instructions

## How to Fix

### Solution 1 — Understand ModR/M encoding

```assembly
; ModR/M byte: mod(2) | reg(3) | r/m(3)
; Example: MOV EAX, [ECX+8]
; mod=01 (disp8), reg=000 (EAX), r/m=001 (ECX)
; Encoding: 01 000 001 = 0x41
```

### Solution 2 — Use NASM syntax (auto-encoded)

```assembly
; NASM handles ModR/M automatically
    mov eax, [rbx]          ; mod=00, r/m=011
    mov eax, [rbx+rcx*4]   ; SIB byte needed
    mov eax, [rbx+8]        ; mod=01, disp8
    mov eax, [rbx+256]      ; mod=10, disp32
```

### Solution 3 — Manually encode when writing assemblers

```assembly
; Manual encoding example:
; MOV EAX, [EBP+disp32] → mod=10, reg=000, r/m=101
; byte = 10_000_101 = 0x85
; followed by 32-bit displacement
```

### Solution 4 — Debug ModR/M with disassembler

```bash
# Assemble and disassemble to verify encoding
echo "MOV EAX, [RBX+RCX*4+8]" | nasm -f bin -o /dev/stdout - | ndisasm -b 64 -o 0 -
```

## Examples

An assembler generates a ModR/M byte with mod=00 and r/m=101, which in 64-bit mode means RIP-relative addressing. The intended absolute address is now relative to the next instruction, causing a wrong memory access. Using mod=10 with a 32-bit displacement fixes the encoding.

## Related Errors

- [REX Prefix](/languages/assembly/asm-rex-prefix-error) — register extension
- [SIB Byte](/languages/assembly/asm-sib-byte-error) — complex addressing
- [RIP Relative](/languages/assembly/asm-rip-relative-error) — RIP-relative mode
