---
title: "[Solution] C Macro Token Pasting Error — How to Fix"
description: "Fix C preprocessor token pasting errors with ## operator. Prevent unexpected concatenation and macro hygiene issues."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Macro Token Pasting Error — How to Fix

The ## operator in C preprocessor macros concatenates two tokens into a single token. Common errors include pasting tokens that do not form a valid identifier, unexpected results from macro argument expansion before pasting, and pasting with reserved identifiers. The # operator (stringification) and ## (token pasting) have different expansion rules that often cause confusion.

## Common Error Messages

- `undefined reference — invalid token pasting`
- `Macro pasting produces unexpected identifier`
- `Token pasting with ## creates reserved identifier`
- `Macro argument not expanded before ## pasting`

## How to Fix It

### Understand expansion order: arguments expand before ##

```c
#include <stdio.h>

#define PASTE(a, b) a ## b
#define MAKE_VAR(n) int var_ ## n = n

int main(void) {
    MAKE_VAR(1);
    MAKE_VAR(2);
    printf("var_1=%d var_2=%d\n", var_1, var_2);
    return 0;
}
```

### Use helper macros to avoid paste pitfalls

```c
#include <stdio.h>

#define CONCAT(a, b) CONCAT_(a, b)
#define CONCAT_(a, b) a ## b
#define STRINGIFY(x) STRINGIFY_(x)
#define STRINGIFY_(x) #x

int main(void) {
    int CONCAT(my, Variable) = 42;
    printf("%d\n", CONCAT(my, Variable));
    printf("%s\n", STRINGIFY(CONCAT(my, Variable)));
    return 0;
}
```

### Avoid pasting into reserved identifiers

```c
#include <stdio.h>

// WRONG: #define PREFIX_TEST 1  // starts with reserved prefix if _PREFIX is reserved
// CORRECT: use a unique macro namespace
#define MYPROJ_COUNTER 0
#define MYPROJ_MAKE_COUNTER(n) int MYPROJ_counter_##n = n

int main(void) {
    MYPROJ_MAKE_COUNTER(1);
    MYPROJ_MAKE_COUNTER(2);
    printf("%d %d\n", MYPROJ_counter_1, MYPROJ_counter_2);
    return 0;
}
```

### Use do { } while(0) for multi-statement macros to avoid paste issues

```c
#include <stdio.h>

#define SWAP_INTS(a, b) do { \
    int tmp_ ## a = a; \
    a = b; \
    b = tmp_ ## a; \
} while(0)

int main(void) {
    int x = 1, y = 2;
    SWAP_INTS(x, y);
    printf("x=%d y=%d\n", x, y);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Pasting tokens that form an invalid identifier, causing a compiler error

This situation occurs when code fails to handle macro paste error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Expecting macro arguments to be expanded before ## pasting — they are not

In production environments, macro paste error can cause cascading failures. Implement proper error recovery and logging to diagnose issues quickly.

### Scenario 3: Accidentally creating reserved identifiers through token pasting

When working with external libraries or system calls, macro paste error may surface unexpectedly. Always check errno or error codes after each operation.

## Prevent It

- **Tip 1:** Use an intermediate macro layer when you need arguments expanded before pasting
- **Tip 2:** Always wrap multi-statement macros in do { } while(0) to prevent paste-related bugs
- **Tip 3:** Name macro helper functions with unique prefixes to avoid collisions with reserved identifiers
