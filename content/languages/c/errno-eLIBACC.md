---
title: "[Solution] C errno ELIBACC — Can't access shared lib Fix"
description: "Fix C ELIBACC (Can't access shared lib) by verifying library permissions, checking paths, and installing missing dependencies."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["elibacc", "cannot-access-shared-lib", "dynamic-loading", "library-permissions"]
weight: 5
---

# [Solution] C errno ELIBACC — Can't access shared lib Fix

When the dynamic linker cannot access a shared library required by a program (due to permission denied, missing file, or access restrictions), it may set `errno` to `ELIBACC`. This error indicates the shared library exists but cannot be opened.

## Common Causes

- The shared library file does not have read/execute permissions.
- The library file exists but is not accessible due to directory permissions.
- SELinux or AppArmor policy blocks access to the library.
- The library path is correct but the file is a symlink to an inaccessible target.

## How to Fix

Check library permissions and ensure the dynamic linker can access all required libraries.

```bash
# Check library permissions
ls -la /usr/lib/libfoo.so

# Verify linker cache
ldconfig -p | grep libfoo

# Check for SELinux denials
ausearch -m avc --start recent
```

```c
#include <dlfcn.h>
#include <stdio.h>

int main(void) {
    void *handle = dlopen("libfoo.so.1", RTLD_NOW);
    if (handle == NULL) {
        fprintf(stderr, "Cannot access library: %s\n", dlerror());
        return 1;
    }
    dlclose(handle);
    return 0;
}
```

## Examples

Dynamic linker failing to load a library:

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Program requires libfoo.so but it's not readable
    // The dynamic linker sets ELIBACC
    fprintf(stderr, "Cannot access shared library (errno %d)\n", ELIBACC);
    return 1;
}
```

## Related Errors

- [errno-79 ELIBACC]({{< relref "/languages/c/errno-eLIBACC" >}}) — can't access shared lib (numeric).
- [errno-80 ELIBBAD]({{< relref "/languages/c/errno-eLIBBAD" >}}) — accessing corrupted shared lib.
- [errno-13 EACCES]({{< relref "/languages/c/errno-eacces" >}}) — permission denied.
