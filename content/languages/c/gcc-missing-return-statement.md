---
title: "[Solution] C MISSING_RETURN — Control reaches end of non-void function"
description: "Fix C control reaches end of non-void function warnings by adding return statements, noreturn attributes, and handling all error paths. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["compile-error"]
weight: 809
---

# C MISSING_RETURN — Control reaches end of non-void function

GCC warns when a function that is declared to return a value can reach the end of its body without executing a `return` statement. This leads to undefined behavior — the caller receives an indeterminate value.

## Common Causes

```c
// Cause 1: Missing return in a function with a return type
int get_value(int x) {
    if (x > 0) {
        return x * 2;
    }
    // no return here — warning: control reaches end of non-void function
}
```

```c
// Cause 2: All paths have return except one edge case
int classify(int x) {
    if (x < 0) return -1;
    if (x == 0) return 0;
    if (x > 0) return 1;
    // compiler doesn't know x must be one of these
}
```

```c
// Cause 3: Switch statement without default and not all cases covered
int get_day_type(int day) {
    switch (day) {
        case 0: return 1;  // Sunday
        case 6: return 1;  // Saturday
        case 1: case 2: case 3: case 4: case 5:
            return 0;      // weekday
        // no default — warning if day is outside 0-6
    }
}
```

```c
// Cause 4: Long function where return is only in some branches
const char* get_status(int code) {
    if (code == 200) {
        return "OK";
    } else if (code == 404) {
        return "Not Found";
    } else if (code == 500) {
        return "Server Error";
    }
    // no return for other codes — warning
}
```

```c
// Cause 5: Function with complex control flow
int process(int a, int b) {
    int result;
    if (a > 0) {
        result = a;
    }
    if (b > 0) {
        result = b;
    }
    return result;  // if both a <= 0 and b <= 0, result is uninitialized
    // Different warning, but related: result may be used uninitialized
}
```

## How to Fix

### Fix 1: Add a default return at the end

```c
int get_value(int x) {
    if (x > 0) {
        return x * 2;
    }
    return 0;  // default return value
}
```

### Fix 2: Use a default case or final return in switch statements

```c
int get_day_type(int day) {
    switch (day) {
        case 0: case 6:
            return 1;  // weekend
        case 1: case 2: case 3: case 4: case 5:
            return 0;  // weekday
        default:
            return -1;  // invalid day
    }
}
```

### Fix 3: Use __attribute__((noreturn)) for functions that never return

```c
#include <stdlib.h>

__attribute__((noreturn))
void fatal_error(const char *msg) {
    fprintf(stderr, "Fatal: %s\n", msg);
    exit(EXIT_FAILURE);
    // No return needed — attribute tells compiler this never returns
}

// In C11/N23:
#include <stdnoreturn.h>
noreturn void fatal_error(const char *msg) {
    fprintf(stderr, "Fatal: %s\n", msg);
    exit(EXIT_FAILURE);
}
```

### Fix 4: Restructure to ensure all paths return

```c
const char* get_status(int code) {
    if (code == 200) return "OK";
    if (code == 404) return "Not Found";
    if (code == 500) return "Server Error";
    return "Unknown";  // default for all other codes
}
```

### Fix 5: Initialize return variable before conditional paths

```c
int process(int a, int b) {
    int result = 0;  // initialize to a known default
    if (a > 0) {
        result = a;
    }
    if (b > 0) {
        result = b;
    }
    return result;
}
```

## Examples

```c
// Real-world: status code to string with full coverage
#include <stdio.h>

const char* http_status_text(int code) {
    switch (code) {
        case 200: return "OK";
        case 201: return "Created";
        case 204: return "No Content";
        case 301: return "Moved Permanently";
        case 304: return "Not Modified";
        case 400: return "Bad Request";
        case 401: return "Unauthorized";
        case 403: return "Forbidden";
        case 404: return "Not Found";
        case 500: return "Internal Server Error";
        case 502: return "Bad Gateway";
        case 503: return "Service Unavailable";
        default:  return "Unknown Status";
    }
}

int main(void) {
    printf("200: %s\n", http_status_text(200));
    printf("999: %s\n", http_status_text(999));
    return 0;
}
```

```c
// Real-world: recursive function that must return on all paths
int factorial(int n) {
    if (n <= 1) return 1;     // base case
    return n * factorial(n - 1);  // recursive case
    // All paths return — no warning
}
```

## Related Errors

- [C IMPLICIT_DECLARATION](/languages/c/gcc-implicit-declaration) — Implicit function declaration
- [C RETURN_LOCAL_ADDRESS](/languages/c/return-local-address) — Returning address of local variable
- [C MODIFY_CONST_OBJECT](/languages/c/modify-const-object) — Modifying const object UB
