---
title: "[Solution] Fortran Do Concurrent — Concurrent Loop Errors"
description: "Fix do concurrent errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1074
---

`do concurrent` (Fortran 2008) tells the compiler iterations are independent and can be parallelized. Errors involve hidden dependencies between iterations or using non-concurrent-safe operations inside the loop.

## Common Causes

- Accumulating into a shared variable (race condition)
- Using I/O inside the loop (not safe for concurrent execution)
- Calling a subroutine with side effects on shared state
- The loop body modifies an index variable

## How to Fix

### 1. Make iterations truly independent

```fortran
real :: a(100), b(100), c(100)
c = 0.0

! WRONG: shared accumulation
do concurrent (i = 1:100)
  c(1) = c(1) + a(i) * b(i)  ! race condition on c(1)
end do

! CORRECT: local accumulation
do concurrent (i = 1:100)
  c(i) = a(i) * b(i)  ! each iteration writes to its own element
end do
```

### 2. Avoid I/O inside do concurrent

```fortran
! WRONG
do concurrent (i = 1:100)
  print *, i  ! not safe
end do

! CORRECT
do concurrent (i = 1:100)
  result(i) = compute(i)  ! pure computation
end do
```

### 3. Use local variables for reduction

```fortran
real :: total
total = 0.0
! Use a regular do for reductions
do i = 1, 100
  total = total + data(i)
end do
```

### 4. Use pure functions inside the loop

```fortran
pure function square(x) result(y)
  real, intent(in) :: x
  real :: y
  y = x ** 2
end function

do concurrent (i = 1:100)
  result(i) = square(data(i))
end do
```

### 5. Check compiler support

```bash
# GCC
gfortran -floop-nest-optimize do_concurrent.f90

# Intel
ifort -qopenmp do_concurrent.f90
```

## Examples

Parallel matrix initialization:

```fortran
program concurrent_demo
  implicit none
  real :: mat(100,100)
  integer :: i, j

  do concurrent (i = 1:100, j = 1:100)
    mat(i,j) = real(i * j)
  end do

  print *, sum(mat)
end program
```

## Related Errors

- [Fortran Do Loop Error](../fortran-do-loop-error)
- [Fortran Co Array Error](../fortran-coarray)
- [Fortran Pure Function](../fortran-pure-function)
