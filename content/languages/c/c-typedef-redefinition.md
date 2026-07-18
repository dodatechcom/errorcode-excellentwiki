---
title: "[Solution] C Typedef Redefinition Error — How to Fix"
description: "Fix C typedef redefinition errors when including headers multiple times or defining types in multiple files."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Typedef Redefinition Error — How to Fix

In C, you cannot redefine a typedef to a different type within the same translation unit. Common causes include including a header that typedefs a name and then redefining it, multiple headers defining the same typedef independently, and missing include guards. C11 allows compatible typedef redefinitions, but C99 does not.

## Common Error Messages

- `error: redefinition of typedef — conflicting types`
- `typedef redefinition with different underlying type`
- `multiple definition of typedef from repeated include`
- `conflicting types for typedef name`

## How to Fix It

### Use include guards to prevent multiple typedef definitions

```c
#ifndef TYPES_H
#define TYPES_H
typedef int my_int_t;
typedef struct { int x; int y; } Point;
#endif
```

### Use unique typedef names with project prefixes

```c
#ifndef PROJECT_TYPES_H
#define PROJECT_TYPES_H
typedef int proj_count_t;
typedef struct { double x; double y; } proj_vec2_t;
#endif
```

### Use struct tags instead of typedef

```c
struct Point {
    int x;
    int y;
};
struct Point p1 = {1, 2};
typedef struct Point Point;
```

### Use compatibility typedefs

```c
#ifndef MY_TYPES_H
#define MY_TYPES_H
#include <stdint.h>
typedef int32_t proj_int32_t;
typedef uint64_t proj_uint64_t;
#endif
```

## Common Scenarios

### Scenario 1: Including two headers that both typedef the same name to different types

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Redefining a typedef in the same file after including a header that defines it

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Not using include guards, causing the same typedef to be defined multiple times

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Use include guards on every header to prevent multiple typedef definitions
- **Tip 2:** Use project-specific prefixes for all typedef names to avoid collisions
- **Tip 3:** Prefer struct tags over typedefs for types that may be defined in multiple contexts
