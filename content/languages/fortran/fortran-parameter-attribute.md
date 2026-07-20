---
title: "[Solution] Fortran Parameter Attribute — Named Constants"
description: "Fix Fortran parameter attribute errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1049
---

The `parameter` attribute declares a named constant that cannot be modified. Errors involve trying to assign to a parameter, using parameters with wrong types, or forgetting `parameter` in `double precision` declarations.

## Common Causes

- Attempting to modify a `parameter` variable
- Using `double precision` without `parameter` for the `double precision` keyword itself
- Type mismatch: integer parameter used where real is expected
- Using `parameter` with `intent` (not allowed for dummy arguments)

## How to Fix

### 1. Declare parameters with the correct type

```fortran
integer, parameter :: MAX_SIZE = 100
real, parameter :: PI = 3.14159265358979
character(len=*), parameter :: VERSION = "1.0"
```

### 2. Do not try to modify parameters

```fortran
integer, parameter :: N = 10
N = 20  ! ERROR: cannot assign to parameter
```

### 3. Use parameters for array bounds and constants

```fortran
program example
  implicit none
  integer, parameter :: DIM = 3
  real :: mat(DIM, DIM)
  mat = 0.0
  print *, DIM
end program
```

### 4. Double precision with parameter

```fortran
! WRONG for Fortran 77 compatibility
double precision :: pi
parameter (pi = 3.14159265358979d0)

! CORRECT modern syntax
real(kind=kind(0.0d0)), parameter :: pi = 3.14159265358979d0
```

### 5. Use parameters for string lengths

```fortran
integer, parameter :: MAX_LEN = 256
character(len=MAX_LEN) :: line
```

## Examples

A physics constants module:

```fortran
module constants
  implicit none
  real, parameter :: PI = acos(-1.0)
  real, parameter :: E = exp(1.0)
  real, parameter :: c = 2.99792458e8  ! speed of light
  real, parameter :: h = 6.62607015e-34  ! Planck constant
  real, parameter :: k_B = 1.380649e-23  ! Boltzmann constant
end module
```

## Related Errors

- [Fortran Data Statement](../fortran-data-statement)
- [Fortran Implicit None Error](../fortran-implicit-none-error)
- [Fortran Kind Parameter](../fortran-kind-parameter)
