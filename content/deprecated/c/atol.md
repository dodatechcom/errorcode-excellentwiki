---
title: "[Solution] C atol() Deprecated — Replace with strtol()"
description: "Replace atol() with strtol() in C for proper error detection. Migration guide with code examples."
deprecated_function: "atol"
replacement_function: "strtol"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C atol() Deprecated — Replace with strtol()

The `atol()` function is deprecated in secure coding guidelines because it provides no way to detect errors. If the input is not a valid long integer, `atol()` silently returns 0L, and it has undefined behavior on overflow. The safe replacement is `strtol()`, which provides full error detection including overflow, underflow, and partial parsing.

## What You'll See

Compiler warnings with security flags:

```
warning: 'atol' is deprecated: use strtol() with error checking
```

## Why Deprecated

`atol()` is deprecated because:

- **No error detection**: Returns 0L for invalid input, indistinguishable from valid "0".
- **Undefined behavior on overflow**: The result is undefined if the value exceeds `long` range.
- **No end pointer**: Cannot tell where parsing stopped or if parsing was complete.
- **No errno setting**: Cannot detect overflow conditions.
- **Silent truncation**: Large numbers may silently wrap around.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *input = "1234567890";
    long value = atol(input);  // DANGEROUS — no error checking

    printf("Value: %ld\n", value);

    // All return 0L — no way to detect the error
    printf("Invalid: %ld\n", atol("abc"));
    printf("Partial: %ld\n", atol("42abc"));
    printf("Overflow: %ld\n", atol("999999999999999999999"));
    return 0;
}
```

## New Code — strtol() Replacement

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int parse_long(const char *str, long *result) {
    if (str == NULL || *str == '\0') {
        return -1;
    }

    char *endptr;
    errno = 0;
    *result = strtol(str, &endptr, 10);

    if (errno == ERANGE) {
        return -2;  // Overflow or underflow
    }

    if (*endptr != '\0') {
        return -3;  // Trailing characters
    }

    return 0;
}

int main(void) {
    long value;

    if (parse_long("1234567890", &value) == 0) {
        printf("Value: %ld\n", value);
    }

    if (parse_long("abc", &value) != 0) {
        fprintf(stderr, "Correctly rejected invalid input\n");
    }

    if (parse_long("42abc", &value) != 0) {
        fprintf(stderr, "Correctly rejected partial input\n");
    }

    if (parse_long("999999999999999999999", &value) != 0) {
        fprintf(stderr, "Correctly detected overflow\n");
    }

    return 0;
}
```

## Migration Steps

1. **Find all atol() calls**:

```bash
grep -rn "\batol\s*(" --include="*.c" /path/to/project/
```

2. **Replace `atol(str)` with `strtol(str, &endptr, 10)`**.

3. **Check `errno` for ERANGE** — indicates overflow or underflow.

4. **Check `endptr`** to ensure the entire string was consumed.

5. **Note**: `strtol()` returns `long`, so it's a direct replacement for `atol()` without range checking.

6. **For `long long` values**, use `strtoll()` to replace `atoll()`.

## Related Deprecations

- [atoi → strtol]({{< relref "/deprecated/c/atoi" >}}) — same issue, int version.
- [atoll → strtoll]({{< relref "/deprecated/c/atoll" >}}) — same issue, long long version.
- [atof → strtod]({{< relref "/deprecated/c/atof" >}}) — same issue, floating-point version.
