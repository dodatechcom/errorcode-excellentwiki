---
title: "Allocation error in Fortran"
description: "Allocation errors in Fortran occur when ALLOCATE fails due to insufficient memory or invalid allocation request."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["allocate", "dynamic-memory", "heap", "stat", "fortran"]
weight: 5
---

## What This Error Means

Fortran's ALLOCATE statement dynamically allocates heap memory for arrays. Allocation errors occur when the system cannot fulfill the request or the allocation parameters are invalid.

## Common Causes

- Requesting too much memory
- Allocating with invalid shape (negative size)
- Double allocation without deallocation
- STAT= not checked

## How to Fix

```fortran
! WRONG: No error check on allocate
program alloc_error
    implicit none
    real, allocatable :: arr(:)
    allocate(arr(1000000000))   ! May fail - too much memory
end program
```

```fortran
! CORRECT: Check STAT on allocate
program alloc_safe
    implicit none
    real, allocatable :: arr(:)
    integer :: ierr
    allocate(arr(1000), stat=ierr)
    if (ierr /= 0) then
        print *, 'Allocation failed with code:', ierr
        stop
    end if
    arr = 1.0
    deallocate(arr)
end program
```

## Examples

```fortran
program example
    implicit none
    integer, allocatable :: big_array(:)
    allocate(big_array(1000000000))   ! May cause allocation error
end program
```

## Related Errors

- [Deallocation Error](/languages/fortran/fortran-deallocate-error) - memory release errors
- [Array Bounds](/languages/fortran/array-bounds2) - index errors
