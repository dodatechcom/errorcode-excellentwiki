---
title: "[Solution] C Format String Vulnerability — Warning Format Not a String Literal Fix"
description: "Fix C format string vulnerabilities and compiler warnings. Prevent crashes and security exploits from passing user input directly to printf."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["format-string", "printf", "security", "vulnerability", "format-warning"]
weight: 5
---

# [Solution] C Format String Vulnerability — Warning Format Not a String Literal Fix

A **format string vulnerability** occurs when user-controlled data is passed as the format argument to `printf`, `fprintf`, `sprintf`, or similar functions. The compiler warns with `warning: format not a string literal and no format arguments` because the `%` characters in the input are interpreted as format specifiers, causing crashes (e.g., `Segfault` from `%n`) or leaking sensitive memory (e.g., `%x` printing stack values).

## Common Causes

- **Passing a variable directly to `printf()`** — `printf(variable)` instead of `printf("%s", variable)`
- **Using `%n` with user input** — an attacker can write to arbitrary memory addresses
- **Stack reads via `%x` or `%p`** — an attacker can dump the call stack to extract secrets
- **Compiler not enforcing warnings** — compiling without `-Wformat-security` hides the bug

## How to Fix

### Fix 1: Always use a format string literal

```c
#include <stdio.h>

int main(void) {
    const char *msg = "Hello, World!";

    /* WRONG — format string vulnerability */
    printf(msg);

    /* CORRECT — use %s format specifier */
    printf("%s\n", msg);

    return 0;
}
```

### Fix 2: Validate format strings in wrapper functions

```c
#include <stdio.h>
#include <stdarg.h>
#include <string.h>

/* Safe wrapper — rejects non-literal format strings */
void safe_printf(const char *fmt, ...) {
    /* Check that fmt is a string literal (at compile time when possible) */
    if (fmt == NULL) return;

    va_list args;
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
}

int main(void) {
    safe_printf("Count: %d\n", 42);      /* OK */
    /* safe_printf(user_input); */        /* would be caught if linted */
    return 0;
}
```

### Fix 3: Use -Wformat-security and -Werror

```bash
# Enable strict format string warnings and treat them as errors
gcc -Wformat -Wformat-security -Werror -o myprogram myprogram.c

# For even stricter checking
gcc -Wformat=2 -Wformat-security -Werror=format-security -o myprogram myprogram.c
```

### Fix 4: Use snprintf for user-controlled format strings

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char user_input[256];
    /* assume user_input comes from user */

    /* WRONG — user input used as format string */
    /* printf(user_input); */

    /* CORRECT — treat user input as data, not format */
    printf("%s", user_input);

    /* Or use snprintf to safely format the message */
    char output[512];
    snprintf(output, sizeof(output), "Message: %s", user_input);
    printf("%s", output);

    return 0;
}
```

## Examples

```c
#include <stdio.h>

int main(void) {
    /* Example 1: Stack leak — attacker learns stack layout */
    char *user_input = "%08x.%08x.%08x.%08x";
    printf(user_input);  /* prints 4 stack values */

    /* Example 2: Crash from %n — writes to random address */
    char *evil = "%n";
    printf(evil);  /* segfault — writes to invalid address */

    /* Example 3: Information leak with %s */
    char secret[] = "SECRET_KEY_123";
    char *evil2 = "%s";
    printf(evil2);  /* may print memory contents */

    return 0;
}
```

## Security Impact

| Specifier | Effect |
|---|---|
| `%x` | Reads a 4-byte value from the stack |
| `%p` | Prints a pointer address |
| `%s` | Reads memory until a NUL byte — can crash or leak data |
| `%n` | Writes an integer to an address on the stack — **arbitrary write** |

## Related Errors

- [Segmentation Fault (Core Dumped)]({{< relref "/languages/c/segfault" >}}) — format string `%n` writes to invalid addresses causing crashes
- [Buffer Overflow: Stack Smashing]({{< relref "/languages/c/buffer-overflow" >}}) — stack corruption from unbounded writes
- [Array Index Out of Bounds]({{< relref "/languages/c/array-out-of-bounds" >}}) — out-of-bounds access patterns
