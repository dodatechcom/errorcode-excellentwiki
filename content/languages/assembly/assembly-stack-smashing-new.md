---
title: "[Solution] Assembly: stack smashing detected or stack buffer overflow"
description: "Fix Assembly stack smashing by preventing buffer overflows and implementing bounds-checked operations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["critical"]
weight: 5
---

## What This Error Means

Stack smashing detected is a security and stability error that occurs when a program writes beyond the bounds of a stack-allocated buffer, corrupting the return address or other critical stack data. The error is detected by stack canaries (guard values placed between local variables and the return address). When the canary value is modified, the runtime system terminates the program with the message `*** stack smashing detected ***`. This is a deliberate security measure to prevent exploitation of buffer overflow vulnerabilities.

## Why It Happens

Stack buffer overflows occur when a program writes more data to a stack buffer than it was allocated. The most common cause is using unsafe functions like `gets`, `strcpy`, or `sprintf` without bounds checking. In Assembly, manually pushing data beyond the allocated stack frame or using `rep movsb` with an incorrect count overflows the buffer. Function arguments or local arrays that are too small for the data they receive cause overflow. Off-by-one errors in loop bounds that write to stack arrays can corrupt the canary. Format string vulnerabilities in `printf`-style functions can also overwrite stack data. The overflow typically corrupts the saved return address, allowing an attacker to redirect execution, or causing a crash when the function tries to return.

## How to Fix It

**Allocate adequate stack space:**

```asm
; WRONG: insufficient stack space for local buffer
my_function:
    push rbp
    mov rbp, rsp
    sub rsp, 32         ; Only 32 bytes allocated
    mov byte [rbp-16], 'A'  ; Writing to local buffer
    ; But if we write 64 bytes, we overflow
    leave
    ret

; CORRECT: allocate enough space
my_function:
    push rbp
    mov rbp, rsp
    sub rsp, 128        ; Allocate enough for all locals
    mov byte [rbp-16], 'A'
    leave
    ret
```

**Use bounds-checked copies:**

```asm
; Safe copy with length limit
; RDI = destination, RSI = source, RDX = max length
safe_copy:
    push rbp
    mov rbp, rsp
    push rbx

    xor rcx, rcx        ; Counter = 0

.copy_loop:
    cmp rcx, rdx        ; Check against max length
    jae .done           ; If counter >= max, stop
    mov al, [rsi + rcx] ; Load source byte
    test al, al         ; Check for null terminator
    jz .done
    mov [rdi + rcx], al ; Store to destination
    inc rcx
    jmp .copy_loop

.done:
    mov byte [rdi + rcx], 0  ; Null-terminate
    pop rbx
    pop rbp
    ret
```

**Compile with stack protection enabled:**

```bash
# GCC/Clang: enable stack canaries
gcc -fstack-protector-strong -o program program.s

# Enable stack clash protection
gcc -fstack-clash-protection -o program program.s

# Disable for debugging only
gcc -fno-stack-protector -o program program.s


## Common Mistakes

- Not allocating enough stack space for all local variables and buffers
- Using `rep movsb` or `rep stosb` with incorrect length registers
- Not placing a canary between local buffers and the saved return address
- Forgetting that the stack grows downward on x86-64, so buffers at lower addresses overflow toward the canary
- Compiling without `-fstack-protector-strong` during development

## Related Pages

- [Invalid opcode in Assembly](/languages/assembly/assembly-invalid-opcode-new)
- [Segmentation fault null pointer in Assembly](/languages/assembly/assembly-segfault-null-new)
- [Page fault in Assembly](/languages/assembly/assembly-page-fault-new)
- [General protection fault in Assembly](/languages/assembly/assembly-alignment-fault-new)
