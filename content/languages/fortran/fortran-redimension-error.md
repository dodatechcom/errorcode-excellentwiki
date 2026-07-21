---
title: "[Solution] Fortran REDIMENSION Error"
description: "Fix Fortran REDIMENSION realloc errors when resizing allocatable arrays."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

REDIMENSION realloc errors occur when allocatable arrays are resized without proper deallocation or when the new size is invalid.

## Common Causes

- REDIMENSION on non-allocatable array
- Negative size in REDIMENSION
- REDIMENSION without matching DEALLOCATE
- REDIMENSION in readonly context

## How to Fix

### 1. Use allocatable arrays properly

```fortran
! WRONG: Static array cannot be redimensioned
integer :: arr(10)
! arr = integer :: arr(20)  ! error

! CORRECT: Use allocatable
integer, allocatable :: arr(:)
allocate(arr(10))
! Later:
deallocate(arr)
allocate(arr(20))
```

### 2. Check allocation status

```fortran
integer, allocatable :: arr(:)
if (.not. allocated(arr)) then
    allocate(arr(100))
end if
```

## Examples

```fortran
program redimension_demo
    implicit none
    integer, allocatable :: data(:)
    integer :: i
    allocate(data(5))
    data = [1, 2, 3, 4, 5]
    print *, 'Size:', size(data)
    deallocate(data)
    allocate(data(10))
    data = 0
    print *, 'New size:', size(data)
    deallocate(data)
end program
```

## Related Errors

- [Allocatable error](/languages/fortran/fortran-allocatable-error)
- [Array bounds error](/languages/fortran/array-bounds)
- [Runtime error](/languages/fortran/runtime-error11)
