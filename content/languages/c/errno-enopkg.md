---
title: "[Solution] C errno ENOPKG — No package found Fix"
description: "Fix C ENOPKG (No package found) by verifying shared library availability and checking package installation."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enopkg", "no-package-found", "shared-library", "dynamic-loading"]
weight: 5
---

# [Solution] C errno ENOPKG — No package found Fix

When a shared library or package required by a dynamically linked program cannot be found, the dynamic linker may set `errno` to `ENOPKG`. This error indicates that a required package or library is missing from the system.

## Common Causes

- A required shared library is not installed on the system.
- The `LD_LIBRARY_PATH` does not include the directory containing the library.
- The library was removed or the package was uninstalled.
- The dynamic linker's cache (`ldconfig`) is not up to date.

## How to Fix

Install the missing package and update the linker cache.

```bash
# Find which package provides the missing library
ldconfig -p | grep libname
dpkg -S libname.so  # Debian/Ubuntu
rpm -qf /path/to/libname.so  # RHEL/CentOS

# Update linker cache
sudo ldconfig
```

```c
#include <dlfcn.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    void *handle = dlopen("libnonexistent.so", RTLD_LAZY);
    if (handle == NULL) {
        fprintf(stderr, "dlopen failed: %s\n", dlerror());
        // May report ENOPKG or similar
    }
    return 0;
}
```

## Examples

Loading a missing shared library:

```c
#include <dlfcn.h>
#include <stdio.h>

int main(void) {
    void *handle = dlopen("libfoo.so.1", RTLD_NOW);
    if (handle == NULL) {
        fprintf(stderr, "Cannot load library: %s\n", dlerror());
        // The dynamic linker may set errno to ENOPKG
    }
    return 0;
}
```

## Related Errors

- [errno-1 ENOEXEC](/languages/c/errno-enopkg/) — exec format error.
- [errno-2 ENOENT](/languages/c/errno-enopkg/) — no such file or directory.
- [errno-40 ELOOP]({{< relref "/languages/c/errno-eloop" >}}) — too many levels of symbolic links.
