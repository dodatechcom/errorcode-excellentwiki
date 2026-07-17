---
title: "[Solution] Fortran: allocation error - insufficient memory"
description: "Fix Fortran allocation errors when ALLOCATE statement fails due to insufficient memory or invalid parameters."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Fortran allocation errors occur when ALLOCATE fails, typically due to insufficient memory, invalid shape, or attempting to allocate already allocated arrays.

## Common Causes

- Requesting too much memory
- Array too large for available memory
- Allocating already allocated array
- Invalid array bounds
- Memory fragmentation

## How to Fix

```fortran
! WRONG: Not checking allocation status
program alloc_error
    implicit none
    real, allocatable :: big_array(:)
    allocate(big_array(1000000000))  ! May fail
    big_array = 0.0
end program
```

```fortran
! CORRECT: Check allocation status
program alloc_safe
    implicit none
    real, allocatable :: big_array(:)
    integer :: ios
    
    allocate(big_array(1000000), stat=ios)
    if (ios /= 0) then
        print *, 'Allocation failed'
        stop
    end if
    
    big_array = 0.0
    deallocate(big_array)
end program
```

```fortran
! CORRECT: Use STAT and ERRMSG
program alloc_detailed
    implicit none
    real, allocatable :: arr(:)
    integer :: ios
    character(len=256) :: errmsg
    
    allocate(arr(1000000), stat=ios, errmsg=errmsg)
    if (ios /= 0) then
        print *, 'Error:', trim(errmsg)
        stop
    end if
    
    deallocate(arr)
end program
```

```fortran
! CORRECT: Deallocate before reallocating
program realloc_safe
    implicit none
    real, allocatable :: arr(:)
    
    allocate(arr(100))
    arr = 1.0
    
    if (allocated(arr)) deallocate(arr)
    allocate(arr(200))
    arr = 2.0
    
    deallocate(arr)
end program
```

```fortran
! CORRECT: Check available memory
program check_memory
    implicit none
    integer :: max_size, ios
    real, allocatable :: arr(:)
    
    max_size = 1000000
    allocate(arr(max_size), stat=ios)
    
    do while (ios /= 0 .and. max_size > 0)
        max_size = max_size / 2
        allocate(arr(max_size), stat=ios)
    end do
    
    if (ios == 0) then
        print *, 'Allocated', max_size, 'elements'
        deallocate(arr)
    else
        print *, 'Cannot allocate memory'
    end if
end program
```

## Related Errors

- [Deallocate Error](fortran-deallocate-error-v2) - deallocation errors
- [Array Bounds](fortran-array-bounds-v2) - index errors
- [Out of Memory](/languages/assembly/asm-out-of-memory-v2) - memory failures
