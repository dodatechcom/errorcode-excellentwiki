---
title: "[Solution] Fortran ERROR STOP Error"
description: "Fix Fortran ERROR STOP statement errors when terminating program with error status."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

ERROR STOP errors occur when the error code is not a valid integer or when ERROR STOP is used in contexts where it is not allowed.

## Common Causes

- ERROR STOP with invalid error code
- ERROR STOP in pure procedure
- ERROR STOP in coarray without image handling
- Missing error code parameter

## How to Fix

### 1. Use valid error codes

```fortran
error stop 1  ! positive integer error code
```

### 2. Provide descriptive message

```fortran
error stop 'Fatal: invalid input'
```

## Examples

```fortran
program error_stop_demo
    implicit none
    integer :: status
    status = 0
    if (status /= 0) then
        error stop 'Error condition detected'
    end if
    print *, 'Program completed normally'
end program
```

## Related Errors

- [Runtime error](/languages/fortran/runtime-error11)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Stop statement error](/languages/fortran/fortran-subroutine)
