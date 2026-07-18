---
title: "[Solution] C fflush Error — How to Fix"
description: "Fix C fflush errors including flushing read streams, disk full conditions, and unflushed data loss prevention."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C fflush Error — How to Fix

The `fflush` function is defined only for output streams. Calling fflush on a read stream results in undefined behavior. Common mistakes include using fflush on stdin (only works on POSIX for discarding input), ignoring the return value, and not flushing before fclose when data integrity is critical.

## Common Error Messages

- `fflush: Invalid argument — flushing a read stream`
- `fflush fails on full disk — data lost`
- `fflush on stdin has no effect on some platforms`
- `Data loss from not flushing before fclose`

## How to Fix It

### Only call fflush on output streams

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("output.txt", "w");
    if (!fp) return 1;
    fprintf(fp, "Important data\n");
    if (fflush(fp) != 0)
        fprintf(stderr, "fflush failed\n");
    fclose(fp);
    return 0;
}
```

### Check fflush return value

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("output.txt", "w");
    if (!fp) return 1;
    for (int i = 0; i < 100; i++)
        fprintf(fp, "Line %d\n", i);
    if (fflush(fp) != 0)
        fprintf(stderr, "fflush failed — disk may be full\n");
    fclose(fp);
    return 0;
}
```

### Flush to synchronize after critical writes

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("log.txt", "a");
    if (!fp) return 1;
    fprintf(fp, "Entry 1\n");
    fflush(fp);
    fprintf(fp, "Entry 2\n");
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
    int val = 42;
    fwrite(&val, sizeof(val), 1, fp);
    fflush(fp);
    fsync(fileno(fp));
    fclose(fp);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Calling fflush on a read-only stream, causing undefined behavior

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Ignoring fflush return value and losing data silently when the disk is full

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Not flushing before fclose when writing critical data

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Only call fflush on output streams — never on read streams except stdin on POSIX
- **Tip 2:** Always check fflush return value to detect write errors
- **Tip 3:** Use fflush followed by fsync when data must survive a power failure
