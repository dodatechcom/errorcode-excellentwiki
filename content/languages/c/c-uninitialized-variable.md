---
title: "[Solution] C Uninitialized Variable Error — How to Fix"
description: "Fix C uninitialized variable bugs causing undefined behavior. Initialize all variables before use."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Uninitialized Variable Error — How to Fix

Using uninitialized variables is undefined behavior. Local variables are not auto-initialized and contain stack garbage. Common causes include no initialization, conditional paths missing init, and relying on zero-init for locals.

## Common Error Messages

- `Use of uninitialized value`
- `Conditional jump depends on uninitialized value`
- `uninitialized variable used in expression`
- `indirection of non-pointer`

## How to Fix It

### Initialize at declaration

```c
#include <stdio.h>

int main(void) {
    int x = 0;
    double d = 0.0;
    char buf[16] = {0};
    int *p = NULL;
    printf("x=%d d=%f\n", x, d);
    return 0;
}
```

### Initialize in all branches

```c
#include <stdio.h>

int main(void) {
    int result;
    int mode = 2;
    if (mode == 1) result = 100;
    else if (mode == 2) result = 200;
    else result = 0;
    printf("result=%d\n", result);
    return 0;
}
```

### Enable compiler warnings

```bash
gcc -Wall -Wextra -Wuninitialized -o program program.c
```

### Use memset for structs

```c
#include <string.h>
typedef struct { int x; int y; double z; } Point;
int main(void) { Point p; memset(&p, 0, sizeof(p)); return 0; }
```

## Common Scenarios

### Scenario 1: Local variable used without initialization after conditional

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Array elements accessed in a loop that misses indices

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Struct member used when only some members were assigned

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Initialize every variable at declaration
- **Tip 2:** Compile with -Wall -Wextra -Wuninitialized
- **Tip 3:** Use -Werror to make warnings into errors
