---
title: "[Solution] Fortran ENTRY Statement Error"
description: "Fix Fortran ENTRY statement errors when defining multiple entry points in a subroutine."
languages: ["fortran"]
error-types: ["syntax-error"]
severities: ["error"]
---

ENTRY statement errors occur when ENTRY is used in the wrong context or when entry points have incompatible argument lists.

## Common Causes

- ENTRY in main program unit
- ENTRY arguments not matching usage
- ENTRY before contains statement
- Using ENTRY with recursive procedures

## How to Fix

### 1. Use ENTRY in subroutines only

```fortran
subroutine main_proc(a, b)
    integer, intent(in) :: a
    integer, intent(out) :: b
    b = a * 2
    entry sub_proc(x)
    ! entry point with different args
end subroutine
```

### 2. Declare entry point arguments

```fortran
subroutine compute(x, y)
    real, intent(in) :: x
    real, intent(out) :: y
    y = x ** 2
    entry square(z)
    ! z is implicitly declared
end subroutine
```

## Examples

```fortran
program entry_demo
    implicit none
    integer :: result
    call main_sub(5, result)
    print *, 'Result:', result
    contains
    subroutine main_sub(n, out)
        integer, intent(in) :: n
        integer, intent(out) :: out
        out = n * 10
    end subroutine
end program
```

## Related Errors

- [Subroutine error](/languages/fortran/subroutine)
- [Interface error](/languages/fortran/fortran-interface-error)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
