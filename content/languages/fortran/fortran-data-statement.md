---
title: "[Solution] Fortran Data Statement — Initialization Errors"
description: "Fix Fortran data statement errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1061
---

The `data` statement initializes variables at compile time. Errors involve mismatched types, re-initialization of variables, or using `data` with `allocatable` or `automatic` arrays.

## Common Causes

- Type mismatch between the variable and the data values
- Trying to use `data` with `allocatable` arrays
- Reinitializing a variable that was already initialized with `data`
- Wrong repeat count syntax in data values

## How to Fix

### 1. Match types in data statements

```fortran
integer :: a(5)
data a /1, 2, 3, 4, 5/  ! OK

real :: b(3)
data b /1.0, 2.0, 3.0/  ! OK
```

### 2. Use repeat syntax for repeated values

```fortran
integer :: arr(100)
data arr /100 * 0/  ! 100 zeros

character(len=20) :: names(5)
data names /5*' '/  ! 5 empty strings
```

### 3. Do not use data with allocatable arrays

```fortran
real, allocatable :: arr(:)
! data arr /1.0, 2.0, 3.0/  ! ERROR: allocatable not allowed
allocate(arr(3))
arr = [1.0, 2.0, 3.0]  ! use assignment instead
```

### 4. Use implied do for indexed initialization

```fortran
integer :: squares(5)
data (squares(i), i=1,5) /1, 4, 9, 16, 25/
```

### 5. Data with save for persistent initialization

```fortran
subroutine counter()
  integer n
  data n /0/
  save n  ! preserves value between calls
  n = n + 1
  print *, n
end subroutine
```

## Examples

Various data statement forms:

```fortran
program data_example
  implicit none
  integer :: a(3,3)
  real :: x(5)
  character(len=10) :: words(3)

  data a /1,2,3,4,5,6,7,8,9/  ! column-major fill
  data x /5*0.0/               ! five zeros
  data words /'hello', 'world', '!'/  ! character init

  print *, a
  print *, x
  print *, words
end program
```

## Related Errors

- [Fortran Parameter Attribute](../fortran-parameter-attribute)
- [Fortran Save Attribute](../fortran-save-attribute)
- [Fortran Implicit None Error](../fortran-implicit-none-error)
