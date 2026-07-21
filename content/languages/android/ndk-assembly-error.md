---
title: "NDK Assembly Error"
description: "Fix ARM assembly errors in Android NDK cross-compilation builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Native build fails with assembly errors when compiling for ARM targets

## Common Causes

- Assembly code uses x86 instructions on ARM target
- Inline assembly syntax not compatible with Clang
- Wrong assembly file extension (.s vs .S)
- Assembly comments using wrong syntax

## Fixes

- Use ARM-compatible assembly instructions
- Use Clang-compatible inline assembly syntax
- Use .S extension for files with preprocessor directives
- Check NDK assembler documentation for syntax

## Code Example

```kotlin
# Correct ARM64 inline assembly
__asm__ __volatile__(
    "mov x0, %0
"
    "ret
"
    : "=r"(result)
    : "r"(input)
    : "x0"
);

# In CMake, specify assembly language:
enable_language(ASM)
```

# Cross-compile for ARM
$ANDROID_HOME/ndk/VERSION/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android34-clang     -c test.S -o test.o
