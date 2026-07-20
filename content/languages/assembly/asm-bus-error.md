---
title: "[Solution] Assembly Bus Error — How to Fix"
description: "Fix bus errors in assembly caused by misaligned memory access or invalid physical address mapping."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1002
---

# Bus Error (SIGBUS)

A bus error occurs when the CPU attempts a memory access that cannot be completed — typically due to alignment violations on strict-alignment architectures or unmapped physical addresses via mmap.

## Common Causes

- Accessing a naturally-aligned type at an odd address on ARM/MIPS
- Memory-mapped I/O region not backed by a valid page
- File-backed mmap when the underlying file was truncated
- Accessing past the end of a shared memory object

## How to Fix

### Solution 1 — Ensure proper alignment

```assembly
; WRONG: loading a DWORD from an odd address on ARM
    ldr r0, [r1]         ; r1 = 0x1001 → SIGBUS

; CORRECT: use unaligned-safe load or align pointer
    bic r1, r1, #3       ; align to 4 bytes
    ldr r0, [r1]
```

### Solution 2 — Verify mmap regions

```assembly
mmap_check:
    mov eax, 9            ; sys_mmap
    mov rdi, 0            ; addr
    mov rsi, 4096         ; length
    mov rdx, 3            ; PROT_READ|PROT_WRITE
    mov r10, 0x22         ; MAP_PRIVATE|MAP_ANONYMOUS
    mov r8, -1
    syscall
    test rax, -1
    js .mmap_failed
```

### Solution 3 — Handle file-backed mmap truncation

```assembly
; Before accessing mmap'd file, verify size hasn't changed
    mov rax, 5            ; sys_fstat
    syscall
    cmp r12, rax          ; compare current size with mmap'd length
    jl .access_ok
    ; file was truncated — remap or bail out
```

## Examples

A network daemon reads a shared memory segment. The writer truncated the backing file, and the reader's mmap'd region now extends past the file end, causing SIGBUS on the next access.

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault-error) — virtual memory violations
- [Alignment Check](/languages/assembly/asm-alignment-check) — AC flag exceptions
- [Segmentation Fault](/languages/assembly/asm-segmentation-fault-v2) — invalid pointer access
