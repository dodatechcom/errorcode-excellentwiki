---
title: "[Solution] Fortran FAILIMAGE Statement Error"
description: "Fix Fortran FAIL IMAGE statement errors when simulating image failure in coarray programs."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

FAIL IMAGE statement errors occur when FAIL IMAGE is used outside of error handling or without proper coarray context.

## Common Causes

- FAIL IMAGE outside critical error handling
- Using FAIL IMAGE in normal control flow
- Missing coarray support
- FAIL IMAGE not supported by compiler

## How to Fix

### 1. Use FAIL IMAGE only for unrecoverable errors

```fortran
if (corrupted_data) then
    fail image  ! simulate failure
end if
```

### 2. Check compiler support

```fortran
! Not all compilers support FAIL IMAGE
! Use with ERROR STOP as alternative
error stop 'Unrecoverable error'
```

## Examples

```fortran
program fail_image_demo
    implicit none
    integer :: status
    status = 0
    if (status /= 0) then
        print *, 'Simulating failure'
        ! fail image  ! if supported
        error stop 'Simulated failure'
    end if
    print *, 'Program complete'
end program
```

## Related Errors

- [Coarray error](/languages/fortran/fortran-coarray)
- [Runtime error](/languages/fortran/runtime-error11)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
