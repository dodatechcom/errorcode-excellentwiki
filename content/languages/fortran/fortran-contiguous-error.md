---
title: "[Solution] Fortran CONTIGUOUS Attribute Error"
description: "Fix Fortran CONTIGUOUS attribute errors when requesting contiguous memory layout for arrays."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

CONTIGUOUS attribute errors occur when the CONTIGUOUS attribute is applied to arrays that cannot be made contiguous.

## Common Causes

- CONTIGUOUS on assumed-shape array that is not contiguous
- Pointer array assigned to non-contiguous source
- CONTIGUOUS with array sections that are not contiguous
- Missing CONTIGUOUS attribute for F2008+ assumptions

## How to Fix

### 1. Use CONTIGUOUS correctly

```fortran
! WRONG: Not all arrays can be made contiguous
subroutine process(arr)
    real, contiguous :: arr(:)  ! may fail

! CORRECT: Use when source is guaranteed contiguous
subroutine process(arr)
    real, contiguous :: arr(:)  ! if caller passes contiguous
```

### 2. Use reshape for non-contiguous data

```fortran
real :: non_contiguous(10,10)
real :: contiguous(100)
contiguous = reshape(non_contiguous, [100])
```

## Examples

```fortran
program contiguous_demo
    implicit none
    real, allocatable :: arr(:)
    allocate(arr(100))
    arr = 1.0
    call process_array(arr)
    deallocate(arr)
    contains
    subroutine process_array(a)
        real, contiguous :: a(:)
        print *, sum(a)
    end subroutine
end program
```

## Related Errors

- [Allocatable error](/languages/fortran/fortran-allocatable-error)
- [Pointer assignment error](/languages/fortran/fortran-pointer-assignment-error)
- [Runtime error](/languages/fortran/runtime-error11)
