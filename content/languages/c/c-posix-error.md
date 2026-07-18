---
title: "[Solution] C POSIX Error — How to Fix"
description: "Fix C POSIX API errors including errno handling, feature test macros, and portability."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C POSIX Error — How to Fix

POSIX errors include not checking return values, wrong feature test macros, and not handling EINTR.

## Common Error Messages

- `Operation not permitted (EPERM)`
- `No such file or directory (ENOENT)`
- `Interrupted system call (EINTR)`
- `Permission denied (EACCES)`

## How to Fix It

### Check return and errno

#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    FILE *f = fopen("/etc/shadow", "r");
    if (!f) {
        fprintf(stderr, "fopen: %s (errno=%d)\n", strerror(errno), errno);
        return 1;
    }
    fclose(f);
    return 0;
}

### Handle EINTR

#include <unistd.h>
#include <errno.h>

ssize_t read_safe(int fd, void *buf, size_t len) {
    ssize_t n;
    do {
        n = read(fd, buf, len);
    } while (n == -1 && errno == EINTR);
    return n;
}

### Use feature test macros

#define _POSIX_C_SOURCE 200809L
#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>

int main(void) {
    char *s = strdup("hello");
    printf("%s\n", s);
    free(s);
    return 0;
}

### Check uid/gid

#include <unistd.h>
#include <stdio.h>

int main(void) {
    printf("uid=%d gid=%d\n", getuid(), getgid());
    return 0;
}

## Common Scenarios

### Scenario 1: EPERM from trying privileged operation

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: EINTR from signal interrupting syscall

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: Compilation fails due to missing feature test macro

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Always check return values and errno
- **Tip 2:** Retry syscalls interrupted by EINTR
- **Tip 3:** Define _POSIX_C_SOURCE or _GNU_SOURCE as needed
