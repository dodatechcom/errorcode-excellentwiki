---
title: "[Solution] C atof() Deprecated — Replace with strtod()"
description: "Replace atof() with strtod() in C for proper error detection and locale-independent parsing. Migration guide with code examples."
deprecated_function: "atof"
replacement_function: "strtod"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["atof", "strtod", "parsing", "locale", "c"]
weight: 5
---

# [Solution] C atof() Deprecated — Replace with strtod()

The `atof()` function is deprecated in secure coding guidelines because it provides no way to detect errors. If the input is not a valid number, `atof()` silently returns 0.0, making it impossible to distinguish between "0" and "invalid input". The safe replacement is `strtod()`, which sets `errno` and provides an end pointer for error detection.

## What You'll See

Compiler warnings with security flags:

```
warning: 'atof' is deprecated: use strtod() with error checking
```

## Why Deprecated

`atof()` is deprecated because:

- **No error detection**: Returns 0.0 for invalid input, indistinguishable from valid "0".
- **No errno setting**: Cannot detect overflow or underflow.
- **No end pointer**: Cannot tell where parsing stopped or if it consumed the entire string.
- **Locale-dependent**: Behavior varies with locale settings for decimal separator.
- **No trailing character detection**: `"42abc"` silently returns 42.0.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *input = "3.14";
    double value = atof(input);  // DANGEROUS — no error checking

    printf("Value: %f\n", value);

    // These all silently return 0.0 — no way to detect the error
    printf("Invalid: %f\n", atof("not_a_number"));
    printf("Overflow: %f\n", atof("1e999"));
    printf("Partial: %f\n", atof("42abc"));
    return 0;
}
```

## New Code — strtod() Replacement

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <math.h>

int parse_double(const char *str, double *result) {
    if (str == NULL || *str == '\0') {
        return -1;  // Empty or null input
    }

    char *endptr;
    errno = 0;
    *result = strtod(str, &endptr);

    if (errno == ERANGE) {
        // Overflow or underflow
        return -2;
    }

    if (*endptr != '\0') {
        // Trailing characters — partial parse
        return -3;
    }

    return 0;  // Success
}

int main(void) {
    double value;

    // Valid input
    if (parse_double("3.14", &value) == 0) {
        printf("Value: %f\n", value);
    } else {
        fprintf(stderr, "Invalid input\n");
    }

    // Invalid input
    if (parse_double("not_a_number", &value) != 0) {
        fprintf(stderr, "Correctly rejected invalid input\n");
    }

    // Overflow
    if (parse_double("1e999", &value) != 0) {
        fprintf(stderr, "Correctly detected overflow\n");
    }

    // Partial parse
    if (parse_double("42abc", &value) != 0) {
        fprintf(stderr, "Correctly rejected partial input\n");
    }

    return 0;
}
```

## New Code — Strict Number Parsing

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <ctype.h>

int parse_double_strict(const char *str, double *result) {
    if (str == NULL) return -1;

    // Skip leading whitespace
    while (isspace((unsigned char)*str)) str++;

    if (*str == '\0') return -1;

    char *endptr;
    errno = 0;
    *result = strtod(str, &endptr);

    if (errno == ERANGE) return -2;

    // Skip trailing whitespace
    while (isspace((unsigned char)*endptr)) endptr++;

    if (*endptr != '\0') return -3;

    return 0;
}

int main(void) {
    double value;
    const char *inputs[] = {"3.14", " -0.5 ", "1e10", "abc", "42.0.0", ""};

    for (size_t i = 0; i < sizeof(inputs) / sizeof(inputs[0]); i++) {
        int err = parse_double_strict(inputs[i], &value);
        if (err == 0) {
            printf("'%s' -> %f\n", inputs[i], value);
        } else {
            printf("'%s' -> error %d\n", inputs[i], err);
        }
    }

    return 0;
}
```

## Migration Steps

1. **Find all atof() calls**:

```bash
grep -rn "\batof\s*(" --include="*.c" /path/to/project/
```

2. **Replace `atof(str)` with `strtod(str, &endptr)`**.

3. **Check `errno` for ERANGE** (overflow/underflow).

4. **Check `endptr`** to ensure the entire string was consumed.

5. **Handle empty strings and NULL** before calling `strtod()`.

6. **Also replace `atoi()` with `strtol()`** and `atol()` with `strtol()` using the same pattern.

## Related Deprecations

- [atoi → strtol]({{< relref "/deprecated/c/atoi" >}}) — same issue, integer version.
- [atol → strtol]({{< relref "/deprecated/c/atol" >}}) — same issue, long integer version.
- [atoll → strtoll]({{< relref "/deprecated/c/atoll" >}}) — same issue, long long version.
