---
title: "[Solution] Fortran Kind Parameter — Precision Selection"
description: "Fix Fortran kind parameter errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1070
---

Kind parameters specify the precision of numeric types. Errors involve wrong kind values, platform-dependent kind numbers, or using `selected_int_kind` / `selected_real_kind` incorrectly.

## Common Causes

- Hardcoding kind numbers (e.g., `real(8)`) that differ across compilers
- Using a kind value that does not exist on the target platform
- Mixing kinds in arithmetic operations
- Using wrong kind for I/O format

## How to Fix

### 1. Use selected_real_kind for portable precision

```fortran
integer, parameter :: dp = selected_real_kind(15, 307)
real(kind=dp) :: x
x = 1.0_dp  ! suffix matches kind
```

### 2. Use selected_int_kind for integer precision

```fortran
integer, parameter :: i64 = selected_int_kind(15)
integer(kind=i64) :: big
big = 1000000000000000_i64
```

### 3. Use kind with literals to avoid mixing

```fortran
integer, parameter :: sp = kind(1.0)
integer, parameter :: dp = kind(1.0d0)

real(kind=sp) :: a = 1.0_sp
real(kind=dp) :: b = 2.0_dp
! a + b  ! WARNING: mixed kinds
b = real(a, kind=dp)  ! explicit conversion
```

### 4. Check available kinds at runtime

```fortran
print *, 'Real kinds:', selected_real_kind(6), selected_real_kind(15)
print *, 'Int kind:', selected_int_kind(9)
```

### 5. Use iso_fortran_env for kind constants

```fortran
use iso_fortran_env
print *, real32, real64, int32, int64
```

## Examples

A precision-portable module:

```fortran
module precision_mod
  implicit none
  integer, parameter :: sp = selected_real_kind(6, 37)
  integer, parameter :: dp = selected_real_kind(15, 307)
  integer, parameter :: qp = selected_real_kind(33, 4931)

  integer, parameter :: i32 = selected_int_kind(9)
  integer, parameter :: i64 = selected_int_kind(18)
end module

program main
  use precision_mod
  implicit none
  real(kind=dp) :: x = 1.0_dp
  real(kind=qp) :: y = 2.0_qp
  print *, x + y
end program
```

## Related Errors

- [Fortran ISO Fortran Env](../fortran-iso-fortran-env)
- [Fortran Selected Int Kind](../fortran-selected-int-kind)
- [Fortran Parameter Attribute](../fortran-parameter-attribute)
