---
title: "[Solution] C mprotect() Error — How to Fix"
description: "Fix C mprotect() errors for changing memory protection on mapped pages."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C mprotect() Error — How to Fix

mprotect() changes memory protection on a page range. Common errors include non-page-aligned addresses, invalid protection flags, and trying to make already-executable memory writable (W^X violations).

## Common Error Messages

- `mprotect: Invalid argument — non-page-aligned address`
- `mprotect: Cannot allocate memory`
- `mprotect fails on executable memory (W^X)`
- `Segmentation fault from wrong protection`

## How to Fix It

### Align address to page boundary

```c
#include <sys/mman.h>
#include <unistd.h>
#include <stdio.h>

int main(void) {
    long page = sysconf(_SC_PAGESIZE);
    size_t len = page * 2;
    void *p = mmap(NULL, len, PROT_READ | PROT_WRITE,
                   MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (p == MAP_FAILED) return 1;
    if (mprotect(p, len, PROT_READ) == -1) {
        perror("mprotect");
    }
    munmap(p, len);
    return 0;
}
```

### Use mprotect for JIT compilation

```c
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>

typedef int (*func_t)(void);

int main(void) {
    long page = sysconf(_SC_PAGESIZE);
    unsigned char code[] = { 0xb8, 0x2a, 0x00, 0x00, 0x00, 0xc3 };
    void *p = mmap(NULL, page, PROT_READ | PROT_WRITE,
                   MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    memcpy(p, code, sizeof(code));
    mprotect(p, page, PROT_READ | PROT_EXEC);
    func_t fn = (func_t)p;
    printf("Result: %d\n", fn());
    munmap(p, page);
    return 0;
}
```

### Guard page for stack overflow detection

```c
#include <sys/mman.h>
#include <unistd.h>

int main(void) {
    long page = sysconf(_SC_PAGESIZE);
    void *p = mmap(NULL, page, PROT_NONE,
                   MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (p != MAP_FAILED) {
        printf("Guard page at %p\n", p);
        munmap(p, page);
    }
    return 0;
}
```

### Check mprotect return value

```c
#include <sys/mman.h>
#include <stdio.h>

int main(void) {
    void *p = mmap(NULL, 4096, PROT_READ | PROT_WRITE,
                   MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (p == MAP_FAILED) return 1;
    if (mprotect(p, 4096, PROT_READ) == -1) {
        perror("mprotect");
        munmap(p, 4096);
        return 1;
    }
    munmap(p, 4096);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Using non-page-aligned address with mprotect

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Trying to make memory writable and executable simultaneously

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Forgetting to handle mprotect failure in JIT scenarios

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always page-align the start address for mprotect
- **Tip 2:** Check mprotect return value for errors
- **Tip 3:** Understand W^X security policy on your platform
