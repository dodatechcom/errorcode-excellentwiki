---
title: "[Solution] Assembly Bit Test Error -- Incorrect BT/BTS/BTR Usage"
description: "Fix assembly bit test errors when using BT, BTS, or BTR instructions incorrectly."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly Bit Test Error

This error occurs when bit test instructions are used with incorrect bit indices or operand types.

## Common Causes

- Bit index exceeding register size
- Using BT with immediate bit index > 63
- Not checking CF after BTS/BTR
- Mixing 32-bit and 64-bit operands

## How to Fix

### Use correct bit test

```asm
; WRONG: bit index out of range
bt rax, 64  ; error: rax is 64-bit, valid indices 0-63

; CORRECT: valid bit index
bt rax, 42  ; test bit 42 of RAX
```

### Use BTS to test and set

```asm
; Test bit and set it atomically
bts [flag_var], 7  ; test bit 7, set if not set
jc .already_set   ; CF=1 if bit was already set
; bit was not set, now it is
```

## Examples

```asm
; Check if bit N is set
is_bit_set:
    bt rdi, rsi  ; test bit RSI of RDI
    setc al       ; AL = 1 if bit was set
    movzx eax, al
    ret
```
