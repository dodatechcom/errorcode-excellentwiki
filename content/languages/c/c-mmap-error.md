---
title: "[Solution] C mmap() Error — How to Fix"
description: "Fix C mmap() errors including MAP_FAILED, invalid flags, and page alignment issues."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C mmap() Error — How to Fix

mmap() maps files or devices into memory. Common errors include not checking for MAP_FAILED, misaligned offset (must be page-aligned), invalid prot/flags combinations, and not calling munmap.

## Common Error Messages

- `mmap: Invalid argument (EINVAL)`
- `mmap returns MAP_FAILED`
- `mmap: Cannot allocate memory (ENOMEM)`
- `Bus error from misaligned mmap offset`

## How to Fix It

### Check MAP_FAILED return

```c
#include <sys/mman.h>
#include <stdio.h>
#include <unistd.h>

int main(void) {
    size_t len = 4096;
    void *p = mmap(NULL, len, PROT_READ | PROT_WRITE,
                   MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (p == MAP_FAILED) { perror("mmap"); return 1; }
    // use p ...
    munmap(p, len);
    return 0;
}
```

### Ensure page-aligned offset

```c
#include <sys/mman.h>
#include <unistd.h>

int main(void) {
    long page_size = sysconf(_SC_PAGESIZE);
    off_t offset = 0;  // must be multiple of page_size
    void *p = mmap(NULL, 4096, PROT_READ, MAP_PRIVATE, fd, offset);
    if (p == MAP_FAILED) { perror("mmap"); return 1; }
    munmap(p, 4096);
    return 0;
}
```

### Use mmap for file I/O

```c
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(void) {
    int fd = open("file.txt", O_RDONLY);
    struct stat st;
    fstat(fd, &st);
    void *p = mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (p != MAP_FAILED) {
        write(STDOUT_FILENO, p, st.st_size);
        munmap(p, st.st_size);
    }
    close(fd);
    return 0;
}
```

### Use mprotect to change permissions

```c
#include <sys/mman.h>
#include <stdio.h>

int main(void) {
    void *p = mmap(NULL, 4096, PROT_READ, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (p == MAP_FAILED) return 1;
    mprotect(p, 4096, PROT_READ | PROT_WRITE);
    int *arr = (int *)p;
    arr[0] = 42;
    printf("%d\n", arr[0]);
    munmap(p, 4096);
    return 0;
}
```

## Common Scenarios

### Scenario 1: mmap fails with EINVAL due to non-page-aligned offset

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Forgetting to munmap causing virtual address space leak

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using PROT_WRITE on read-only file

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check for MAP_FAILED before using mmap pointer
- **Tip 2:** Ensure offset is a multiple of sysconf(_SC_PAGESIZE)
- **Tip 3:** Always munmap when done and check return value
