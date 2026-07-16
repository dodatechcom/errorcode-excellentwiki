---
title: "[Solution] C strcat() Deprecated — Replace with strlcat() or snprintf()"
description: "Replace strcat() with strlcat() or snprintf() in C to prevent buffer overflow. Migration guide with code examples."
deprecated_function: "strcat"
replacement_function: "strlcat"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["strcat", "strlcat", "buffer-overflow", "string", "c"]
weight: 5
---

# [Solution] C strcat() Deprecated — Replace with strlcat() or snprintf()

The `strcat()` function is deprecated in secure coding guidelines because it appends to a destination buffer without any bounds checking. If the combined length of the destination and source exceeds the buffer, it causes a buffer overflow. The safe replacements are `strlcat()` (BSD/glibc) or using `snprintf()` to build the string.

## What You'll See

Compiler warnings with security-hardened build flags:

```
warning: 'strcat' is deprecated: use strlcat() or snprintf() instead
```

On MSVC:

```
warning C4996: 'strcat': This function or variable may be unsafe. Consider using strlcat instead.
```

## Why Deprecated

`strcat()` is deprecated because:

- **No buffer size parameter**: It assumes the destination buffer is large enough.
- **Buffer overflow**: Concatenation can easily exceed the buffer if the source string grows.
- **Requires strlen() calls**: You must manually calculate the destination length, which is error-prone.
- **Common source of vulnerabilities**: Many CVEs result from off-by-one errors in `strcat()` usage.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char path[64] = "/home/user";
    char filename[] = "/Documents/report.txt";

    strcat(path, filename);  // DANGEROUS — may overflow path

    printf("Path: %s\n", path);
    return 0;
}
```

## New Code — strlcat() Replacement

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char path[64] = "/home/user";
    char filename[] = "/Documents/report.txt";

    if (strlcat(path, filename, sizeof(path)) >= sizeof(path)) {
        fprintf(stderr, "Warning: path was truncated\n");
    }

    printf("Path: %s\n", path);
    return 0;
}
```

## New Code — snprintf() Replacement (Portable)

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char path[64] = "/home/user";
    char filename[] = "/Documents/report.txt";

    snprintf(path, sizeof(path), "%s%s", path, filename);

    printf("Path: %s\n", path);
    return 0;
}
```

## New Code — Helper Function for strlcat (Portability Shim)

```c
#include <string.h>

#ifndef HAVE_STRLCAT
size_t strlcat(char *dst, const char *src, size_t dstsize) {
    size_t dstlen = strlen(dst);
    size_t srclen = strlen(src);

    if (dstlen >= dstsize) {
        return dstsize + srclen;
    }

    size_t copylen = srclen < (dstsize - dstlen - 1) ? srclen : (dstsize - dstlen - 1);
    memcpy(dst + dstlen, src, copylen);
    dst[dstlen + copylen] = '\0';

    return dstlen + srclen;
}
#endif
```

## Migration Steps

1. **Find all strcat() calls**:

```bash
grep -rn "\bstrcat\s*(" --include="*.c" /path/to/project/
```

2. **Replace `strcat(dst, src)` with `strlcat(dst, src, sizeof(dst))`**.

3. **Check return value** — if `strlcat()` returns a value `>= sizeof(dst)`, truncation occurred.

4. **For stack-allocated buffers**, `sizeof()` works. For heap-allocated buffers, pass the allocated size explicitly.

5. **Consider using `snprintf()`** for multi-part string assembly — it's more explicit about buffer sizes.

6. **Audit all string concatenation** for potential overflow, including chained `strcat()` calls.

## Related Deprecations

- [strcpy → strncpy]({{< relref "/deprecated/c/strcpy" >}}) — unsafe string copy without bounds.
- [sprintf → snprintf]({{< relref "/deprecated/c/sprintf" >}}) — unbounded formatted output.
- [gets → fgets]({{< relref "/deprecated/c/gets" >}}) — unbounded input reading.
