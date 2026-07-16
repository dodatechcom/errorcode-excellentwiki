---
title: "[Solution] C Stack Smashing Detected — Buffer Overflow Security Fix"
description: "Fix C '*** stack smashing detected ***' buffer overflow errors. Understand stack canaries, prevent overflows, and secure your C programs."
languages: ["c"]
severities: ["critical"]
error-types: ["runtime-error", "memory-error"]
tags: ["stack-smashing", "buffer-overflow", "stack-canary", "security", "fortify-source"]
weight: 5
---

# [Solution] C Stack Smashing Detected — Buffer Overflow Security Fix

The error **"*** stack smashing detected ***: terminated"** is printed by glibc when a stack-based buffer overflow overwrites the stack canary — a secret value placed on the stack by the compiler to detect buffer overflows. When `main()` or a function returns, the runtime checks the canary; if it was modified, the program is killed immediately to prevent potential exploitation. This is a security-critical error that must be fixed.

## Common Causes

- **Unbounded string copy** — using `gets()`, `strcpy()`, or `sprintf()` without size limits
- **Incorrect buffer size** — allocating fewer bytes than needed for the data being stored
- **Off-by-one error** — forgetting to account for the NUL terminator in strings
- **Array indexing without bounds checking** — writing to an index beyond the array size

## How to Fix

### Fix 1: Use bounded string functions

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char name[32];

    /* WRONG — gets() has no bounds checking */
    gets(name);

    /* CORRECT — fgets() limits input to buffer size */
    if (fgets(name, sizeof(name), stdin) != NULL) {
        /* strip trailing newline */
        name[strcspn(name, "\n")] = '\0';
    }
    return 0;
}
```

### Fix 2: Use snprintf instead of sprintf

```c
#include <stdio.h>

int main(void) {
    char buf[64];
    int id = 42;
    const char *name = "Alice";

    /* WRONG — sprintf has no size limit */
    sprintf(buf, "User %d: %s", id, name);

    /* CORRECT — snprintf limits output to buffer size */
    int needed = snprintf(buf, sizeof(buf), "User %d: %s", id, name);
    if (needed >= (int)sizeof(buf)) {
        printf("Warning: output was truncated\n");
    }
    return 0;
}
```

### Fix 3: Use strncpy or strlcpy correctly

```c
#include <string.h>
#include <stdio.h>

int main(void) {
    char dst[32];
    const char *src = "This is a very long string that exceeds 32 bytes";

    /* CORRECT — strlcpy (BSD/macOS) or strncpy + explicit NUL */
    strncpy(dst, src, sizeof(dst) - 1);
    dst[sizeof(dst) - 1] = '\0';  /* always NUL-terminate */

    printf("%s\n", dst);
    return 0;
}
```

### Fix 4: Allocate dynamically when needed

```c
#include <stdlib.h>
#include <string.h>

char *duplicate_string(const char *src) {
    size_t len = strlen(src) + 1;
    char *copy = malloc(len);
    if (copy) {
        memcpy(copy, src, len);
    }
    return copy;
}
```

## Examples

```c
#include <stdio.h>
#include <string.h>

/* WRONG — buffer overflow in function */
void vulnerable(const char *user_input) {
    char password[16];
    strcpy(password, user_input);  /* stack smash if input > 15 chars */
}

/* CORRECT */
void safe(const char *user_input) {
    char password[16];
    strncpy(password, user_input, sizeof(password) - 1);
    password[sizeof(password) - 1] = '\0';
}
```

## Compilation Flags for Protection

```bash
# Enable stack protector (default on most modern compilers)
gcc -fstack-protector-strong -o myprogram myprogram.c

# Enable Fortified source functions (sprintf_s, snprintf, etc.)
gcc -D_FORTIFY_SOURCE=2 -o myprogram myprogram.c

# Enable AddressSanitizer for runtime detection
gcc -fsanitize=address -g -o myprogram myprogram.c
```

## Related Errors

- [Segmentation Fault (Core Dumped)]({{< relref "/languages/c/segfault" >}}) — general memory access violation
- [Heap Corruption Detected]({{< relref "/languages/c/heap-corruption" >}}) — heap buffer overflow
- [Use After Free]({{< relref "/languages/c/use-after-free" >}}) — accessing freed memory
