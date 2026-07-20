---
title: "[Solution] Fortran Pure Function — Side-Effect-Free Functions"
description: "Fix pure function errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1078
---

Pure functions have no side effects and can be used in `do concurrent`, `forall`, and `pure` contexts. Errors involve modifying global state, using I/O, or calling impure functions from a pure one.

## Common Causes

- Modifying a module variable inside a pure function
- Using I/O (print, read, write) inside a pure function
- Calling an impure subroutine or function from within a pure function
- Using `save` attributes inside a pure function

## How to Fix

### 1. Only read intent(in) arguments

```fortran
pure function add(a, b) result(c)
  real, intent(in) :: a, b
  real :: c
  c = a + b
end function
```

### 2. No I/O or state modification

```fortran
! WRONG
pure function bad(x) result(y)
  real, intent(in) :: x
  real :: y
  print *, x  ! I/O not allowed
  y = x
end function
```

### 3. Use module variables only for constants

```fortran
module constants
  implicit none
  real, parameter :: PI = 3.14159265
end module

pure function circle_area(r) result(area)
  use constants
  real, intent(in) :: r
  real :: area
  area = PI * r**2  ! OK: PI is a parameter
end function
```

### 4. Pure functions can call other pure functions

```fortran
pure function square(x) result(y)
  real, intent(in) :: x
  real :: y
  y = x * x
end function

pure function sum_of_squares(a, b) result(s)
  real, intent(in) :: a, b
  real :: s
  s = square(a) + square(b)
end function
```

### 5. Use pure for elemental procedures

```fortran
pure function negate(x) result(y)
  real, intent(in) :: x
  real :: y
  y = -x
end function
```

## Examples

A library of pure functions:

```fortran
module math_lib
  implicit none
contains
  pure function factorial(n) result(f)
    integer, intent(in) :: n
    integer :: f
    integer :: i
    f = 1
    do i = 2, n
      f = f * i
    end do
  end function

  pure function gcd(a, b) result(g)
    integer, intent(in) :: a, b
    integer :: g, ta, tb
    ta = a; tb = b
    do while (tb /= 0)
      g = tb
      tb = mod(ta, tb)
      ta = g
    end do
    g = ta
  end function
end module
```

## Related Errors

- [Fortran Elemental Function](../fortran-elemental-function)
- [Fortran Do Concurrent](../fortran-do-concurrent)
- [Fortran Subroutine](../fortran-subroutine)
