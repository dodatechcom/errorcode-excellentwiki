---
title: "Floating point division by zero"
description: "A floating point division by zero occurs when a Fortran program divides a real or complex number by zero."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A floating point division by zero occurs when a Fortran program divides a `real` or `complex` value by zero. Unlike integer division by zero, floating-point division by zero may produce `Infinity` or `NaN` depending on the compiler and runtime settings, but many Fortran compilers trap on this condition by default, causing a runtime error.

## Common Causes

- Divisor variable not initialized or accidentally set to zero
- Denormalized floating-point values that underflow to zero
- Missing validation of computed denominators before division
- Incorrect formula causing a zero denominator under specific input conditions

## How to Fix

```fortran
! WRONG: Dividing without checking denominator
program div_example
    implicit none
    real :: x, y, result
    x = 1.0
    y = 0.0
    result = x / y          ! floating point division by zero
end program

! CORRECT: Check denominator before dividing
program div_example
    implicit none
    real :: x, y, result
    x = 1.0
    y = 0.0
    if (abs(y) < tiny(y)) then
        print *, 'Error: denominator is too small'
        result = huge(result)  ! or handle appropriately
    else
        result = x / y
    end if
    print *, 'Result:', result
end program
```

```fortran
! WRONG: Dividing by a computed value without validation
subroutine compute(a, b, c, result)
    real, intent(in) :: a, b, c
    real, intent(out) :: result
    result = a / (b - c)    ! if b == c, division by zero
end subroutine

! CORRECT: Validate the computed denominator
subroutine compute(a, b, c, result)
    real, intent(in) :: a, b, c
    real, intent(out) :: result
    real :: denom
    denom = b - c
    if (abs(denom) < epsilon(1.0)) then
        print *, 'Warning: near-zero denominator'
        result = 0.0
    else
        result = a / denom
    end if
end subroutine
```

## Examples

```fortran
program div_zero_example
    implicit none
    real :: values(5)
    real :: average, sum
    integer :: i, count

    values = (/ 1.0, 2.0, 3.0, 4.0, 5.0 /)
    count = 0
    sum = 0.0

    ! BUG: count is never incremented, so division by zero occurs
    do i = 1, 5
        if (values(i) > 10.0) then
            sum = sum + values(i)
            ! count = count + 1  <-- missing line
        end if
    end do

    average = sum / real(count)  ! count is 0 - division by zero
    print *, 'Average:', average
end program
```

## Related Errors

- [Arithmetic overflow](/languages/fortran/overflow-error5)
- [Runtime error](/languages/fortran/runtime-error11)
