---
title: "[Solution] Fortran Selected Int Kind — Integer Precision"
description: "Fix selected_int_kind errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1071
---

`selected_int_kind(r)` returns a kind parameter for integers that can represent at least `10^r`. Errors involve requesting a precision that does not exist or using the result incorrectly.

## Common Causes

- Requesting a kind that the platform does not support
- Using the result of `selected_int_kind` directly without storing in a parameter
- Mixing integer kinds in arithmetic
- Overflow when the kind is insufficient for the value

## How to Fix

### 1. Store the result in a named parameter

```fortran
integer, parameter :: i64 = selected_int_kind(15)
integer(kind=i64) :: big_number
```

### 2. Check if the kind exists

```fortran
integer :: k
k = selected_int_kind(20)
if (k == -1) then
  print *, 'Kind not available'
  stop
end if
```

### 3. Use appropriate kind for your values

```fortran
! For values up to ~2 billion: kind 4 or selected_int_kind(9)
! For values up to ~9e18: kind 8 or selected_int_kind(18)
integer, parameter :: i32 = selected_int_kind(9)
integer, parameter :: i64 = selected_int_kind(18)
```

### 4. Use kind suffix on literals

```fortran
integer(kind=i64) :: n = 1000000000_i64
```

### 5. Convert between kinds explicitly

```fortran
integer(kind=i32) :: a = 100
integer(kind=i64) :: b
b = int(a, kind=i64)
```

## Examples

Portable integer kind selection:

```fortran
program int_kinds
  implicit none
  integer, parameter :: k1 = selected_int_kind(4)   ! up to 9999
  integer, parameter :: k2 = selected_int_kind(9)   ! up to 2e9
  integer, parameter :: k3 = selected_int_kind(18)  ! up to 9e18

  integer(kind=k1) :: small = 1234_k1
  integer(kind=k2) :: medium = 1000000000_k2
  integer(kind=k3) :: large = 1000000000000000000_k3

  print *, small, medium, large
end program
```

## Related Errors

- [Fortran Kind Parameter](../fortran-kind-parameter)
- [Fortran ISO Fortran Env](../fortran-iso-fortran-env)
- [Fortran Parameter Attribute](../fortran-parameter-attribute)
