---
title: "[Solution] Fortran: deallocation of unallocated array"
description: "Fix Fortran errors when attempting to deallocate arrays that haven't been allocated."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["deallocate", "memory", "array", "allocated", "pointer", "fortran"]
weight: 5
---

## What This Error Means

Fortran deallocation errors occur when DEALLOCATE is called on an array that hasn't been allocated, or when attempting to deallocate already deallocated memory.

## Common Causes

- Deallocating unallocated array
- Double deallocation
- Missing ALLOCATE before DEALLOCATE
- Pointer array not allocated
- Error in allocation logic

## How to Fix

```fortran
! WRONG: Deallocating unallocated array
program dealloc_error
    implicit none
    real, allocatable :: arr(:)
    deallocate(arr)  ! Error: arr not allocated
end program
```

```fortran
! CORRECT: Check allocation status
program dealloc_safe
    implicit none
    real, allocatable :: arr(:)
    
    allocate(arr(100))
    arr = 1.0
    
    ! Always check before deallocating
    if (allocated(arr)) then
        deallocate(arr)
    end if
end program
```

```fortran
! CORRECT: Use ALLOCATED intrinsic
program alloc_check
    implicit none
    real, allocatable :: arr(:)
    
    print *, 'Before allocate:', allocated(arr)
    
    allocate(arr(100))
    print *, 'After allocate:', allocated(arr)
    
    deallocate(arr)
    print *, 'After deallocate:', allocated(arr)
end program
```

```fortran
! CORRECT: Safe deallocation wrapper
subroutine safe_dealloc(arr)
    implicit none
    real, allocatable, intent(inout) :: arr(:)
    
    if (allocated(arr)) then
        deallocate(arr)
    end if
end subroutine
```

```fortran
! CORRECT: Initialize pointers
program pointer_safe
    implicit none
    real, pointer :: ptr(:)
    
    nullify(ptr)  ! Initialize to null
    
    allocate(ptr(100))
    ptr = 1.0
    
    if (associated(ptr)) then
        deallocate(ptr)
    end if
end program
```

```fortran
! CORRECT: Use error handling
program error_handling
    implicit none
    real, allocatable :: arr(:)
    integer :: ios
    
    allocate(arr(100), stat=ios)
    if (ios /= 0) then
        print *, 'Allocation failed'
        stop
    end if
    
    arr = 1.0
    
    ! Use SAFE DEALLOCATE macro or function
    if (allocated(arr)) then
        deallocate(arr, stat=ios)
        if (ios /= 0) then
            print *, 'Deallocation failed'
        end if
    end if
end program
```

## Related Errors

- [Allocate Error](fortran-allocate-error-v2) - allocation errors
- [Array Bounds](fortran-array-bounds-v2) - index errors
- [Undefined Variable](fortran-undefined-variable-v2) - declaration errors
