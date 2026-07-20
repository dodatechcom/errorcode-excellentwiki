---
title: "[Solution] C SIGBUS — Bus error handling"
description: "Fix and handle SIGBUS bus errors by checking memory alignment, mmap file boundaries, and sparse files. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 828
---

# C SIGBUS — Bus error handling

SIGBUS (Bus Error) is delivered when a program attempts to access memory in a way that the hardware cannot satisfy — typically due to alignment violations, accessing beyond the end of a memory-mapped file, or accessing nonexistent physical memory.

## Common Causes

```c
// Cause 1: Memory alignment violation
#include <stdint.h>
char buf[16];
int32_t *ip = (int32_t *)(buf + 1);  // not aligned to 4 bytes
int32_t val = *ip;  // SIGBUS on strict-alignment architectures (ARM, SPARC)
```

```c
// Cause 2: mmap beyond file end
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>

int fd = open("small.txt", O_RDONLY);  // file is 100 bytes
void *ptr = mmap(NULL, 4096, PROT_READ, MAP_SHARED, fd, 0);
int val = *(int *)ptr;  // SIGBUS if accessing beyond 100 bytes
```

```c
// Cause 3: Accessing hole in sparse file
// Sparse file: 0-1023 bytes exist, 1024-4095 is a hole, 4096-8191 exists
void *ptr = mmap(NULL, 8192, PROT_READ, MAP_SHARED, fd, 0);
// Accessing bytes 1024-4095 triggers SIGBUS (hole has no backing store)
```

```c
// Cause 4: Memory-mapped file truncated while mapped
void *ptr = mmap(NULL, size, PROT_READ, MAP_SHARED, fd, 0);
truncate("file.txt", 0);  // file shrunk
int val = *(int *)ptr;  // SIGBUS: mapped region no longer backed by file
```

```c
// Cause 5: Shared memory segment detached while in use
void *ptr = shmat(shmid, NULL, 0);
shmdt(ptr);  // detach
// ... later ...
int val = *(int *)ptr;  // possible SIGBUS
```

## How to Fix

### Fix 1: Ensure proper memory alignment

```c
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

// CORRECT: aligned allocation
int32_t *aligned = aligned_alloc(4, sizeof(int32_t));
if (aligned) {
    *aligned = 42;
    free(aligned);
}

// Or use posix_memalign
int32_t *ptr;
posix_memalign((void **)&ptr, sizeof(int32_t), sizeof(int32_t));
*ptr = 42;
free(ptr);
```

### Fix 2: Handle mmap beyond file boundaries

```c
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

void* safe_mmap_file(const char *filename, size_t *out_size) {
    int fd = open(filename, O_RDONLY);
    if (fd < 0) return NULL;

    struct stat st;
    if (fstat(fd, &st) < 0) { close(fd); return NULL; }

    size_t file_size = st.st_size;
    if (file_size == 0) { close(fd); return NULL; }

    // Map only the actual file size
    void *ptr = mmap(NULL, file_size, PROT_READ, MAP_PRIVATE, fd, 0);
    close(fd);

    if (ptr == MAP_FAILED) return NULL;

    // Ensure we don't access beyond file_size
    *out_size = file_size;
    return ptr;
}
```

### Fix 3: Use MAP_FIXED_NOREPLACE or check mapping validity

```c
#include <sys/mman.h>
#include <unistd.h>

// Safely map a file, checking page-by-page
void* safe_mmap_region(int fd, size_t offset, size_t length) {
    long page_size = sysconf(_SC_PAGESIZE);
    size_t aligned_length = ((length + page_size - 1) / page_size) * page_size;

    void *ptr = mmap(NULL, aligned_length, PROT_READ, MAP_PRIVATE, fd, offset);
    if (ptr == MAP_FAILED) return NULL;

    // Verify the mapping is valid by touching pages
    volatile char *p = (volatile char *)ptr;
    for (size_t i = 0; i < aligned_length; i += page_size) {
        (void)p[i];  // force page fault — will SIGBUS if invalid
    }

    return ptr;
}
```

### Fix 4: Install SIGBUS handler for graceful recovery

```c
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

static sigjmp_buf bus_jump_buffer;
static volatile sig_atomic_t bus_can_jump = 0;

void sigbus_handler(int sig, siginfo_t *info, void *context) {
    (void)sig;
    (void)info;
    (void)context;
    if (bus_can_jump) {
        bus_can_jump = 0;
        siglongjmp(bus_jump_buffer, 1);
    }
    _exit(1);
}

int safe_memory_access(void *ptr, size_t offset) {
    struct sigaction sa, old_sa;
    sa.sa_sigaction = sigbus_handler;
    sa.sa_flags = SA_SIGINFO;
    sigemptyset(&sa.sa_mask);
    sigaction(SIGBUS, &sa, &old_sa);

    bus_can_jump = 1;
    int result = 0;

    if (sigsetjmp(bus_jump_buffer, 1) == 0) {
        volatile char *p = (volatile char *)ptr;
        result = p[offset];  // may trigger SIGBUS
    } else {
        result = -1;  // recovered from SIGBUS
    }

    bus_can_jump = 0;
    sigaction(SIGBUS, &old_sa, NULL);
    return result;
}
```

### Fix 5: Use pread() instead of mmap for file access

```c
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int read_file_safely(const char *filename, size_t offset, void *buf, size_t buf_size) {
    int fd = open(filename, O_RDONLY);
    if (fd < 0) return -1;

    ssize_t n = pread(fd, buf, buf_size, offset);
    close(fd);

    return (n > 0) ? (int)n : -1;
}
```

## Examples

```c
// Real-world: safely reading a memory-mapped file with alignment
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdint.h>
#include <stdio.h>

typedef struct __attribute__((packed)) {
    uint32_t magic;
    uint32_t version;
    uint64_t data_offset;
    uint32_t data_size;
} FileHeader;

int read_header(const char *filename, FileHeader *header) {
    int fd = open(filename, O_RDONLY);
    if (fd < 0) return -1;

    struct stat st;
    fstat(fd, &st);

    if ((size_t)st.st_size < sizeof(FileHeader)) {
        close(fd);
        return -1;
    }

    void *map = mmap(NULL, sizeof(FileHeader), PROT_READ, MAP_PRIVATE, fd, 0);
    close(fd);

    if (map == MAP_FAILED) return -1;

    memcpy(header, map, sizeof(FileHeader));
    munmap(map, sizeof(FileHeader));

    return (header->magic == 0x4D59464C) ? 0 : -1;  // check magic number
}
```

```bash
# Debugging SIGBUS
# Check if the fault is alignment-related
gdb ./app -ex run -ex 'thread apply all bt' -ex quit

# Check file mapping
cat /proc/$(pidof app)/maps | grep "deleted\|txt\|mmap"

# Check for sparse files
file --sparse somefile.bin
```

## Related Errors

- [C SIGSEGV](/languages/c/sigsegv-handling) — Segmentation fault handling
- [C SIGILL](/languages/c/sigill-handling) — Illegal instruction
- [C USE_AFTER_FREE_C](/languages/c/use-after-free-c) — Use after free UB
