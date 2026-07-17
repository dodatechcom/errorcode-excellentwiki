---
title: "[Solution] C Too many levels of symbolic links: ELOOP"
description: "Fix C ELOOP: too many levels of symbolic links. Break circular symlink chains."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Too many levels of symbolic links: ELOOP

ELOOP occurs when following symbolic links reaches the system limit (typically 40 hops). This usually means a circular symlink chain exists.

## Common Causes

```c
// Cause 1: Circular symlinks
// a -> b, b -> a
open("a/file.txt", O_RDONLY); // ELOOP

// Cause 2: Self-referencing symlink
// link -> link
readlink("link", buf, sizeof(buf)); // ELOOP

// Cause 3: Deep symlink chain
// a -> b -> c -> d -> ... (too many)
```

## How to Fix

### Fix 1: Find and break the loop

```bash
# Find circular symlinks
find /path -type l -exec readlink {} \; | sort | uniq -d

# Find circular links
find /path -type l -follow -print 2>&1 | grep -i loop
```

### Fix 2: Remove circular symlinks

```bash
rm link_name
```

### Fix 3: Use realpath to resolve

```c
char resolved[PATH_MAX];
realpath("link", resolved); // will fail if circular
```

## Examples

```c
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int main(void) {
    char resolved[PATH_MAX];
    if (realpath("mylink", resolved) == NULL) {
        perror("realpath");
        return 1;
    }
    printf("Resolves to: %s\n", resolved);
    return 0;
}
```

## Related Errors

- [Not a directory]({{< relref "/languages/c/not-a-directory" >}}) — ENOTDIR.
- [Is a directory]({{< relref "/languages/c/is-a-directory" >}}) — EISDIR.
- [Too many links]({{< relref "/languages/c/too-many-links" >}}) — EMLINK.
