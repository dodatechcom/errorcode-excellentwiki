---
title: "[Solution] C errno ELOOP — Too many levels of symbolic links Fix"
description: "Fix C ELOOP (Too many levels of symbolic links) by resolving circular symlinks and limiting symlink depth."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eloop", "too-many-symlinks", "symbolic-links", "circular-link"]
weight: 5
---

# [Solution] C errno ELOOP — Too many levels of symbolic links Fix

When the kernel encounters too many symbolic links while resolving a path, the system call fails and sets `errno` to `ELOOP`. This typically indicates a circular symbolic link chain where a symlink points (directly or indirectly) back to itself.

## Common Causes

- A circular chain of symbolic links exists (e.g., `a -> b -> c -> a`).
- Too many nested symbolic links exceed `MAXSYMLINKS` (typically 40 on Linux).
- A symlink points to another symlink, creating a deep chain.
- A symlink in the current directory points back to itself.

## How to Fix

Use `readlink()` or `realpath()` to detect circular links. Check for circular references before creating symlinks.

```c
#include <limits.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    char resolved[PATH_MAX];
    if (realpath("/path/to/symlink", resolved) == NULL) {
        if (errno == ELOOP) {
            fprintf(stderr, "Circular symbolic link detected\n");
        } else {
            fprintf(stderr, "realpath failed: %s\n", strerror(errno));
        }
        return 1;
    }
    printf("Resolved path: %s\n", resolved);
    return 0;
}
```

## Examples

A circular symlink chain:

```bash
# Create circular links
ln -s /tmp/b /tmp/a
ln -s /tmp/a /tmp/b
cat /tmp/a  # ELOOP
```

Detecting circular links programmatically:

```c
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <limits.h>

int main(void) {
    char target[PATH_MAX];
    ssize_t len = readlink("/tmp/a", target, sizeof(target) - 1);
    if (len == -1) {
        perror("readlink");
        return 1;
    }
    target[len] = '\0';
    printf("Symlink points to: %s\n", target);

    int fd = open("/tmp/a", O_RDONLY);
    if (fd == -1 && errno == ELOOP) {
        fprintf(stderr, "Circular symlink detected (errno %d)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-40 ELOOP](/languages/c/errno-eloop/) — too many levels of symbolic links (numeric).
- [errno-2 ENOENT](/languages/c/errno-eloop/) — no such file or directory.
- [errno-40 ELOOP](/languages/c/errno-eloop/) — too many symbolic links encountered.
