---
title: "[Solution] C errno ELIBEXEC — Cannot exec a shared lib directly Fix"
description: "Fix C ELIBEXEC (Cannot exec a shared lib directly) by using a proper executable wrapper and fixing execve calls."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["elibexec", "cannot-exec-shared-lib", "execve", "dynamic-linking"]
weight: 5
---

# [Solution] C errno ELIBEXEC — Cannot exec a shared lib directly Fix

When `execve()` is called with a path pointing to a shared library (`.so` file) instead of a proper executable, the system call fails and sets `errno` to `ELIBEXEC`. Shared libraries are not directly executable — they must be loaded by a program or the dynamic linker.

## Common Causes

- The `execve()` argument points to a `.so` shared library instead of an executable.
- A symlink that should point to an executable instead points to a shared library.
- The executable was replaced by a shared library during an update.
- A script or wrapper incorrectly invokes a shared library path.

## How to Fix

Always exec proper executables, not shared libraries. Use `dlopen()` to load shared libraries at runtime.

```c
#include <dlfcn.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    void *handle = dlopen("libplugin.so", RTLD_NOW);
    if (handle == NULL) {
        fprintf(stderr, "dlopen failed: %s\n", dlerror());
        return 1;
    }

    // Get function pointer from the library
    void (*init)(void) = dlsym(handle, "plugin_init");
    if (init) init();

    dlclose(handle);
    return 0;
}
```

## Examples

Incorrectly execve-ing a shared library:

```c
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    char *argv[] = {"/usr/lib/libfoo.so", NULL};
    if (execve("/usr/lib/libfoo.so", argv, NULL) == -1) {
        if (errno == ELIBEXEC) {
            fprintf(stderr, "Cannot exec shared library directly\n");
        } else {
            perror("execve");
        }
    }
    return 1;
}
```

## Related Errors

- [errno-83 ELIBEXEC]({{< relref "/languages/c/errno-eLIBEXEC" >}}) — cannot exec shared lib directly (numeric).
- [errno-1 ENOEXEC](/languages/c/errno-eLIBEXEC/) — exec format error.
- [errno-80 ELIBBAD]({{< relref "/languages/c/errno-eLIBBAD" >}}) — accessing corrupted shared lib.
