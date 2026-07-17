---
title: "[Solution] Fortran: array subscript out of bounds"
description: "Fix Fortran errors when array indices exceed the declared bounds."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["array", "bounds", "subscript", "index", "out-of-range", "fortran"]
weight: 5
---

## What This Error Means

Fortran array subscript out of bounds occurs when an array index exceeds the declared upper or lower bounds. Fortran arrays can have custom bounds (not always starting at 1).

## Common Causes

- Index exceeds array upper bound
- Index below array lower bound
- Loop boundary miscalculation
- Off-by-one error
- Wrong array dimension accessed

## How to Fix

```fortran
! WRONG: Index exceeds bounds
program array_error
    implicit none
    integer :: arr(5)
    arr(10) = 42  ! Error: 10 > 5
end program
```

```fortran
! CORRECT: Check bounds before access
program array_safe
    implicit none
    integer :: arr(5), i
    do i = 1, 5
        arr(i) = i * 2
    end do
    print *, arr(5)  ! OK
end program
```

```fortran
! CORRECT: Use LBOUND and UBOUND
program bounds_check
    implicit none
    integer :: arr(3:7), i
    
    do i = LBOUND(arr, 1), UBOUND(arr, 1)
        arr(i) = i
    end do
    
    do i = LBOUND(arr, 1), UBOUND(arr, 1)
        print *, arr(i)
    end do
end program
```

```fortran
! CORRECT: Pass array bounds to subroutines
subroutine process_array(arr, n)
    implicit none
    integer, intent(in) :: n
    real, intent(in) :: arr(n)
    integer :: i
    
    do i = 1, n
        print *, arr(i)
    end do
end subroutine
```

```fortran
! CORRECT: Use assumed-shape arrays
module array_utils
    implicit none
contains
    subroutine print_arr(arr)
        real, intent(in) :: arr(:)
        integer :: i
        do i = 1, size(arr)
            print *, arr(i)
        end do
    end subroutine
end module
```

## Related Errors

- [Undefined Variable](fortran-undefined-variable-v2) - declaration errors
- [Allocate Error](fortran-allocate-error-v2) - memory allocation
- [Deallocate Error](fortran-deallocate-error-v2) - memory deallocation
