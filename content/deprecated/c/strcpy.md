---
title: "[Solution] C strcpy() Deprecated — Replace with strncpy() or strlcpy()"
description: "Replace strcpy() with strncpy() or strlcpy() in C to prevent buffer overflow. Complete migration guide with code examples."
deprecated_function: "strcpy"
replacement_function: "strncpy"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C strcpy() Deprecated — Replace with strncpy() or strlcpy()

The `strcpy()` function is deprecated in secure coding guidelines because it copies a string to a destination buffer without any bounds checking. If the source string is longer than the destination buffer, it causes a buffer overflow. The safe replacements are `strncpy()` (C standard) or `strlcpy()` (BSD/glibc, preferred).

## What You'll See

Compiler warnings with security flags:

```
warning: 'strcpy' is deprecated: use strncpy() or strlcpy() instead
```

On MSVC:

```
warning C4996: 'strcpy': This function or variable may be unsafe. Consider using strncpy_s instead.
```

## Why Deprecated

`strcpy()` is deprecated because:

- **No buffer size limit**: It copies until the null terminator, ignoring the destination buffer size.
- **Buffer overflow**: Source strings from external input can easily exceed the buffer.
- **No return value for required size**: You cannot detect truncation.
- **Pervasive vulnerability source**: One of the most common sources of buffer overflow vulnerabilities.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char dest[32];
    char src[] = "This is a very long string that will overflow";

    strcpy(dest, src);  // DANGEROUS — buffer overflow

    printf("%s\n", dest);
    return 0;
}
```

## New Code — strlcpy() Replacement (Preferred)

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char dest[32];
    char src[] = "This is a very long string that will overflow";

    size_t needed = strlcpy(dest, src, sizeof(dest));
    if (needed >= sizeof(dest)) {
        fprintf(stderr, "Warning: string truncated (%zu bytes needed)\n", needed);
    }

    printf("%s\n", dest);
    return 0;
}
```

## New Code — strncpy() Replacement (C Standard)

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char dest[32];
    char src[] = "This is a very long string that will overflow";

    // strncpy does NOT guarantee null termination if truncated
    strncpy(dest, src, sizeof(dest) - 1);
    dest[sizeof(dest) - 1] = '\0';

    // Note: strncpy pads with zeros if src < n, which is slow for large buffers
    size_t srclen = strlen(src);
    if (srclen >= sizeof(dest)) {
        fprintf(stderr, "Warning: string truncated\n");
    }

    printf("%s\n", dest);
    return 0;
}
```

## New Code — snprintf() Replacement (Portable)

```c
#include <stdio.h>

int main(void) {
    char dest[32];
    char src[] = "This is a very long string that will overflow";

    snprintf(dest, sizeof(dest), "%s", src);

    printf("%s\n", dest);
    return 0;
}
```

## Migration Steps

1. **Find all strcpy() calls**:

```bash
grep -rn "\bstrcpy\s*(" --include="*.c" /path/to/project/
```

2. **Replace `strcpy(dst, src)` with `strlcpy(dst, src, sizeof(dst))`** (preferred) or add null-termination after `strncpy()`.

3. **For strncpy(), always add explicit null termination** — `strncpy()` does not null-terminate if the source is too long.

4. **Avoid strncpy() for zero-fill performance** — it pads with zeros, which is slow. Use `strlcpy()` or `snprintf()` instead.

5. **Test with strings at the buffer boundary** — exactly the buffer size, one byte longer, and much longer.

6. **Audit pointer arguments** — `sizeof()` only works for arrays, not pointers. Pass the size explicitly for heap-allocated buffers.

## Related Deprecations

- [strcat → strlcat]({{< relref "/deprecated/c/strcat" >}}) — unsafe string concatenation.
- [sprintf → snprintf]({{< relref "/deprecated/c/sprintf" >}}) — unbounded formatted output.
- [gets → fgets]({{< relref "/deprecated/c/gets" >}}) — unbounded input reading.
