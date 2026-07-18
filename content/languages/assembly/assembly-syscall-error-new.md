---
title: "[Solution] Assembly: system call failed or errno"
description: "Fix Assembly system call failures by checking return values and interpreting errno codes correctly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A system call failure in Assembly occurs when a Linux or Windows system call returns an error indicator. On Linux x86-64, system calls return the result in RAX; negative values indicate errors (the negated errno value). On 32-bit Linux, the carry flag (CF) is set on error and the error code is in RAX. Common errors include EBADF (bad file descriptor), EACCES (permission denied), ENOENT (no such file or directory), and EINVAL (invalid argument). The program must check for these error conditions after every system call to avoid using invalid return values.

## Why It Happens

System call failures occur for many reasons. Invalid file descriptors passed to read/write/close cause EBADF. Passing NULL or invalid pointers to buffer arguments causes EFAULT. Incorrect syscall numbers (wrong value in RAX) trigger EINVAL. Permission denied (EACCES) occurs when attempting operations without proper user permissions. File not found (ENOENT) results from opening files at incorrect paths. Resource exhaustion (ENOMEM, EMFILE) happens when the system runs out of memory or file descriptors. Signal interruption (EINTR) occurs when a blocking syscall is interrupted by a signal. Broken pipe (EPIPE) happens when writing to a pipe whose read end has been closed.

## How to Fix It

**Always check syscall return values:**

```asm
section .text
global _start

_start:
    ; Write syscall
    mov rax, 1          ; SYS_write
    mov rdi, 1          ; stdout
    lea rsi, [msg]      ; buffer
    mov rdx, msg_len    ; count
    syscall

    ; Check for error (negative return)
    cmp rax, 0
    jl .write_error

    ; Success: RAX contains bytes written
    jmp .exit

.write_error:
    ; Negate RAX to get errno
    neg rax
    ; RAX now contains errno value
    ; Handle specific errors
    cmp rax, 14         ; EFAULT
    je .bad_address
    cmp rax, 22         ; EINVAL
    je .invalid_arg
    jmp .exit

.bad_address:
.invalid_arg:
.exit:
    mov rax, 60         ; SYS_exit
    xor rdi, rdi
    syscall
```

**Handle specific errno values:**

```asm
section .text
handle_error:
    ; Input: RAX = errno value
    cmp rax, 1          ; EPERM
    je .permission_denied
    cmp rax, 2          ; ENOENT
    je .file_not_found
    cmp rax, 5          ; EIO
    je .io_error
    cmp rax, 9          ; EBADF
    je .bad_fd
    cmp rax, 12         ; ENOMEM
    je .out_of_memory
    cmp rax, 13         ; EACCES
    je .access_denied
    cmp rax, 22         ; EINVAL
    je .invalid_argument
    cmp rax, 32         ; EPIPE
    je .broken_pipe

    ; Unknown error
    ret

.permission_denied:
.file_not_found:
.io_error:
.bad_fd:
.out_of_memory:
.access_denied:
.invalid_argument:
.broken_pipe:
    ret
```

**Check 32-bit syscall errors with CF flag:**

```asm
; 32-bit Linux syscall error checking
    mov eax, 4          ; SYS_write
    mov ebx, 1          ; stdout
    mov ecx, msg        ; buffer
    mov edx, msg_len    ; count
    int 0x80            ; Make syscall

    ; Check carry flag for error
    jc .syscall_error   ; CF set = error
    ; EAX contains result
    jmp .done

.syscall_error:
    ; EAX contains errno
    neg eax
    ; Handle error
.done:


## Common Mistakes

- Not checking syscall return values, assuming all calls succeed
- On 32-bit Linux, forgetting to check the carry flag for errors
- Not negating the return value to get the actual errno on x86-64
- Using the raw syscall return value as a pointer or size without error checking
- Assuming specific errno values are the same across different operating systems

## Related Pages

- [mmap failed in Assembly](/languages/assembly/assembly-mmap-error-new)
- [Segmentation fault null pointer in Assembly](/languages/assembly/assembly-segfault-null-new)
- [Invalid opcode in Assembly](/languages/assembly/assembly-invalid-opcode-new)
- [Page fault in Assembly](/languages/assembly/assembly-page-fault-new)
