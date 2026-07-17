---
title: "[Solution] C atoi() Deprecated — Replace with strtol()"
description: "Replace atoi() with strtol() in C for proper error detection. Migration guide with code examples."
deprecated_function: "atoi"
replacement_function: "strtol"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C atoi() Deprecated — Replace with strtol()

The `atoi()` function is deprecated in secure coding guidelines because it provides no way to detect errors. If the input is not a valid integer, `atoi()` silently returns 0, making it impossible to distinguish between "0" and "invalid input". It also has undefined behavior on overflow. The safe replacement is `strtol()`, which provides full error detection.

## What You'll See

Compiler warnings with security flags:

```
warning: 'atoi' is deprecated: use strtol() with error checking
```

## Why Deprecated

`atoi()` is deprecated because:

- **No error detection**: Returns 0 for invalid input, indistinguishable from valid "0".
- **Undefined behavior on overflow**: The result is undefined if the value exceeds `int` range.
- **No end pointer**: Cannot tell where parsing stopped.
- **No errno setting**: Cannot detect overflow.
- **Silent truncation**: `"99999999999999"` may silently overflow.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *input = "42";
    int value = atoi(input);  // DANGEROUS — no error checking

    printf("Value: %d\n", value);

    // All return 0 — no way to detect the error
    printf("Invalid: %d\n", atoi("abc"));
    printf("Partial: %d\n", atoi("42abc"));
    printf("Overflow: %d\n", atoi("9999999999999999"));
    return 0;
}
```

## New Code — strtol() Replacement

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int parse_int(const char *str, int *result) {
    if (str == NULL || *str == '\0') {
        return -1;
    }

    char *endptr;
    errno = 0;
    long val = strtol(str, &endptr, 10);

    if (errno == ERANGE) {
        return -2;  // Overflow or underflow
    }

    if (val > INT_MAX || val < INT_MIN) {
        return -2;  // Value out of int range
    }

    if (*endptr != '\0') {
        return -3;  // Trailing characters
    }

    *result = (int)val;
    return 0;
}

int main(void) {
    int value;

    if (parse_int("42", &value) == 0) {
        printf("Value: %d\n", value);
    }

    if (parse_int("abc", &value) != 0) {
        fprintf(stderr, "Correctly rejected invalid input\n");
    }

    if (parse_int("42abc", &value) != 0) {
        fprintf(stderr, "Correctly rejected partial input\n");
    }

    if (parse_int("9999999999999999", &value) != 0) {
        fprintf(stderr, "Correctly detected overflow\n");
    }

    return 0;
}
```

## New Code — Generic Number Parsing

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

typedef enum {
    PARSE_OK = 0,
    PARSE_EMPTY,
    PARSE_OVERFLOW,
    PARSE_INCOMPLETE
} ParseResult;

ParseResult parse_int_strict(const char *str, int *result) {
    if (str == NULL || *str == '\0') return PARSE_EMPTY;

    char *endptr;
    errno = 0;
    long val = strtol(str, &endptr, 10);

    if (errno == ERANGE || val > INT_MAX || val < INT_MIN) {
        return PARSE_OVERFLOW;
    }

    if (*endptr != '\0') return PARSE_INCOMPLETE;

    *result = (int)val;
    return PARSE_OK;
}

int main(void) {
    int value;
    const char *tests[] = {"0", "42", "-7", "abc", "42x", "9999999999999999", ""};

    for (size_t i = 0; i < sizeof(tests) / sizeof(tests[0]); i++) {
        ParseResult result = parse_int_strict(tests[i], &value);
        if (result == PARSE_OK) {
            printf("'%s' -> %d\n", tests[i], value);
        } else {
            printf("'%s' -> error %d\n", tests[i], result);
        }
    }

    return 0;
}
```

## Migration Steps

1. **Find all atoi() calls**:

```bash
grep -rn "\batoi\s*(" --include="*.c" /path/to/project/
```

2. **Replace `atoi(str)` with `strtol(str, &endptr, 10)`**.

3. **Check `errno` for ERANGE** — indicates overflow or underflow.

4. **Check `endptr`** to ensure the entire string was consumed.

5. **Check range** — `strtol()` returns `long`, so verify it fits in `int` if needed.

6. **Also replace `atof()` with `strtod()`** and `atol()` with `strtol()`.

## Related Deprecations

- [atol → strtol]({{< relref "/deprecated/c/atol" >}}) — same issue, long integer version.
- [atoll → strtoll]({{< relref "/deprecated/c/atoll" >}}) — same issue, long long version.
- [atof → strtod]({{< relref "/deprecated/c/atof" >}}) — same issue, floating-point version.
