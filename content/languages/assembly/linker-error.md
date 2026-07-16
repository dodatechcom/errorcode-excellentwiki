---
title: "Linker error: undefined reference"
description: "A linker error occurs when the linker cannot resolve a reference to a symbol defined in another object file or library."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["linker", "undefined-reference", "link-time", "library"]
weight: 5
---

## What This Error Means

A linker error with "undefined reference" occurs when the linker processes object files and cannot find the definition for a symbol that code references. Unlike an undefined symbol error detected by the assembler, this error occurs during the linking stage when combining multiple object files or libraries.

## Common Causes

- Forgetting to link the object file that contains the symbol definition
- Omitting the `-l` flag for required libraries (e.g., `-lc`, `-lm`)
- Link order matters: libraries must appear after the object files that reference them
- Symbol name mismatch due to missing `extern` declaration or name mangling

## How to Fix

```asm
; WRONG: Missing extern declaration
section .text
    call printf           ; linker error - printf not declared

; CORRECT: Declare external symbols
extern printf

section .text
    call printf           ; linker resolves printf from libc
```

```bash
# WRONG: Linking without the required library
nasm -f elf64 main.asm -o main.o
ld main.o -o main        # error: undefined reference to 'printf'

# CORRECT: Include the C library after object files
nasm -f elf64 main.asm -o main.o
ld main.o -lc -o main    # link libc

# Or better, use gcc which handles startup code:
gcc main.o -o main
```

```asm
; WRONG: Symbol defined but not exported
section .text
helper_func:
    mov rax, 42
    ret

; CORRECT: Export the symbol for other object files
section .text
    global helper_func
helper_func:
    mov rax, 42
    ret
```

## Examples

```asm
; main.asm
extern printf
extern exit

section .data
    msg db "Hello, world!", 10, 0

section .text
    global _start

_start:
    lea rdi, [msg]
    xor rax, rax
    call printf          ; if libc is not linked, this causes:
                         ; undefined reference to `printf`

    xor rdi, rdi
    call exit            ; undefined reference to `exit`
```

Build command that produces the error:
```bash
nasm -f elf64 main.asm -o main.o
ld main.o -o main       # fails: undefined reference to `printf`, `exit`
```

## Related Errors

- [Undefined symbol](/languages/assembly/undefined-symbol)
- [Invalid instruction](/languages/assembly/invalid-instruction)
