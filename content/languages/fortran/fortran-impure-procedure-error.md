---
title: "[Solution] Fortran IMPURE Procedure Error"
description: "Fix Fortran IMPURE procedure errors when declaring procedures that may have side effects."
languages: ["fortran"]
error-types: ["compile-error"]
severities: ["error"]
---

IMPURE procedure errors occur when procedures are not properly declared as IMPURE when they have side effects.

## Common Causes

- Impure procedure called in PURE context
- Missing IMPURE declaration for side-effect procedures
- IMPURE procedure in DO CONCURRENT
- Calling impure from elemental procedure

## How to Fix

### 1. Declare procedures with side effects as IMPURE

```fortran
impure subroutine log_message(msg)
    character(len=*), intent(in) :: msg
    print *, msg  ! side effect: I/O
end subroutine
```

### 2. Do not call IMPURE from PURE contexts

```fortran
! WRONG: Impure call in pure function
pure function bad(x) result(y)
    real, intent(in) :: x
    real :: y
    call log_message('computing')  ! error!
    y = x * 2.0
end function
```

## Examples

```fortran
program impure_demo
    implicit none
    call write_log('Starting program')
    call write_log('Program complete')
    contains
    impure subroutine write_log(msg)
        character(len=*), intent(in) :: msg
        print *, 'LOG:', msg
    end subroutine
end program
```

## Related Errors

- [Pure procedure error](/languages/fortran/fortran-pure-procedure-error)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Interface error](/languages/fortran/fortran-interface-error)
