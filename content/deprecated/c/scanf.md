---
title: "[Solution] C scanf() Deprecated — Replace with fgets() + sscanf()"
description: "Replace scanf() with fgets() and sscanf() in C for safer input handling. Migration guide with code examples."
deprecated_function: "scanf"
replacement_function: "fgets + sscanf"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["scanf", "fgets", "sscanf", "input", "buffer-overflow", "c"]
weight: 5
---

# [Solution] C scanf() Deprecated — Replace with fgets() + sscanf()

The `scanf()` function family is deprecated in secure coding guidelines because `%s` and `%c` specifiers read unbounded input, causing buffer overflows. While `scanf()` itself is not removed from the standard, using it with string inputs is dangerous. The recommended pattern is to read a full line with `fgets()` then parse with `sscanf()`.

## What You'll See

Compiler warnings with security-hardened flags:

```
warning: 'scanf' is deprecated: use fgets() + sscanf() for safer input
```

On MSVC:

```
warning C4996: 'scanf': This function or variable may be unsafe. Consider using scanf_s instead.
```

## Why Deprecated

`scanf()` is deprecated for string input because:

- **Unbounded %s**: `scanf("%s", buf)` reads until whitespace with no buffer size limit.
- **Unbounded %c**: Without a width specifier, `%c` reads exactly one character but `%[...]` can overflow.
- **No line boundary**: `scanf()` reads across newlines, which is often unexpected.
- **Complex return value handling**: Distinguishing EOF from input failure requires careful logic.

## Old Code (Deprecated)

```c
#include <stdio.h>

int main(void) {
    char name[32];
    int age;

    printf("Enter name and age: ");
    scanf("%s %d", name, &age);  // DANGEROUS — no bounds on %s

    printf("Name: %s, Age: %d\n", name, age);
    return 0;
}
```

## New Code — fgets() + sscanf() Replacement

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char line[128];
    char name[32];
    int age;

    printf("Enter name and age: ");
    if (fgets(line, sizeof(line), stdin) == NULL) {
        fprintf(stderr, "Error reading input\n");
        return 1;
    }

    if (sscanf(line, "%31s %d", name, &age) != 2) {
        fprintf(stderr, "Invalid input format\n");
        return 1;
    }

    printf("Name: %s, Age: %d\n", name, age);
    return 0;
}
```

## New Code — Portable fgets() Wrapper

```c
#include <stdio.h>
#include <string.h>

// Returns 0 on success, -1 on EOF, 1 on truncation
int read_line(char *buf, size_t size, FILE *stream) {
    if (fgets(buf, size, stream) == NULL) {
        return -1;
    }

    size_t len = strlen(buf);
    if (len > 0 && buf[len - 1] == '\n') {
        buf[len - 1] = '\0';
        return 0;
    }

    // Flush remaining input if line was too long
    int c;
    while ((c = fgetc(stream)) != '\n' && c != EOF);
    return 1;
}

int main(void) {
    char name[32];
    int age;

    printf("Enter name and age: ");
    char line[128];
    if (read_line(line, sizeof(line), stdin) != 0) {
        fprintf(stderr, "Input error\n");
        return 1;
    }

    if (sscanf(line, "%31s %d", name, &age) != 2) {
        fprintf(stderr, "Invalid input format\n");
        return 1;
    }

    printf("Name: %s, Age: %d\n", name, age);
    return 0;
}
```

## Migration Steps

1. **Find all scanf() calls with %s or %[**:

```bash
grep -rn "\bscan[fp]\s*(" --include="*.c" /path/to/project/
```

2. **Replace `scanf("%s", buf)` with `fgets(buf, sizeof(buf), stdin)`**.

3. **Parse the line with `sscanf()`** using width specifiers (`%31s`) to limit field widths.

4. **Strip trailing newline** from `fgets()` output if present.

5. **Handle empty input and format errors** — `sscanf()` returns the number of successfully parsed fields.

6. **Use `getline()`** if you need to read lines of arbitrary length.

## Related Deprecations

- [gets → fgets]({{< relref "/deprecated/c/gets" >}}) — another unbounded input function.
- [sprintf → snprintf]({{< relref "/deprecated/c/sprintf" >}}) — unbounded formatted output.
- [tmpnam → mkstemp]({{< relref "/deprecated/c/tmpnam" >}}) — race condition in temp file creation.
