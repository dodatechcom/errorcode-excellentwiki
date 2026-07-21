---
title: "[Solution] Fortran ENUM Error"
description: "Fix Fortran ENUM and ENUMERATOR errors when defining enumeration types."
languages: ["fortran"]
error-types: ["syntax-error"]
severities: ["error"]
---

ENUM errors occur when ENUM/ENUMERATOR declarations have syntax issues or when ENUM values conflict.

## Common Causes

- Missing ENUM, BIND(C) syntax
- Duplicate ENUMERATOR values
- ENUM not closed with END ENUM
- Using ENUM values incorrectly

## How to Fix

### 1. Use correct ENUM syntax

```fortran
enum, bind(c)
    enumerator :: red = 0
    enumerator :: green = 1
    enumerator :: blue = 2
end enum
```

### 2. Assign explicit values

```fortran
enum, bind(c)
    enumerator :: status_ok = 0
    enumerator :: status_error = -1
    enumerator :: status_warning = 1
end enum
```

## Examples

```fortran
program enum_demo
    implicit none
    enum, bind(c)
        enumerator :: low = 1
        enumerator :: medium = 2
        enumerator :: high = 3
    end enum
    integer :: level
    level = medium
    print *, 'Level:', level
end program
```

## Related Errors

- [Type mismatch](/languages/fortran/fortran-derived-type-error)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Syntax error](/languages/fortran/fortran-format-error)
