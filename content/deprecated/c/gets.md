---
title: "[Solution] C gets() Deprecated — Replace with fgets()"
description: "Replace dangerous gets() with fgets() in C. Prevents buffer overflow vulnerabilities. Complete migration guide with code examples."
deprecated_function: "gets"
replacement_function: "fgets"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C gets() Deprecated — Replace with fgets()

The `gets()` function was deprecated in C99 and removed in C11 because it is impossible to use safely. It reads input from stdin with no way to limit how many bytes are read into the buffer, making it the single most dangerous function in the C standard library. Every use of `gets()` is a potential buffer overflow vulnerability.

## What You'll See

Compiling with `-std=c11` or newer:

```
warning: 'gets' is deprecated: it is insecure and should not be used
```

On older compilers, you may see:

```
warning: the `gets' function is dangerous and should not be used.
```

## Why Deprecated

`gets()` was removed because:

- **No buffer size limit**: It reads until a newline or EOF with no way to specify the buffer size.
- **Buffer overflow**: If input exceeds the buffer, it overwrites adjacent memory, enabling arbitrary code execution.
- **No return value check**: You cannot detect read errors reliably.
- **Every real-world use is vulnerable**: Even with careful usage, it cannot be made safe.

## Old Code (Deprecated)

```c
#include <stdio.h>

int main(void) {
    char name[64];

    printf("Enter your name: ");
    gets(name);  // DANGEROUS — no bounds checking

    printf("Hello, %s!\n", name);
    return 0;
}
```

## New Code — fgets() Replacement

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char name[64];

    printf("Enter your name: ");
    if (fgets(name, sizeof(name), stdin) == NULL) {
        fprintf(stderr, "Error reading input\n");
        return 1;
    }

    // Remove trailing newline if present
    size_t len = strlen(name);
    if (len > 0 && name[len - 1] == '\n') {
        name[len - 1] = '\0';
    } else {
        // Input was too long — flush remaining characters
        int c;
        while ((c = getchar()) != '\n' && c != EOF);
        fprintf(stderr, "Warning: input truncated\n");
    }

    printf("Hello, %s!\n", name);
    return 0;
}
```

## New Code — Read Entire Line (Dynamic Buffer)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *read_line(FILE *stream) {
    char *line = NULL;
    size_t capacity = 0;
    ssize_t len;

    len = getline(&line, &capacity, stream);
    if (len == -1) {
        free(line);
        return NULL;
    }

    // Remove trailing newline
    if (len > 0 && line[len - 1] == '\n') {
        line[len - 1] = '\0';
    }

    return line;
}

int main(void) {
    printf("Enter your name: ");
    char *name = read_line(stdin);
    if (name == NULL) {
        fprintf(stderr, "Error reading input\n");
        return 1;
    }

    printf("Hello, %s!\n", name);
    free(name);
    return 0;
}
```

## Migration Steps

1. **Find all gets() calls**:

```bash
grep -rn "\bgets\s*(" --include="*.c" /path/to/project/
```

2. **Replace `gets(buf)` with `fgets(buf, sizeof(buf), stdin)`**.

3. **Add newline stripping code** — `fgets()` includes the newline character, unlike `gets()`.

4. **Check for truncation** — if `strlen(buf) == sizeof(buf) - 1` and the last character is not `\n`, the input was truncated. Decide how to handle this (error, flush, or accept).

5. **For dynamic-length input**, use `getline()` instead of `fgets()`.

6. **Test with long input** — verify that input exceeding the buffer size is handled gracefully.

## Related Deprecations

- [sprintf → snprintf]({{< relref "/deprecated/c/sprintf" >}}) — another fixed-buffer function without bounds checking.
- [strcpy → strncpy]({{< relref "/deprecated/c/strcpy" >}}) — similar buffer overflow risk with string copies.
- [strcat → strlcat]({{< relref "/deprecated/c/strcat" >}}) — unsafe string concatenation.
