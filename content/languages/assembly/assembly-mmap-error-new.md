---
title: "[Solution] Assembly: mmap failed or cannot map memory"
description: "Fix Assembly mmap failures by validating parameters and checking for MAP_FAILED return values."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An mmap failure in Assembly occurs when the `mmap` system call cannot create the requested memory mapping. On Linux x86-64, `mmap` returns MAP_FAILED (0xffffffffffffffff) on error, with the actual error code available via errno. Common failure reasons include ENOMEM (out of memory), EINVAL (invalid arguments), EACCES (permission conflict), and ENOMEM (exceeding the maximum number of mappings). The program must check for MAP_FAILED after every mmap call before using the returned pointer, as MAP_FAILED is not a valid address and dereferencing it causes a segmentation fault.

## Why It Happens

mmap failures occur for several reasons. Requesting a length of zero is invalid and causes EINVAL. The flags parameter may contain conflicting options, such as MAP_SHARED combined with MAP_ANONYMOUS without a file descriptor. The protection flags (PROT_NONE, PROT_READ, PROT_WRITE, PROT_EXEC) may be incompatible with the file's permissions or the kernel's security policy. Address space exhaustion, where the process has too many virtual memory areas (VMAs), causes mmap to fail with ENOMEM. The offset for file-backed mappings must be page-aligned; non-aligned offsets cause EINVAL. MAP_FIXED with an address that conflicts with existing mappings may fail. Overcommit settings may prevent large anonymous mappings. ASLR (Address Space Layout Randomization) may prevent MAP_FIXED from finding a suitable location.

## How to Fix It

**Always check mmap return value:**

```asm
section .text
extern mmap
extern munmap

safe_mmap:
    push rbp
    mov rbp, rsp
    sub rsp, 32

    ; mmap(addr, length, prot, flags, fd, offset)
    mov rdi, 0              ; Let kernel choose address
    mov rsi, [rsp+16]       ; length from stack
    mov rdx, 3              ; PROT_READ | PROT_WRITE
    mov r10, 0x22           ; MAP_PRIVATE | MAP_ANONYMOUS
    mov r8, -1              ; fd = -1 for anonymous
    mov r9, 0               ; offset = 0
    mov rax, 9              ; SYS_mmap
    syscall

    ; Check for MAP_FAILED
    cmp rax, -1
    je .mmap_failed

    ; Additional check for high address on error
    cmp rax, 0xfffffffffffff000
    ja .mmap_failed

    ; RAX = valid mapped address
    leave
    ret

.mmap_failed:
    ; Get actual error from errno
    ; On Linux, errno is in thread-local storage
    ; For simplicity, set return to 0
    xor rax, rax
    leave
    ret
```


```asm
cleanup_mmap:
    push rbp
    mov rbp, rsp

    mov rdi, [mapped_addr]   ; Address from mmap
    mov rsi, [mapped_size]   ; Same length as mmap
    mov rax, 11             ; SYS_munmap
    syscall

    cmp rax, 0
    jne .unmap_failed
    leave
    ret

.unmap_failed:
    mov rax, -1
    leave
    ret

section .bss
    mapped_addr resq 1
    mapped_size resq 1


## Common Mistakes

- Not checking if mmap returns MAP_FAILED before using the pointer
- Using MAP_FIXED without first unmapping the existing mapping
- Passing a non-page-aligned offset for file-backed mappings
- Requesting more memory than the system can provide without checking ulimits
- Forgetting to munmap memory when it is no longer needed, causing virtual address space exhaustion

## Related Pages

- [Page fault in Assembly](/languages/assembly/assembly-page-fault-new)
- [Segmentation fault null pointer in Assembly](/languages/assembly/assembly-segfault-null-new)
