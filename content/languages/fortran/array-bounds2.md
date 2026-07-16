---
title: "Array bounds exceeded"
description: "An array bounds error occurs when a Fortran program attempts to access an element outside the declared bounds of an array."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["array", "bounds", "index-out-of-range"]
weight: 5
---

## What This Error Means

Fortran arrays have fixed bounds declared at compile time. When code attempts to access an index that falls outside the declared range (either below the lower bound or above the upper bound), a runtime error occurs. This is a common source of bugs in numerical and scientific code.

## Common Causes

- Off-by-one errors in loop bounds
- Using uncorrected loop indices after nested loops
- Passing incorrect dimensions to subroutines
- Hardcoding array sizes instead of using declared bounds

## How to Fix

```fortran
! WRONG: Loop goes one past the declared upper bound
program array_bounds
    implicit none
    integer :: arr(10)
    integer :: i
    do i = 1, 11
        arr(i) = i * 2       ! arr(11) is out of bounds
    end do
end program

! CORRECT: Use declared bounds
program array_bounds
    implicit none
    integer :: arr(10)
    integer :: i
    do i = 1, size(arr)       ! size() returns declared size
        arr(i) = i * 2
    end do
end program
```

```fortran
! WRONG: Hardcoded bounds in subroutine
subroutine fill_array(arr, n)
    integer, intent(in) :: n
    integer :: arr(n)
    integer :: i
    do i = 1, 100             ! hardcoded, may exceed n
        arr(i) = i
    end do
end subroutine

! CORRECT: Use the passed dimension
subroutine fill_array(arr, n)
    integer, intent(in) :: n
    integer :: arr(n)
    integer :: i
    do i = 1, n               ! matches actual size
        arr(i) = i
    end do
end subroutine
```

## Examples

```fortran
program array_bounds_example
    implicit none
    integer, parameter :: N = 5
    integer :: matrix(N, N)
    integer :: i, j

    ! Accessing row beyond declared bound
    do i = 1, N + 1
        do j = 1, N
            matrix(i, j) = i + j   ! error when i > N
        end do
    end do

end program
```

## Related Errors

- [I/O error](/languages/fortran/io-error3)
- [Allocation error](/languages/fortran/allocate-error)
