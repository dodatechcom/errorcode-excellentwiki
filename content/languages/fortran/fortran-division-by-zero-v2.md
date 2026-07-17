---
title: "[Solution] Fortran: division by zero"
description: "Fix Fortran errors when dividing by zero in integer or real arithmetic."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["division", "zero", "arithmetic", "floating-point", "integer", "fortran"]
weight: 5
---

## What This Error Means

Fortran division by zero occurs when dividing an integer or real value by zero. This is undefined mathematically and causes a runtime exception.

## Common Causes

- Divisor variable is zero
- Uninitialized divisor
- Missing zero-check
- Array element is zero
- Function returns zero

## How to Fix

```fortran
! WRONG: No zero check
program div_error
    implicit none
    integer :: a, b, result
    a = 10
    b = 0
    result = a / b  ! Division by zero
end program
```

```fortran
! CORRECT: Check before dividing
program div_safe
    implicit none
    integer :: a, b, result
    a = 10
    b = 0
    
    if (b /= 0) then
        result = a / b
        print *, 'Result:', result
    else
        print *, 'Error: Division by zero'
    end if
end program
```

```fortran
! CORRECT: Use function with error checking
function safe_divide(a, b) result(res)
    implicit none
    real, intent(in) :: a, b
    real :: res
    
    if (abs(b) < epsilon(0.0)) then
        res = 0.0  ! Or handle error
        return
    end if
    
    res = a / b
end function
```

```fortran
! CORRECT: Check array elements
program array_div
    implicit none
    real :: data(5)
    integer :: i
    
    data = (/ 1.0, 2.0, 0.0, 4.0, 5.0 /)
    
    do i = 1, 5
        if (data(i) /= 0.0) then
            print *, 1.0 / data(i)
        else
            print *, 'Skipping zero at index', i
        end if
    end do
end program
```

```fortran
! CORRECT: Use epsilon for floating point comparison
program float_div
    implicit none
    real :: a, b
    a = 1.0
    b = 0.0
    
    if (abs(b) > epsilon(0.0)) then
        print *, a / b
    else
        print *, 'Divisor too small'
    end if
end program
```

## Related Errors

- [Array Bounds](fortran-array-bounds-v2) - index errors
- [Runtime Error](fortran-runtime-error-v2) - general runtime
- [Allocate Error](fortran-allocate-error-v2) - memory errors
