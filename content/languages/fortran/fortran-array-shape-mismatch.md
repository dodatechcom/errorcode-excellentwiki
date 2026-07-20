---
title: "[Solution] Fortran Array Shape Mismatch — Dimension Inconsistency"
description: "Fix Fortran array shape mismatch errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1044
---

An array shape mismatch occurs when an operation receives arrays with different dimensions or extents. Fortran compilers enforce shape agreement for element-wise operations and assignments.

## Common Causes

- Assigning an array of one shape to an array of a different shape
- Passing arrays with wrong dimensions to a subroutine
- Element-wise operations on arrays with different sizes
- Slicing an array with bounds that do not match the target

## How to Fix

### 1. Check array dimensions at compile time

```fortran
real :: a(3,3), b(3,3)
a = b  ! OK: same shape

real :: c(4,4)
a = c  ! ERROR: shape mismatch
```

### 2. Use assumed-shape arrays for flexibility

```fortran
subroutine process(arr)
  real, intent(in) :: arr(:,:)
  print *, size(arr,1), size(arr,2)
end subroutine
```

### 3. Use shape() or size() to verify before operations

```fortran
if (shape(a) /= shape(b)) then
  print *, 'Shape mismatch'
  stop
end if
```

### 4. Use reshape() to convert between shapes

```fortran
real :: flat(9), matrix(3,3)
flat = reshape(matrix, [9])
matrix = reshape(flat, [3,3])
```

### 5. Pass array sections with matching bounds

```fortran
call sub(a(1:3, 1:3))  ! matches expected (3,3) shape
```

## Examples

A common shape mismatch in a matrix multiply:

```fortran
program matrix_mul
  implicit none
  real :: A(2,3), B(3,2), C(2,2)
  A = 1.0
  B = 2.0
  C = matmul(A, B)  ! OK: (2,3) x (3,2) = (2,2)
  print *, C
end program
```

## Related Errors

- [Fortran Dimension Error](../fortran-dimension-error)
- [Fortran Allocatable Error](../fortran-allocatable-error)
- [Fortran Array Bounds](../fortran-array-bounds)
