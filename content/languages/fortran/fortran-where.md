---
title: "[Solution] Fortran Where — Masked Array Assignment"
description: "Fix Fortran where errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1076
---

`where` assigns values to array elements that satisfy a condition. Errors involve mismatched array shapes, using where on non-arrays, or mixing scalar and array operations incorrectly.

## Common Causes

- The mask and target arrays have different shapes
- Using where on a scalar instead of an array
- The elsewhere clause references a different-shaped array
- Using where when an elemental function would be cleaner

## How to Fix

### 1. Ensure arrays have matching shapes

```fortran
real :: a(3,3), b(3,3)
where (a > 0.0)
  b = log(a)  ! OK: same shape
end where
```

### 2. Use where with scalar constants

```fortran
real :: arr(10)
where (arr < 0.0)
  arr = 0.0  ! scalar to array
end where
```

### 3. Use elsewhere for the complement

```fortran
real :: arr(10)
where (arr > 0.0)
  arr = log(arr)
elsewhere
  arr = 0.0
end where
```

### 4. Nested where for multiple conditions

```fortran
real :: arr(10)
where (arr > 10.0)
  arr = 10.0
elsewhere (arr < -10.0)
  arr = -10.0
end where
```

### 5. Use where as a function (Fortran 2003)

```fortran
real :: arr(10), result(10)
result = where(arr > 0.0, arr, 0.0)
```

## Examples

Clipping and normalizing:

```fortran
program where_demo
  implicit none
  real :: data(10)
  integer :: i

  data = [(real(i) - 5.0, i=1,10)]

  ! Clip to [-3, 3]
  where (data > 3.0)
    data = 3.0
  elsewhere (data < -3.0)
    data = -3.0
  end where

  print *, data
end program
```

## Related Errors

- [Fortran Elemental Function](../fortran-elemental-function)
- [Fortran Array Shape Mismatch](../fortran-array-shape-mismatch)
- [Fortran Forall](../fortran-forall)
