---
title: "[Solution] C Stringify Error — How to Fix"
description: "Fix C preprocessor stringification errors with the # operator. Convert macro arguments to strings correctly in C."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Stringify Error — How to Fix

The # operator in the C preprocessor converts a macro argument into a string literal. Common errors include stringifying before macro expansion, using # with variadic macro arguments, and forgetting that # produces a string literal not a variable. The argument is stringified at the point of the # operator, so intermediate macro expansions may not behave as expected.

## Common Error Messages

- `Stringify produces unexpected result — argument not expanded`
- `Stringify with variadic macro gives wrong result`
- `Number becomes string literal from # operator`
- `Undefined behavior from stringify on empty macro argument`

## How to Fix It

### Use helper macro for stringification to ensure proper expansion

```c
#include <stdio.h>

#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)

int main(void) {
    int x = 42;
    printf("%s\n", TOSTRING(x));      // prints "x"
    printf("%s\n", TOSTRING(42));     // prints "42"
    printf("%s\n", TOSTRING(x + 1)); // prints "x + 1"
    return 0;
}
```

### Stringify macro values with TOSTRING helper

```c
#include <stdio.h>

#define VERSION_MAJOR 1
#define VERSION_MINOR 2
#define VERSION_PATCH 3

#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)

#define VERSION_STRING TOSTRING(VERSION_MAJOR) "." TOSTRING(VERSION_MINOR) "." TOSTRING(VERSION_PATCH)

int main(void) {
    printf("Version: %s\n", VERSION_STRING);
    return 0;
}
```

### Stringify with variadic macros using __VA_ARGS__

```c
#include <stdio.h>

#define LOG(msg, ...) printf("[" __FILE__ ":%d] " msg "\n", __LINE__, ##__VA_ARGS__)

int main(void) {
    LOG("Hello %s", "world");
    LOG("Count: %d", 42);
    return 0;
}
```

### Stringify in debug macros

```c
#include <stdio.h>

#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)
#define ASSERT(cond) \
    do { \
        if (!(cond)) { \
            fprintf(stderr, "ASSERT failed: %s at %s:%d\n", #cond, __FILE__, __LINE__); \
        } \
    } while(0)

int main(void) {
    int x = 5;
    ASSERT(x == 5);
    ASSERT(x == 10);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Stringifying a macro that has not been expanded first, producing the macro name instead of its value

This situation occurs when code fails to handle stringify error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using # with an empty macro argument, which produces an empty string on some compilers

In production environments, stringify error can cause cascading failures. Implement proper error recovery and logging to diagnose issues quickly.

### Scenario 3: Expecting stringification to produce a quoted string — it produces a string literal already

When working with external libraries or system calls, stringify error may surface unexpectedly. Always check errno or error codes after each operation.

## Prevent It

- **Tip 1:** Use a two-level macro (TOSTRING wrapping STRINGIFY) to ensure arguments are expanded before stringification
- **Tip 2:** Remember that # produces a string literal — no quotes are needed around the result
- **Tip 3:** Test stringification output with different macro expansion scenarios to avoid surprises
