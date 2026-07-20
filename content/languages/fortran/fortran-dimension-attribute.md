---
title: "[Solution] Fortran Dimension Attribute — Array Declaration Errors"
description: "Fix Fortran dimension attribute errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1045
---

The `dimension` attribute declares the shape and bounds of an array. Errors arise from mismatched bounds, using dimension with non-array variables, or conflicting declarations.

## Common Causes

- Declaring an array with dimension and then re-declaring with different bounds
- Using `dimension` with a type that also has an explicit array syntax
- Conflicting `dimension` and `allocatable` without `::` separator
- Using assumed-size (`*`) in a context where assumed-shape is needed

## How to Fix

### 1. Use consistent array declaration syntax

```fortran
! These are equivalent
real :: a(10)
real, dimension(10) :: a

! But do not mix them in the same declaration
real :: a(10), dimension(10) :: b  ! WRONG
```

### 2. Use explicit bounds when needed

```fortran
real, dimension(-5:5) :: centered
real, dimension(0:9) :: indexed
```

### 3. Combine dimension with intent and other attributes

```fortran
subroutine process(arr)
  real, dimension(:,:), intent(in) :: arr
  print *, size(arr,1), size(arr,2)
end subroutine
```

### 4. Use assumed-shape for procedure arguments

```fortran
subroutine mat_add(a, b, c)
  real, dimension(:,:), intent(in) :: a, b
  real, dimension(:,:), intent(out) :: c
  c = a + b
end subroutine
```

### 5. Check bounds with lbound and ubound

```fortran
program check_bounds
  implicit none
  real :: arr(3,4)
  print *, lbound(arr), ubound(arr)
  ! Prints: 1 1  3 4
end program
```

## Examples

Correct dimension usage in a subroutine:

```fortran
subroutine fill_matrix(m)
  real, dimension(:,:), intent(out) :: m
  integer :: i, j
  do i = 1, size(m,1)
    do j = 1, size(m,2)
      m(i,j) = real(i * j)
    end do
  end do
end subroutine
```

## Related Errors

- [Fortran Array Shape Mismatch](../fortran-array-shape-mismatch)
- [Fortran Allocatable Error](../fortran-allocatable-error)
- [Fortran Intent Error](../fortran-intent-error)
