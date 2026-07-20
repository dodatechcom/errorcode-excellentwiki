---
title: "[Solution] Fortran Forall — Forall Construct Errors"
description: "Fix forall errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["warning"]
weight: 1075
---

`forall` is an array assignment construct that specifies all assignments happen conceptually simultaneously. Errors involve side effects, non-array assignments, or using forall when elemental operations would be clearer.

## Common Causes

- Using forall with scalar operations (use regular assignment instead)
- Side effects between forall indices (undefined behavior)
- Using forall when array syntax would be simpler
- Forall with a mask that causes undefined results

## How to Fix

### 1. Use forall for array element assignments

```fortran
real :: a(10), b(10)
forall (i = 1:10)
  a(i) = b(10 - i + 1)  ! reverse
end forall
```

### 2. Avoid side effects in forall

```fortran
! WRONG: j depends on previous i
forall (i = 1:10)
  a(i) = func(a(i-1))  ! undefined if i-1 was modified
end forall
```

### 3. Use array syntax instead of forall when possible

```fortran
! forall equivalent
a(1:10) = b(10:1:-1)

! This is the same and usually clearer
```

### 4. Use forall with masks carefully

```fortran
forall (i = 1:10, a(i) > 0.0)
  a(i) = log(a(i))
end forall
```

### 5. Use nested forall for multi-dimensional arrays

```fortran
real :: mat(3,3)
forall (i = 1:3, j = 1:3)
  mat(i,j) = real(i + j)
end forall
```

## Examples

Forall for matrix operations:

```fortran
program forall_demo
  implicit none
  real :: a(3,3), b(3,3)
  integer :: i, j

  ! Initialize
  forall (i=1:3, j=1:3)
    a(i,j) = real(i*3 + j)
  end forall

  ! Transpose
  forall (i=1:3, j=1:3)
    b(i,j) = a(j,i)
  end forall

  print *, 'A:'
  print *, a
  print *, 'B (transpose):'
  print *, b
end program
```

## Related Errors

- [Fortran Do Loop Error](../fortran-do-loop-error)
- [Fortran Elemental Function](../fortran-elemental-function)
- [Fortran Do Concurrent](../fortran-do-concurrent)
