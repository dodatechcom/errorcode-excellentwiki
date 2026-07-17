---
title: "[Solution] C errno ELIBBAD — Accessing corrupted shared lib Fix"
description: "Fix C ELIBBAD (Accessing corrupted shared lib) by reinstalling libraries, verifying checksums, and checking filesystem integrity."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ELIBBAD — Accessing corrupted shared lib Fix

When the dynamic linker detects that a shared library file is corrupted (invalid ELF header, truncated file, or bad section data), loading the library fails and sets `errno` to `ELIBBAD`. This error indicates the library file is present and accessible but its contents are invalid.

## Common Causes

- The shared library file was corrupted during download or installation.
- Disk I/O errors have damaged the library file.
- An incomplete or partial library installation left a truncated file.
- The library was modified by malware or an incorrect patch.

## How to Fix

Reinstall the corrupted library and verify file integrity.

```bash
# Reinstall the package containing the library
sudo apt-get install --reinstall libfoo-dev  # Debian/Ubuntu
sudo yum reinstall libfoo  # RHEL/CentOS

# Verify library integrity
md5sum /usr/lib/libfoo.so
file /usr/lib/libfoo.so
```

```c
#include <dlfcn.h>
#include <stdio.h>

int main(void) {
    void *handle = dlopen("libfoo.so.1", RTLD_NOW);
    if (handle == NULL) {
        fprintf(stderr, "Library loading failed: %s\n", dlerror());
        // May indicate ELIBBAD — corrupted library
        return 1;
    }
    dlclose(handle);
    return 0;
}
```

## Examples

Loading a corrupted ELF file:

```bash
# Corrupt a library for testing
dd if=/dev/urandom of=/usr/lib/libtest.so bs=1 count=10 conv=notrunc
# Now any program using libtest.so will fail to load
```

## Related Errors

- [errno-80 ELIBBAD]({{< relref "/languages/c/errno-eLIBBAD" >}}) — accessing corrupted shared lib (numeric).
- [errno-79 ELIBACC]({{< relref "/languages/c/errno-eLIBACC" >}}) — can't access shared lib.
- [errno-8 ELIBEXEC]({{< relref "/languages/c/errno-eLIBEXEC" >}}) — cannot exec shared lib.
