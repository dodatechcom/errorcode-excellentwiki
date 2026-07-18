---
title: "[Solution] Assembly: segfault in data segment"
description: "Fix Assembly data segment segfaults by checking section placement and validating writable regions."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A segmentation fault in the data segment occurs when an Assembly program attempts to write to a memory region that is not writable, or reads from a data address that is not mapped. The data segment (.data, .bss) should be readable and writable, but errors in linker scripts, incorrect section declarations, or writing beyond segment boundaries can cause SIGSEGV. The fault address typically falls within the expected data segment range, but the access is denied due to memory protection violations.

## Why It Happens

Data segment segfaults occur when the program writes to a read-only section, such as attempting to modify code in the .text section or constants in .rodata. Incorrect linker scripts that do not properly define the data segment boundaries cause the kernel to not map the expected pages. Writing beyond the end of the .bss section, past the allocated program break, triggers a page fault that becomes SIGSEGV. Using absolute addresses that the linker did not place in valid memory regions causes faults. Forgetting to reserve space in .bss with `resb`/`resw`/`resq` and then writing to those addresses accesses unmapped memory. Modifying the GOT (Global Offset Table) or PLT entries incorrectly can corrupt pointer resolution and cause segfaults during data access.

## How to Fix It

**Place data in writable sections:**

```asm
; WRONG: trying to modify read-only data
section .rodata
    constant db 42
    ; mov byte [constant], 0  ; SIGSEGV!

; CORRECT: use writable section for mutable data
section .data
    mutable db 42

section .text
    mov byte [mutable], 0   ; Works fine
```

**Allocate sufficient .bss space:**

```asm
section .bss
    ; WRONG: not reserving enough space
    ; small_buffer resb 4
    ; mov qword [small_buffer], 0  ; Writes 8 bytes into 4-byte buffer

    ; CORRECT: reserve adequate space
    big_buffer resq 256     ; 256 * 8 = 2048 bytes
    temp_storage resb 4096

section .text
    mov qword [big_buffer], 0   ; Safe
    mov byte [temp_storage], 0  ; Safe
```

**Verify linker script defines sections:**

```ld
/* Default linker script (simplified) */
SECTIONS
{
    . = 0x400000;

    .text : { *(.text) }
    .rodata : { *(.rodata) }

    .data : {
        *(.data)
        *(.data.*)
    }

    .bss : {
        *(.bss)
        *(.bss.*)
        *(COMMON)
    }

    _end = .;
}
```

**Use proper section attributes:**

```asm
; NASM: section with flags
section .data write alloc

; GAS: .section with flags
.section .data, "aw"

; These ensure the section is both allocated and writable


## Common Mistakes

- Placing mutable data in .rodata or .text sections
- Not reserving enough space in .bss for all static variables
- Using hardcoded addresses instead of section-relative addressing
- Assuming the linker will automatically extend sections to page boundaries
- Not using `BITS 64` when assembling 64-bit code, causing address size issues

## Related Pages

- [Segmentation fault null pointer in Assembly](/languages/assembly/assembly-segfault-null-new)
- [Page fault in Assembly](/languages/assembly/assembly-page-fault-new)
- [mmap failed in Assembly](/languages/assembly/assembly-mmap-error-new)
- [General protection fault in Assembly](/languages/assembly/assembly-alignment-fault-new)
