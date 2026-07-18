---
title: "[Solution] Assembly: page fault in nonpaged area"
description: "Fix Assembly page faults by validating memory addresses and checking mmap results properly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A page fault in nonpaged area is a memory management error that occurs when the CPU tries to access a memory page that is not present in physical memory and the operating system cannot page it in. In user-space Assembly programs on Linux, a page fault typically manifests as SIGSEGV with a fault address that points to a valid virtual address range but one that has not been backed by physical pages. The kernel cannot satisfy the page fault because the page was never mapped, the mapping was removed, or the underlying storage (swap) is unavailable.

## Why It Happens

Page faults in Assembly programs occur when accessing virtual addresses that are not mapped into the process address space. Using a pointer that was returned by `mmap` with `MAP_FIXED` that overlaid existing mappings can cause subsequent accesses to fail. Accessing memory beyond the end of an `mmap`-ed region, past the allocated length, triggers a page fault. After `munmap` is called, any access to the freed region faults. Stack overflow beyond the guard page causes a page fault because the guard page is intentionally unmapped. Memory-mapped files that have been truncated or deleted may cause page faults when accessed. Accessing the zero page (address 0x0 through 0xFFF) always faults because it is intentionally unmapped by the kernel.

## How to Fix It

**Validate mmap return values:**

```asm
section .text
extern mmap
extern munmap

map_file:
    push rbp
    mov rbp, rsp

    ; mmap(addr, length, prot, flags, fd, offset)
    mov rdi, 0              ; addr = NULL (let kernel choose)
    mov rsi, 4096           ; length = one page
    mov rdx, 3              ; prot = PROT_READ | PROT_WRITE
    mov r10, 0x22           ; flags = MAP_PRIVATE | MAP_ANONYMOUS
    mov r8, -1              ; fd = -1 (anonymous)
    mov r9, 0               ; offset = 0
    mov rax, 9              ; SYS_mmap
    syscall

    ; Check for mmap failure
    cmp rax, -1
    jbe .mmap_failed        ; If return is negative (error)
    cmp rax, 0xfffffffffffff000
    ja .mmap_failed

    ; RAX contains valid pointer
    ; Safe to use: mov byte [rax], 0x42

    ; Store pointer for later munmap
    mov [mapped_ptr], rax
    ret

.mmap_failed:
    mov rax, 0              ; Return NULL
    ret
```

**Handle stack growth properly:**

```asm
; Ensure stack has enough space
; Linux default stack is 8MB with guard page
my_deep_function:
    push rbp
    mov rbp, rsp

    ; Check if we need more stack space
    mov rax, rsp
    sub rax, 65536          ; Need 64KB
    cmp rax, [stack_limit]
    jb .stack_overflow

    sub rsp, 65536          ; Allocate on stack
    ; Use stack space...
    add rsp, 65536
    leave
    ret

.stack_overflow:
    mov rax, -1
    leave
    ret


## Common Mistakes

- Not checking mmap return values before using the returned pointer
- Accessing memory after munmap has been called
- Exceeding the length specified in the mmap call
- Not accounting for page alignment when calculating mmap sizes
- Assuming memory is always available without checking system limits

## Related Pages

- [Segmentation fault null pointer in Assembly](/languages/assembly/assembly-segfault-null-new)
- [mmap failed in Assembly](/languages/assembly/assembly-mmap-error-new)
- [General protection fault in Assembly](/languages/assembly/assembly-alignment-fault-new)
- [Stack smashing in Assembly](/languages/assembly/assembly-stack-smashing-new)
