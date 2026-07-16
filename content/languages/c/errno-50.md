---
title: "[Solution] C errno 50 ENOPKG — No package found"
description: "Fix C errno 50 ENOPKG (No package found) by installing required packages, checking package manager, or using static linking."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enopkg", "errno-50", "package", "not-found", "missing-package"]
weight: 5
---

# [Solution] C errno 50 ENOPKG — No package found

No package found occurs when a system call fails and sets `errno` to 50. This error indicates that the requested operation cannot be performed due to the specific condition described by ENOPKG.

## Common Causes

- Trying to load a shared library that is not installed.
- Package dependency missing.
- Using dlopen() with a library that doesn't exist.
- System package manager reports missing dependencies.

## How to Fix

```c
#include <dlfcn.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    void *handle = dlopen("libnonexistent.so", RTLD_LAZY);
    if (handle == NULL) {
        fprintf(stderr, "dlopen failed: %s (errno %d)\n", dlerror(), errno);
        return 1;
    }
    dlclose(handle);
    return 0;
}
```

## Examples

```c
#include <stdio.h>
#include <dlfcn.h>

int main(void) {
    void *handle = dlopen("libm.so", RTLD_LAZY);
    if (handle != NULL) {
        printf("Library loaded successfully\n");
        dlclose(handle);
    } else {
        fprintf(stderr, "Failed to load library: %s\n", dlerror());
    }
    return 0;
}
```

## Related Errors

- [errno-12 ENOMEM]({{< relref "/languages/c/errno-12" >}}) — cannot allocate memory.
- [errno-50 ENOPKG]({{< relref "/languages/c/errno-50" >}}) — no package found (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
