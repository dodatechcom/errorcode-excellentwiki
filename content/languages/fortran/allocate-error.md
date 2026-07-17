---
title: "Allocation error"
description: "An allocation error occurs when a Fortran program fails to allocate memory for a dynamic array or deferred-length variable."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An allocation error occurs when the Fortran `allocate` statement fails to obtain memory for a dynamic array or deferred-length variable. This can happen due to insufficient memory, requesting an excessively large allocation, or allocating the same variable twice without deallocating it first (memory leak leading to exhaustion).

## Common Causes

- Requesting more memory than is available (e.g., very large array sizes)
- Double allocation without prior `deallocate` (memory leak)
- Allocating with invalid or negative size expressions
- Repeated allocations in loops without matching deallocations

## How to Fix

```fortran
! WRONG: Double allocation without deallocation
program alloc_example
    implicit none
    integer, allocatable :: arr(:)
    allocate(arr(1000))
    allocate(arr(2000))    ! ERROR: arr is already allocated
end program

! CORRECT: Deallocate before reallocating
program alloc_example
    implicit none
    integer, allocatable :: arr(:)
    allocate(arr(1000))
    deallocate(arr)
    allocate(arr(2000))    ! now safe
    deallocate(arr)
end program
```

```fortran
! WRONG: Not checking allocation success
program unsafe_alloc
    implicit none
    real, allocatable :: big_array(:)
    allocate(big_array(1000000000))  ! may fail - no error check
    big_array = 0.0
end program

! CORRECT: Use STAT= to check for allocation failure
program safe_alloc
    implicit none
    real, allocatable :: big_array(:)
    integer :: ierr
    allocate(big_array(1000000000), stat=ierr)
    if (ierr /= 0) then
        print *, 'Allocation failed, ierr =', ierr
        stop
    end if
    big_array = 0.0
    deallocate(big_array)
end program
```

## Examples

```fortran
program alloc_error_example
    implicit none
    integer, allocatable :: matrix(:,:)
    integer :: n, ierr

    ! Trying to allocate with a negative size (from bad calculation)
    n = -100
    allocate(matrix(n, n), stat=ierr)
    if (ierr /= 0) then
        print *, 'Allocation failed for size', n
    end if

    ! Memory leak: allocating in a loop without deallocating
    do n = 1, 10000
        allocate(matrix(n, n))   ! previous allocation leaked
    end do

    ! Eventually fails with allocation error due to memory exhaustion
end program
```

## Related Errors

- [Array bounds exceeded](/languages/fortran/array-bounds2)
- [Runtime error](/languages/fortran/runtime-error11)
