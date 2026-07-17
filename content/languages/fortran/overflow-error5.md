---
title: "Arithmetic overflow"
description: "An arithmetic overflow occurs when a computation produces a value that exceeds the range of the data type."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An arithmetic overflow occurs when the result of an integer or fixed-point arithmetic operation exceeds the maximum (or falls below the minimum) value that the data type can represent. In Fortran, integer overflow wraps around silently on most platforms, but compilers with overflow checking enabled will raise a runtime error. Floating-point overflow produces `Infinity`.

## Common Causes

- Multiplying large integers without using a wider data type
- Accumulating values in a loop that exceed the type's range
- Implicit type promotion issues between `integer(kind=4)` and `integer(kind=8)`
- Converting a large `real` value to a smaller integer type

## How to Fix

```fortran
! WRONG: Using default integer for large computation
program overflow_example
    implicit none
    integer :: i, result
    result = 1
    do i = 1, 20
        result = result * i    ! overflows default 32-bit integer at 13!
    end do
    print *, '20! =', result
end program

! CORRECT: Use a wider integer kind
program overflow_example
    implicit none
    integer(kind=8) :: i, result
    result = 1_8
    do i = 1, 20
        result = result * i    ! fits in 64-bit integer
    end do
    print *, '20! =', result
end program
```

```fortran
! WRONG: Implicit narrowing conversion
subroutine narrow_convert(big_val)
    integer(kind=8), intent(in) :: big_val
    integer :: small_val
    small_val = int(big_val)   ! may overflow if big_val > 2^31 - 1
end subroutine

! CORRECT: Validate range before converting
subroutine narrow_convert(big_val)
    integer(kind=8), intent(in) :: big_val
    integer :: small_val
    if (big_val > huge(0) .or. big_val < -huge(0)) then
        print *, 'Error: value too large for default integer'
        return
    end if
    small_val = int(big_val)
end subroutine
```

## Examples

```fortran
program overflow_demo
    implicit none
    integer :: a, b, c

    ! Integer overflow
    a = 2000000000
    b = 2000000000
    c = a + b                ! overflows 32-bit integer: wraps to negative

    print *, a, '+', b, '=', c
    ! Output: 2000000000 + 2000000000 = -294967296 (wrong!)

    ! Floating-point overflow
    print *, huge(0.0) * 2.0  ! produces +Infinity

end program
```

## Related Errors

- [Floating point division by zero](/languages/fortran/division-zero8)
- [Runtime error](/languages/fortran/runtime-error11)
