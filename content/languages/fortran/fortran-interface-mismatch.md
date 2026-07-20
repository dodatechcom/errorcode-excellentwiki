---
title: "[Solution] Fortran Interface Mismatch — Procedure Interface Errors"
description: "Fix Fortran interface mismatch errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1051
---

An interface mismatch occurs when a procedure is called with arguments that do not match the declared interface. This can be an explicit interface block or the implicit interface from the procedure's definition.

## Common Causes

- Wrong number of arguments in the call vs the interface
- Type, kind, or shape mismatch between actual and dummy arguments
- Intent violation (passing expression to intent(inout) argument)
- Missing interface block for external procedures

## How to Fix

### 1. Write an explicit interface block

```fortran
interface
  subroutine process(arr, n)
    real, intent(in) :: arr(:)
    integer, intent(in) :: n
  end subroutine
end interface
```

### 2. Make sure argument types match exactly

```fortran
subroutine compute(x, y)
  real, intent(in) :: x
  real, intent(out) :: y
  y = x * 2.0
end subroutine

! Call with matching types
call compute(1.0, result)
```

### 3. Check array shape in interface

```fortran
interface
  function dot(a, b) result(d)
    real, intent(in) :: a(:), b(:)
    real :: d
  end function
end interface
```

### 4. Use module procedures for automatic interfaces

```fortran
module math
contains
  function add(a, b) result(c)
    real, intent(in) :: a, b
    real :: c
    c = a + b
  end function
end module

! No interface block needed; use math, only: add
```

### 5. Verify intent matches between declaration and call

```fortran
! If the callee declares intent(in), do not pass a literal
subroutine f(x)
  real, intent(inout) :: x
  x = x + 1
end subroutine

call f(1.0)  ! ERROR: literal to intent(inout)
call f(var)  ! OK
```

## Examples

A complete interface block:

```fortran
module vectors
  implicit none
contains
  function vec_dot(a, b, n) result(d)
    integer, intent(in) :: n
    real, intent(in) :: a(n), b(n)
    real :: d
    integer :: i
    d = 0.0
    do i = 1, n
      d = d + a(i) * b(i)
    end do
  end function
end module

program main
  use vectors
  implicit none
  real :: x(3), y(3)
  x = [1.0, 2.0, 3.0]
  y = [4.0, 5.0, 6.0]
  print *, vec_dot(x, y, 3)
end program
```

## Related Errors

- [Fortran Generic Interface](../fortran-generic-interface)
- [Fortran Subroutine Error](../fortran-subroutine)
- [Fortran Intent Error](../fortran-intent-attribute)
