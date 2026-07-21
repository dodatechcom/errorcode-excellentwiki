---
title: "[Solution] Fortran VALUE Attribute Intent Error"
description: "Fix Fortran VALUE attribute with INTENT conflicts when passing arguments by value."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

VALUE with INTENT conflicts occur when combining VALUE with INTENT(OUT), which prevents returning values to the caller.

## Common Causes

- VALUE with INTENT(OUT) not returning changes
- VALUE with INTENT(IN) when modification needed
- Missing VALUE causing reference issues
- VALUE on intent(out) dummy argument

## How to Fix

### 1. Use VALUE with intent(in) only

```fortran
subroutine scale(x, factor)
    real, value, intent(in) :: x
    real, intent(in) :: factor
    print *, x * factor
end subroutine
```

### 2. Do not use VALUE with INTENT(OUT)

```fortran
! WRONG
subroutine broken(x)
    integer, value, intent(out) :: x
    x = 10  ! only changes local copy
end subroutine

! CORRECT: Use reference for output
subroutine working(x)
    integer, intent(out) :: x
    x = 10  ! changes original
end subroutine
```

## Examples

```fortran
program value_intent_demo
    implicit none
    integer :: a
    a = 5
    call show_value(a)
    print *, 'Original:', a
    contains
    subroutine show_value(n)
        integer, value :: n
        n = n + 1
        print *, 'Modified:', n
    end subroutine
end program
```

## Related Errors

- [Value attribute error](/languages/fortran/fortran-value-attribute-error)
- [Intent error](/languages/fortran/fortran-intent-error)
- [Runtime error](/languages/fortran/runtime-error11)
