---
title: "[Solution] Fortran Elemental Function — Array-Compatible Functions"
description: "Fix elemental function errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1077
---

Elemental functions can be applied element-wise to arrays. Errors involve non-pure operations, side effects, or using elemental on functions that cannot be element-wise.

## Common Causes

- Using I/O or side effects inside an elemental function
- The function accesses global state that varies per element
- Using allocatable or pointer arguments (not allowed in elemental)
- The function has an assumed-shape argument (not allowed in elemental)

## How to Fix

### 1. Make elemental functions pure

```fortran
elemental function square(x) result(y)
  real, intent(in) :: x
  real :: y
  y = x ** 2
end function
```

### 2. No I/O or side effects

```fortran
! WRONG
elemental function bad(x) result(y)
  real, intent(in) :: x
  real :: y
  print *, x  ! I/O not allowed in elemental
  y = x
end function

! CORRECT
elemental function good(x) result(y)
  real, intent(in) :: x
  real :: y
  y = x
end function
```

### 3. Use with intent(in) only

```fortran
elemental function abs_val(x) result(y)
  real, intent(in) :: x
  real :: y
  y = abs(x)
end function
```

### 4. Apply to arrays directly

```fortran
real :: arr(10), result(10)
arr = [(real(i), i=1,10)]
result = square(arr)  ! applied element-wise
```

### 5. Combine elemental functions

```fortran
real :: arr(10)
arr = [(real(i), i=1,10)]
arr = sqrt(abs(arr - 5.0))  ! all elemental
```

## Examples

A complete elemental function module:

```fortran
module math elemental
  implicit none
contains
  elemental function clamp(x, lo, hi) result(y)
    real, intent(in) :: x, lo, hi
    real :: y
    y = max(lo, min(hi, x))
  end function

  elemental function sigmoid(x) result(y)
    real, intent(in) :: x
    real :: y
    y = 1.0 / (1.0 + exp(-x))
  end function
end module

program main
  use math_el elemental
  implicit none
  real :: vals(5) = [-2.0, -1.0, 0.0, 1.0, 2.0]
  print *, sigmoid(vals)
  print *, clamp(vals, -1.0, 1.0)
end program
```

## Related Errors

- [Fortran Pure Function](../fortran-pure-function)
- [Fortran Where](../fortran-where)
- [Fortran Subroutine](../fortran-subroutine)
