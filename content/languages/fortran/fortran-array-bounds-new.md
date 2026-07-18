---
title: "[Solution] Fortran: array bounds exceeded or subscript out of range"
description: "Fix Fortran array bounds errors by validating indices and using LBOUND and UBOUND functions."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Fortran array bounds exceeded errors occur when a program attempts to access an array element using an index that falls outside the declared bounds. Fortran arrays can have custom lower and upper bounds, not necessarily starting at 1. When an out-of-bounds access occurs, the program may crash, produce incorrect results, or silently corrupt memory depending on compiler settings. Runtime bounds checking is not enabled by default in most Fortran compilers, making this a particularly insidious class of bug.

## Why It Happens

Array bounds errors in Fortran typically result from off-by-one mistakes in loop boundaries. A loop that iterates from 1 to N+1 when the array has N elements will access one element beyond the declared size. Incorrect calculations of array indices, such as using a formula that produces negative values or values exceeding the upper bound, are another common cause. When passing arrays to subroutines, the assumed size may not match the actual array, leading to accesses beyond the real bounds. Allocatable arrays that are not properly allocated before use can cause bounds violations. Multi-dimensional array indexing mistakes, particularly when mixing Fortran's column-major ordering, also frequently trigger these errors.

## How to Fix It

**Check loop boundaries against array bounds:**

```fortran
! WRONG: loop exceeds array bounds
program bounds_error
    implicit none
    integer :: arr(5), i
    do i = 1, 6
        arr(i) = i * 2  ! Error when i = 6
    end do
end program

! CORRECT: use size or UBOUND
program bounds_safe
    implicit none
    integer :: arr(5), i
    do i = 1, size(arr)
        arr(i) = i * 2
    end do
end program
```

**Use LBOUND and UBOUND for custom-bounded arrays:**

```fortran
program custom_bounds
    implicit none
    integer :: arr(-3:3), i
    do i = LBOUND(arr, 1), UBOUND(arr, 1)
        arr(i) = i
    end do
    ! Safe iteration using actual bounds
    do i = LBOUND(arr, 1), UBOUND(arr, 1)
        print *, i, arr(i)
    end do
end program
```

**Pass array bounds explicitly to subroutines:**

```fortran
subroutine process(arr, n)
    implicit none
    integer, intent(in) :: n
    real, intent(in) :: arr(n)
    integer :: i
    do i = 1, n
        print *, arr(i)
    end do
end subroutine

program main
    implicit none
    real :: data(10)
    call process(data, 10)
end program
```

**Enable runtime bounds checking during development:**

```bash
# GFortran
gfortran -fcheck=all -o myprog source.f90

# Intel Fortran
ifort -check bounds -o myprog source.f90

# Disable for production
gfortran -O2 -o myprog source.f90
```

**Use assumed-shape arrays with Fortran 2003+:**

```fortran
module array_utils
    implicit none
contains
    subroutine print_array(arr)
        real, intent(in) :: arr(:)
        integer :: i
        do i = 1, size(arr)
            print *, arr(i)
        end do
    end subroutine
end module
```

## Common Mistakes

- Assuming arrays always start at index 1 when using custom lower bounds
- Forgetting that Fortran passes arrays by reference, so modifying indices affects the caller
- Not allocating allocatable arrays before use
- Mixing up array dimensions when using multi-dimensional arrays
- Using hardcoded loop limits instead of querying array size

## Related Pages

- [Undefined variable in Fortran](/languages/fortran/fortran-undefined-variable-v2)
- [Memory allocation failed in Fortran](/languages/fortran/fortran-allocate-error-v2)
- [Deallocate failed in Fortran](/languages/fortran/fortran-deallocate-error-v2)
- [Floating point overflow in Fortran](/languages/fortran/fortran-overflow-v2)
