---
title: "[Solution] Fortran Do Loop — Loop Construction Errors"
description: "Fix Fortran DO loop errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1128
---

DO loops provide iterative execution. Errors involve wrong loop bounds, missing END DO, or using DO WHILE when DO CONCURRENT was intended.

## Common Causes

- Loop variable modified inside the loop body
- Wrong step value (BY) causing infinite loop
- Missing END DO for block DO
- Loop variable declared with wrong kind (overflow)

## How to Fix

### 1. Use block DO with END DO

```fortran
do i = 1, 10
  print *, i
end do
```

### 2. Use DO WHILE for condition-based loops

```fortran
do while (n > 0)
  n = n / 2
end do
```

### 3. Check loop variable kind for large ranges

```fortran
integer(kind=4) :: i
do i = 1, 1000000
  ! ...
end do
```

### 4. Do not modify the loop variable

```fortran
do i = 1, 10
  ! do NOT assign to i here
end do
```

### 5. Use labeled DO for legacy code

```fortran
do 10 i = 1, 10
  print *, i
10 continue
```

## Examples

Nested DO loops:

```fortran
program do_demo
  implicit none
  integer :: i, j, mat(3,3)

  do i = 1, 3
    do j = 1, 3
      mat(i,j) = i * j
    end do
  end do

  do i = 1, 3
    print '(3I4)', mat(i,:)
  end do
end program
```

## Related Errors

- [Fortran Do Concurrent](../fortran-do-concurrent)
- [Fortran Forall](../fortran-forall)
- [Fortran Array Bounds](../fortran-array-bounds)
