---
title: "[Solution] C tmpnam() Deprecated — Replace with mkstemp()"
description: "Replace tmpnam() with mkstemp() in C to avoid TOCTOU race conditions. Complete migration guide with code examples."
deprecated_function: "tmpnam"
replacement_function: "mkstemp"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["tmpnam", "mkstemp", "tempfile", "race-condition", "security", "c"]
weight: 5
---

# [Solution] C tmpnam() Deprecated — Replace with mkstemp()

The `tmpnam()` function is deprecated because it has a time-of-check-to-time-of-use (TOCTOU) race condition. It generates a temporary filename, but between the time you check the name doesn't exist and the time you create the file, another process can create a file with that name. The safe replacement is `mkstemp()`, which atomically creates and opens the file.

## What You'll See

Compiler warnings:

```
warning: 'tmpnam' is deprecated: use mkstemp() instead
```

On MSVC:

```
warning C4996: 'tmpnam': This function or variable may be unsafe. Consider using _mktemp_s instead.
```

## Why Deprecated

`tmpnam()` is deprecated because:

- **TOCTOU race condition**: The file might exist when checked but be created by another process before you open it.
- **Predictable filenames**: The names follow a predictable pattern, making them vulnerable to symlink attacks.
- **No atomic creation**: There is no way to create the file and get exclusive access in one step.
- **Security vulnerability**: An attacker can pre-create the file or a symlink, leading to arbitrary file writes.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char tmpname[L_tmpnam];

    // Generate a temporary filename
    if (tmpnam(tmpname) == NULL) {
        fprintf(stderr, "Failed to generate temp name\n");
        return 1;
    }

    // RACE CONDITION — another process could create this file here
    FILE *fp = fopen(tmpname, "w");
    if (fp == NULL) {
        perror("fopen");
        return 1;
    }

    fprintf(fp, "Temporary data\n");
    fclose(fp);

    // Delete the file
    remove(tmpname);
    return 0;
}
```

## New Code — mkstemp() Replacement

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    char tmpl[] = "/tmp/myapp.XXXXXX";

    // mkstemp atomically creates the file with exclusive access
    int fd = mkstemp(tmpl);
    if (fd == -1) {
        perror("mkstemp");
        return 1;
    }

    // tmpl now contains the actual filename created
    printf("Temp file: %s\n", tmpl);

    // Write data
    const char *data = "Temporary data\n";
    write(fd, data, strlen(data));

    // Close the file
    close(fd);

    // Optionally remove it
    unlink(tmpl);
    return 0;
}
```

## New Code — Using tmpfile() (Simpler)

```c
#include <stdio.h>

int main(void) {
    // tmpfile() creates and opens a temporary file that is
    // automatically removed when closed or program exits
    FILE *fp = tmpfile();
    if (fp == NULL) {
        perror("tmpfile");
        return 1;
    }

    fprintf(fp, "Temporary data\n");
    rewind(fp);

    // Read back
    char buf[64];
    fgets(buf, sizeof(buf), fp);
    printf("Read: %s", buf);

    // File is automatically removed when closed
    fclose(fp);
    return 0;
}
```

## Migration Steps

1. **Find all tmpnam() and _tempnam() calls**:

```bash
grep -rn "\btmpnam\s*\|\b_tempnam\s*\|\bmktemp\s*(" --include="*.c" /path/to/project/
```

2. **Replace `tmpnam(name)` with `mkstemp(template)`** using a template ending in `"XXXXXX"`.

3. **Use the returned file descriptor** instead of opening the file separately — `mkstemp()` creates and opens it atomically.

4. **Call `unlink()` when the file is no longer needed** if you want it removed.

5. **For temporary files that should be removed on close**, use `tmpfile()` instead.

6. **Never use `mktemp()`** — it has the same race condition as `tmpnam()`.

## Related Deprecations

- [system → exec family]({{< relref "/deprecated/c/system" >}}) — another security-sensitive function.
- [gets → fgets]({{< relref "/deprecated/c/gets" >}}) — unsafe input handling.
- [signal → sigaction]({{< relref "/deprecated/c/signal" >}}) — unreliable signal handling.
