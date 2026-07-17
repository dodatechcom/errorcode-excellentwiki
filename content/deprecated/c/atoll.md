---
title: "[Solution] C atoll() Deprecated — Replace with strtoll()"
description: "Replace atoll() with strtoll() in C for proper error detection. Migration guide with code examples."
deprecated_function: "atoll"
replacement_function: "strtoll"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C atoll() Deprecated — Replace with strtoll()

The `atoll()` function is deprecated in secure coding guidelines because it provides no way to detect errors. If the input is not a valid long long integer, `atoll()` silently returns 0LL, and it has undefined behavior on overflow. The safe replacement is `strtoll()`, which provides full error detection.

## What You'll See

Compiler warnings with security flags:

```
warning: 'atoll' is deprecated: use strtoll() with error checking
```

## Why Deprecated

`atoll()` is deprecated because:

- **No error detection**: Returns 0LL for invalid input, indistinguishable from valid "0".
- **Undefined behavior on overflow**: The result is undefined if the value exceeds `long long` range.
- **No end pointer**: Cannot tell where parsing stopped.
- **No errno setting**: Cannot detect overflow conditions.
- **Non-standard on some platforms**: May not be available on all systems.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *input = "98765432101234";
    long long value = atoll(input);  // DANGEROUS — no error checking

    printf("Value: %lld\n", value);

    // All return 0LL — no way to detect the error
    printf("Invalid: %lld\n", atoll("abc"));
    printf("Partial: %lld\n", atoll("42abc"));
    printf("Overflow: %lld\n", atoll("999999999999999999999999999999"));
    return 0;
}
```

## New Code — strtoll() Replacement

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int parse_longlong(const char *str, long long *result) {
    if (str == NULL || *str == '\0') {
        return -1;
    }

    char *endptr;
    errno = 0;
    *result = strtoll(str, &endptr, 10);

    if (errno == ERANGE) {
        return -2;  // Overflow or underflow
    }

    if (*endptr != '\0') {
        return -3;  // Trailing characters
    }

    return 0;
}

int main(void) {
    long long value;

    if (parse_longlong("98765432101234", &value) == 0) {
        printf("Value: %lld\n", value);
    }

    if (parse_longlong("abc", &value) != 0) {
        fprintf(stderr, "Correctly rejected invalid input\n");
    }

    if (parse_longlong("42abc", &value) != 0) {
        fprintf(stderr, "Correctly rejected partial input\n");
    }

    if (parse_longlong("999999999999999999999999999999", &value) != 0) {
        fprintf(stderr, "Correctly detected overflow\n");
    }

    return 0;
}
```

## Migration Steps

1. **Find all atoll() calls**:

```bash
grep -rn "\batoll\s*(" --include="*.c" /path/to/project/
```

2. **Replace `atoll(str)` with `strtoll(str, &endptr, 10)`**.

3. **Check `errno` for ERANGE** — indicates overflow or underflow.

4. **Check `endptr`** to ensure the entire string was consumed.

5. **For `int` values**, use `strtol()` to replace `atoi()`.

6. **For `double` values**, use `strtod()` to replace `atof()`.

## Related Deprecations

- [atoi → strtol]({{< relref "/deprecated/c/atoi" >}}) — same issue, int version.
- [atol → strtol]({{< relref "/deprecated/c/atol" >}}) — same issue, long version.
- [atof → strtod]({{< relref "/deprecated/c/atof" >}}) — same issue, floating-point version.
