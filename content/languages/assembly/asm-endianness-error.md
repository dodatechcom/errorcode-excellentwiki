---
title: "[Solution] Assembly Endianness Error -- Byte Order Mismatch"
description: "Fix assembly endianness errors when data is read in wrong byte order."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Endianness Error

This error occurs when data is read or written in the wrong byte order between little-endian and big-endian formats.

## Common Causes

- Reading network data (big-endian) as little-endian
- Incorrect byte swap for cross-platform data
- Mixed endianness in structure fields
- Not converting between host and network byte order

## How to Fix

### Swap bytes for correct endianness

```asm
; WRONG: network byte order not converted
mov eax, [network_data]  ; reads as little-endian

; CORRECT: swap bytes
bswap eax  ; convert big-endian to little-endian
```

### Use BSWAP for 32-bit values

```asm
; Network to host byte order
ntohl:
    bswap eax
    ret

htonl:
    bswap eax
    ret
```

## Examples

```asm
; Read big-endian 16-bit value
read_be16:
    movzx eax, word [rdi]
    xchg al, ah  ; swap bytes
    ret
```
