---
title: "[Solution] Fortran STOP Statement Error"
description: "Fix Fortran STOP statement errors when terminating program execution with optional status."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

STOP statement errors occur when STOP is used in contexts where it is not allowed or when the stop code is invalid.

## Common Causes

- STOP in pure procedure
- STOP in coarray program without handling all images
- STOP with invalid stop code
- STOP in interface block

## How to Fix

### 1. Use STOP appropriately

```fortran
stop 0  ! normal termination
stop 1  ! error termination
```

### 2. Do not use STOP in pure procedures

```fortran
! WRONG: STOP in pure
pure subroutine bad()
    stop 1  ! error!
end subroutine

! CORRECT: Use error return
subroutine good ierr)
    integer, intent(out) :: ierr
    ierr = 1  ! return error code
end subroutine
```

## Examples

```fortran
program stop_demo
    implicit none
    integer :: input
    print *, 'Enter a positive number:'
    read *, input
    if (input <= 0) then
        print *, 'Invalid input'
        stop 1
    end if
    print *, 'Input:', input
end program
```

## Related Errors

- [Runtime error](/languages/fortran/runtime-error11)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Error stop error](/languages/fortran/fortran-error-stop-error)
