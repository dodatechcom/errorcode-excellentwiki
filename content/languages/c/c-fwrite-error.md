---
title: "[Solution] C fwrite Error — How to Fix"
description: "Fix C fwrite errors including short writes, disk full conditions, and unflushed buffers for safe binary output."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C fwrite Error — How to Fix

The `fwrite` function may write fewer bytes than requested due to disk full, broken pipe, or I/O errors. Common mistakes include not checking the return value, not flushing after critical writes, and ignoring partial writes. Data loss can occur when fwrite fails silently.

## Common Error Messages

- `fwrite returns fewer items than expected`
- `fwrite error — disk full or I/O error`
- `Data loss from unchecked fwrite return value`
- `fwrite: short write detected`

## How to Fix It

### Check return value and retry on short writes

```c
#include <stdio.h>

int write_full(const void *buf, size_t size, size_t count, FILE *fp) {
    const char *p = (const char *)buf;
    size_t total = size * count;
    size_t written = 0;
    while (written < total) {
        size_t n = fwrite(p + written, 1, total - written, fp);
        if (n == 0) return -1;
        written += n;
    }
    if (fflush(fp) != 0) return -1;
    return 0;
}

int main(void) {
    int data[] = {1, 2, 3, 4, 5};
    FILE *fp = fopen("output.bin", "wb");
    if (!fp) return 1;
    if (write_full(data, sizeof(int), 5, fp) != 0)
        fprintf(stderr, "Write failed\n");
    fclose(fp);
    return 0;
}
```

### Flush the buffer after critical writes

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("log.bin", "ab");
    if (!fp) return 1;
    int val = 42;
    if (fwrite(&val, sizeof(val), 1, fp) != 1)
        fprintf(stderr, "fwrite failed\n");
    if (fflush(fp) != 0)
        fprintf(stderr, "fflush failed\n");
    fclose(fp);
    return 0;
}
```

### Handle disk full condition

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    FILE *fp = fopen("output.bin", "wb");
    if (!fp) return 1;
    char buf[4096];
    size_t n = fwrite(buf, 1, sizeof(buf), fp);
    if (n < sizeof(buf) && ferror(fp))
        fprintf(stderr, "Write error: %s\n", strerror(errno));
    fclose(fp);
    return 0;
}
```

### Use fsync for guaranteed disk persistence

```c
#include <stdio.h>
#include <unistd.h>

int main(void) {
    FILE *fp = fopen("critical.dat", "wb");
    if (!fp) return 1;
    int data = 42;
    fwrite(&data, sizeof(data), 1, fp);
    fflush(fp);
    fsync(fileno(fp));
    fclose(fp);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Not checking fwrite return value and silently losing data on partial writes

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Failing to flush before fclose when data must be persisted immediately

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Ignoring ferror after fwrite and continuing with corrupted state

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check fwrite return value and use a retry loop for short writes
- **Tip 2:** Call fflush followed by fsync for data that must survive a crash
- **Tip 3:** Use ferror(fp) after a zero fwrite return to distinguish error from EOF
