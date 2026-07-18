---
title: "[Solution] C fclose Error — How to Fix"
description: "Fix C fclose errors including double close, flushing before close, and file descriptor reuse issues."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C fclose Error — How to Fix

The `fclose` function can fail when flushing buffered data to disk encounters an error, or when the file handle is invalid. Common mistakes include double-closing a FILE pointer, not checking the return value, and using a FILE pointer after fclose has been called.

## Common Error Messages

- `fclose: Bad file descriptor — double close`
- `fclose error when flushing write buffer`
- `Use of FILE pointer after fclose — undefined behavior`
- `fclose fails on already-closed stream`

## How to Fix It

### Set FILE pointer to NULL after fclose

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("output.txt", "w");
    if (!fp) return 1;
    fprintf(fp, "Hello\n");
    if (fclose(fp) != 0)
        fprintf(stderr, "fclose failed\n");
    fp = NULL;
    return 0;
}
```

### Check fclose return value

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("output.txt", "w");
    if (!fp) return 1;
    fprintf(fp, "Data\n");
    if (fclose(fp) != 0) {
        fprintf(stderr, "Error closing file — data may be lost\n");
        return 1;
    }
    return 0;
}
```

### Avoid double-close with tracking

```c
#include <stdio.h>

typedef struct {
    FILE *fp;
    int is_open;
} FileHandle;

void safe_close(FileHandle *h) {
    if (h->fp && h->is_open) {
        fclose(h->fp);
        h->fp = NULL;
        h->is_open = 0;
    }
}
```

### Handle fclose error for write streams

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    FILE *fp = fopen("output.txt", "w");
    if (!fp) return 1;
    for (int i = 0; i < 1000; i++)
        fprintf(fp, "Line %d\n", i);
    if (fclose(fp) != 0) {
        fprintf(stderr, "fclose: %s\n", strerror(errno));
        return 1;
    }
    return 0;
}
```

## Common Scenarios

### Scenario 1: Double-closing a FILE pointer and corrupting a newly assigned file descriptor

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using a FILE pointer after fclose without setting it to NULL

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Ignoring fclose return value on write streams where flush errors can occur

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always set the FILE pointer to NULL after fclose to prevent use-after-close
- **Tip 2:** Check fclose return value on write streams to detect flush failures
- **Tip 3:** Avoid double-close by tracking whether the file handle is still open
