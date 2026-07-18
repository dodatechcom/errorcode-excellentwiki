---
title: "[Solution] C scanf Format Error — How to Fix"
description: "Fix C scanf format specifier mismatches, buffer overflows, and input handling issues. Parse user input safely."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C scanf Format Error — How to Fix

The `scanf` family of functions can cause buffer overflows when %s is used without a width limit, and format mismatches when specifiers do not match argument types. Common mistakes include using %d for unsigned values, not checking the return value, and leaving unread characters in the input buffer which affects subsequent reads.

## Common Error Messages

- `scanf: stack buffer-overflow from unbounded %s`
- `scanf returns 0 — no items matched the format`
- `Leftover characters in input buffer after scanf`
- `scanf format '%d' expects int* but gets long*`

## How to Fix It

### Always use width specifiers with %s in scanf

```c
#include <stdio.h>

int main(void) {
    char name[32];
    int age;
    // WRONG: scanf("%s %d", name, &age);
    // CORRECT:
    if (scanf("%31s %d", name, &age) == 2) {
        printf("Name: %s, Age: %d\n", name, age);
    }
    return 0;
}
```

### Match format specifiers to correct pointer types

```c
#include <stdio.h>

int main(void) {
    int i;
    long l;
    float f;
    if (scanf("%d %ld %f", &i, &l, &f) == 3) {
        printf("int=%d long=%ld float=%f\n", i, l, f);
    }
    return 0;
}
```

### Clear input buffer after scanf

```c
#include <stdio.h>

void clear_stdin(void) {
    int c;
    while ((c = getchar()) != n && c != EOF);
}

int main(void) {
    int num;
    scanf("%d", &num);
    clear_stdin();
    char buf[128];
    fgets(buf, sizeof(buf), stdin);
    printf("Number: %d, String: %s\n", num, buf);
    return 0;
}
```

### Use fgets and strtol for safer input

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char buf[128];
    if (fgets(buf, sizeof(buf), stdin)) {
        char *end;
        long num = strtol(buf, &end, 10);
        if (end != buf) {
            printf("Parsed: %ld\n", num);
        } else {
            fprintf(stderr, "Invalid number\n");
        }
    }
    return 0;
}
```

## Common Scenarios

### Scenario 1: Using scanf with %s without width limit, causing buffer overflow on long input

This situation occurs when code fails to handle scanf format error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Not checking scanf return value and using uninitialized variables

In production environments, scanf format error can cause cascading failures. Implement proper error recovery and logging to diagnose issues quickly.

### Scenario 3: Mixing scanf and fgets without clearing the input buffer between them

When working with external libraries or system calls, scanf format error may surface unexpectedly. Always check errno or error codes after each operation.

## Prevent It

- **Tip 1:** Always specify a width limit like %31s in scanf to prevent buffer overflow
- **Tip 2:** Check scanf return value to ensure all expected fields were successfully parsed
- **Tip 3:** Consider fgets+strtol for more robust and controllable input parsing
