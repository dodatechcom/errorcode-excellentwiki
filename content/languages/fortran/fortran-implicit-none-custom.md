---
title: "[Solution] Fortran Implicit None — Forgetting Type Declarations"
description: "Fix Fortran implicit none errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1069
---

`implicit none` disables Fortran's default typing rules (I-N = integer, else real). Without it, typos in variable names create silent bugs because undeclared variables get a default type.

## Common Causes

- Forgetting `implicit none` at the top of a program unit
- Placing `implicit none` after variable declarations (too late)
- Typos in variable names that silently create new variables
- Missing `implicit none` in a module or submodule

## How to Fix

### 1. Always start with implicit none

```fortran
program myprog
  implicit none  ! first statement after program/module/subroutine
  integer :: x
  real :: y
end program
```

### 2. Place it in every program unit

```fortran
module mymod
  implicit none
  integer :: public_var
contains
  subroutine mysub()
    implicit none  ! also needed in each contained subprogram
    integer :: local
  end subroutine
end module
```

### 3. Use implicit double precision for legacy code

```fortran
implicit double precision (a-h, o-z)
implicit integer (i-n)
```

### 4. Check compiler warnings for implicit typing

```bash
gfortran -Wimplicit -c myprog.f90
```

### 5. Use IDE support to verify all variables are declared

```bash
# Use fortls (Fortran Language Server) for real-time checking
```

## Examples

Proper implicit none usage:

```fortran
module utils
  implicit none
  private
  public :: add, multiply

contains

  function add(a, b) result(c)
    real, intent(in) :: a, b
    real :: c
    c = a + b
  end function

  function multiply(a, b) result(c)
    real, intent(in) :: a, b
    real :: c
    c = a * b
  end function

end module
```

## Related Errors

- [Fortran Module Error](../fortran-module-error)
- [Fortran Kind Parameter](../fortran-kind-parameter)
- [Fortran Undefined Variable](../fortran-undefined-variable)
