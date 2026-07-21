---
title: "[Solution] Fortran VALUE Attribute Error"
description: "Fix Fortran VALUE attribute errors when passing arguments by value instead of reference."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

VALUE attribute errors occur when VALUE is used with arrays or when the passed value does not match the expected type.

## Common Causes

- VALUE on array argument (not allowed)
- VALUE with INTENT(OUT) (copy-out cannot return)
- VALUE mismatch between declaration and call
- VALUE on character arguments of wrong length

## How to Fix

### 1. Use VALUE for scalar arguments only

```fortran
subroutine add_one(x)
    integer, value :: x
    x = x + 1
    print *, x
end subroutine
```

### 2. Do not use VALUE with INTENT(OUT)

```fortran
! WRONG: VALUE with INTENT(OUT)
subroutine bad_sub(x)
    integer, value, intent(out) :: x
    x = 10  ! changes local copy, not original
end subroutine

! CORRECT: Use VALUE with intent(in) or no intent
subroutine good_sub(x)
    integer, value :: x
    x = x + 1  ! modifies local copy
end subroutine
```

## Examples

```fortran
program value_demo
    implicit none
    integer :: a
    a = 5
    call increment(a)
    print *, 'After:', a
    contains
    subroutine increment(n)
        integer, value :: n
        n = n + 1
        print *, 'Inside:', n
    end subroutine
end program
```

## Related Errors

- [Intent error](/languages/fortran/fortran-intent-error)
- [Subroutine argument error](/languages/fortran/fortran-subroutine-argument)
- [Runtime error](/languages/fortran/runtime-error11)
