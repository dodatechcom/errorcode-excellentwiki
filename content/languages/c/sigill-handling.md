---
title: "[Solution] C SIGILL — Illegal instruction handling"
description: "Fix and handle SIGILL illegal instruction errors by checking CPU features, compiler flags, and executable file integrity. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 829
---

# C SIGILL — Illegal instruction handling

SIGILL (Illegal Instruction) is delivered when the CPU encounters an instruction it cannot execute — due to missing CPU features (like SSE/AVX), executing data as code (buffer overflow), corrupt executable, or mismatched architecture.

## Common Causes

```c
// Cause 1: SSE/AVX instructions on CPU that doesn't support them
// Compiled with: gcc -msse4.2 -o app main.c
// Running on older CPU without SSE4.2 → SIGILL
#include <smmintrin.h>
int main(void) {
    __m128i a = _mm_set_epi32(1, 2, 3, 4);  // SIGILL on old CPUs
    return 0;
}
```

```c
// Cause 2: Executing data as code (buffer overflow / ROP)
// A buffer overflow overwrites the return address, jumping to data
char buf[16];
gets(buf);  // classic buffer overflow → return address corrupted → SIGILL
```

```c
// Cause 3: Corrupted executable or shared library
// Binary was partially overwritten on disk or in memory
```

```c
// Cause 4: Architecture mismatch
// Compiled for x86-64, running on ARM (or vice versa)
// ./app:  ELF 64-bit LSB executable, x86-64
// On ARM system → SIGILL
```

```c
// Cause 5: Inline assembly with invalid instruction
void *ptr;
asm volatile(
    "ud2"  // intentionally undefined instruction — triggers SIGILL
    :
    :
    : "memory"
);
```

## How to Fix

### Fix 1: Check CPU features at runtime before using SIMD

```c
#include <cpuid.h>
#include <stdio.h>

int has_sse42(void) {
    unsigned int eax, ebx, ecx, edx;
    if (__get_cpuid(1, &eax, &ebx, &ecx, &edx)) {
        return (ecx & (1 << 20)) != 0;  // SSE4.2 bit
    }
    return 0;
}

int has_avx2(void) {
    unsigned int eax, ebx, ecx, edx;
    if (__get_cpuid(7, &eax, &ebx, &ecx, &edx)) {
        return (ebx & (1 << 5)) != 0;  // AVX2 bit
    }
    return 0;
}

int main(void) {
    if (has_sse42()) {
        printf("SSE4.2 available\n");
        // use SSE4.2 code path
    } else {
        printf("SSE4.2 not available, using fallback\n");
        // use scalar fallback
    }
    return 0;
}
```

### Fix 2: Use CPU feature dispatch (function pointers)

```c
#include <cpuid.h>

// Function pointer type for implementations
typedef void (*process_fn)(float *data, size_t n);

// Scalar fallback
void process_scalar(float *data, size_t n) {
    for (size_t i = 0; i < n; i++) {
        data[i] = data[i] * 2.0f + 1.0f;
    }
}

// SSE implementation (conditional compilation)
#ifdef __SSE2__
#include <emmintrin.h>
void process_sse2(float *data, size_t n) {
    size_t i;
    __m128 two = _mm_set1_ps(2.0f);
    __m128 one = _mm_set1_ps(1.0f);
    for (i = 0; i + 4 <= n; i += 4) {
        __m128 v = _mm_loadu_ps(&data[i]);
        v = _mm_add_ps(_mm_mul_ps(v, two), one);
        _mm_storeu_ps(&data[i], v);
    }
    for (; i < n; i++) data[i] = data[i] * 2.0f + 1.0f;
}
#endif

process_fn get_process_fn(void) {
#ifdef __SSE2__
    unsigned int eax, ebx, ecx, edx;
    if (__get_cpuid(1, &eax, &ebx, &ecx, &edx) && (edx & (1 << 26))) {
        return process_sse2;
    }
#endif
    return process_scalar;
}
```

### Fix 3: Install SIGILL handler for diagnostics

```c
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

void sigill_handler(int sig, siginfo_t *info, void *context) {
    (void)sig;
    (void)context;
    fprintf(stderr, "SIGILL: illegal instruction at address %p\n", info->si_addr);
    fprintf(stderr, "This may indicate missing CPU features or a corrupted binary.\n");
    _exit(1);
}

int main(void) {
    struct sigaction sa;
    sa.sa_sigaction = sigill_handler;
    sa.sa_flags = SA_SIGINFO;
    sigemptyset(&sa.sa_mask);
    sigaction(SIGILL, &sa, NULL);

    // ... program code ...
    return 0;
}
```

### Fix 4: Compile with baseline instruction set

```bash
# Use generic x86-64 instructions only (no SSE beyond baseline)
gcc -march=x86-64 main.c -o app

# Instead of:
# gcc -march=native main.c -o app  (uses all CPU features of build machine)
```

### Fix 5: Verify executable integrity

```bash
# Check if binary is valid ELF
file ./app

# Check architecture
readelf -h ./app | grep Machine

# Verify checksum
md5sum ./app
sha256sum ./app

# Check if binary is corrupted
readelf -S ./app  # list sections — errors indicate corruption
```

## Examples

```c
// Real-world: runtime CPU feature detection and dispatch
#include <cpuid.h>
#include <stdio.h>

typedef struct {
    int sse2 : 1;
    int sse41 : 1;
    int avx : 1;
    int avx2 : 1;
    int avx512f : 1;
} CpuFeatures;

CpuFeatures detect_cpu_features(void) {
    CpuFeatures features = {0};
    unsigned int eax, ebx, ecx, edx;

    if (__get_cpuid(1, &eax, &ebx, &ecx, &edx)) {
        features.sse2  = (edx & (1 << 26)) != 0;
        features.sse41 = (ecx & (1 << 19)) != 0;
        features.avx   = (ecx & (1 << 28)) != 0;
    }

    if (__get_cpuid(7, &eax, &ebx, &ecx, &edx)) {
        features.avx2   = (ebx & (1 << 5)) != 0;
        features.avx512f = (ebx & (1 << 16)) != 0;
    }

    return features;
}

int main(void) {
    CpuFeatures cpu = detect_cpu_features();
    printf("SSE2:   %s\n", cpu.sse2   ? "yes" : "no");
    printf("SSE4.1: %s\n", cpu.sse41  ? "yes" : "no");
    printf("AVX:    %s\n", cpu.avx    ? "yes" : "no");
    printf("AVX2:   %s\n", cpu.avx2   ? "yes" : "no");
    printf("AVX-512:%s\n", cpu.avx512f? "yes" : "no");
    return 0;
}
```

```bash
# Diagnosing SIGILL
gdb ./app
(gdb) run
# Program received signal SIGILL, Illegal instruction.
(gdb) disassemble $pc-4, $pc+4
# Shows the instruction that caused the fault
```

## Related Errors

- [C SIGSEGV](/languages/c/sigsegv-handling) — Segmentation fault handling
- [C SIGBUS](/languages/c/sigbus-handling) — Bus error
- [C SIGFPE](/languages/c/sigfpe-handling) — Floating point exception
