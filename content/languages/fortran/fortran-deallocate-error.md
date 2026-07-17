---
title: "Deallocation error in Fortran"
description: "Deallocation errors in Fortran occur when DEALLOCATE fails, often due to double deallocation or invalid pointer."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Fortran's DEALLOCATE statement releases dynamically allocated memory. Errors occur when trying to deallocate memory that's already been freed, was never allocated, or has an invalid status.

## Common Causes

- Double deallocation of same variable
- Deallocating an unallocated variable
- Deallocating with wrong shape
- Memory corruption before deallocation

## How to Fix

```fortran
! WRONG: Double deallocation
program dealloc_error
    implicit none
    integer, allocatable :: arr(:)
    allocate(arr(100))
    deallocate(arr)
    deallocate(arr)   ! Error: already deallocated
end program
```

```fortran
! CORRECT: Check allocation status before deallocating
program dealloc_safe
    implicit none
    integer, allocatable :: arr(:)
    allocate(arr(100))
    if (allocated(arr)) deallocate(arr)
    ! Safe to call again
    if (allocated(arr)) deallocate(arr)   ! No-op
end program
```

## Examples

```fortran
program example
    implicit none
    integer, allocatable :: x(:)
    ! x is not allocated
    deallocate(x)   ! Error: deallocate of unallocated variable
end program
```

## Related Errors

- [Allocation Error](/languages/fortran/fortran-allocate-error) - memory allocation errors
- [Runtime Error](/languages/fortran/runtime-error11) - general runtime errors
