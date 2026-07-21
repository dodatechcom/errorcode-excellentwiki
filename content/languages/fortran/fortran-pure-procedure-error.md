---
title: "[Solution] Fortran PURE Procedure Error"
description: "Fix Fortran PURE procedure errors when declaring procedures with no side effects."
languages: ["fortran"]
error-types: ["compile-error"]
severities: ["error"]
---

PURE procedure errors occur when the PURE attribute is applied to procedures that perform I/O, modify global state, or have side effects.

## Common Causes

- PURE procedure doing I/O
- PURE procedure modifying global variables
- PURE procedure calling impure functions
- Missing PURE on elemental procedures

## How to Fix

### 1. Ensure no side effects

```fortran
pure function safe_add(a, b) result(c)
    real, intent(in) :: a, b
    real :: c
    c = a + b
end function
```

### 2. Remove I/O from PURE procedures

```fortran
! WRONG: I/O in PURE
pure subroutine bad_sub(x)
    real, intent(in) :: x
    print *, x  ! error!
end subroutine

! CORRECT: Pure computation only
pure function compute(x) result(y)
    real, intent(in) :: x
    real :: y
    y = x * 2.0
end function
```

## Examples

```fortran
program pure_demo
    implicit none
    real :: values(5)
    integer :: i
    values = [(real(i), i=1,5)]
    values = my_pure_func(values)
    print *, values
    contains
    pure function my_pure_func(arr) result(res)
        real, intent(in) :: arr(:)
        real :: res(size(arr))
        res = arr ** 2
    end function
end program
```

## Related Errors

- [Elemental function error](/languages/fortran/fortran-elemental-function)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Interface error](/languages/fortran/fortran-interface-error)
