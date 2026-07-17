---
title: "Runtime error"
description: "A runtime error is a general error that occurs during program execution due to invalid operations, unhandled conditions, or resource limitations."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A runtime error is a broad category of errors that occur while the program is executing, as opposed to compile-time or link-time errors. In Fortran, runtime errors include conditions like invalid input, unhandled edge cases, resource exhaustion, and violated program assumptions. They are typically caught by the runtime system and reported with an error message and line number.

## Common Causes

- Invalid numeric operations (e.g., square root of a negative number)
- Uninitialized variables used in computations
- Array index out of bounds (detected by runtime bounds checking)
- Division by zero or overflow in arithmetic expressions

## How to Fix

```fortran
! WRONG: No error handling for invalid input
program runtime_example
    implicit none
    real :: x, y
    print *, 'Enter a number:'
    read(*, *) x
    y = sqrt(x)           ! runtime error if x is negative
    print *, 'Square root:', y
end program

! CORRECT: Validate input before operations
program runtime_example
    implicit none
    real :: x, y
    print *, 'Enter a number:'
    read(*, *) x
    if (x < 0.0) then
        print *, 'Error: cannot take square root of negative number'
        stop
    end if
    y = sqrt(x)
    print *, 'Square root:', y
end program
```

```fortran
! WRONG: No bounds checking in subroutine
subroutine process(n, arr)
    integer, intent(in) :: n
    real :: arr(n)
    real :: sum
    integer :: i
    sum = 0.0
    do i = 1, n + 1          ! off-by-one: goes past array end
        sum = sum + arr(i)    ! runtime error on last iteration
    end do
    print *, 'Sum:', sum
end subroutine

! CORRECT: Use correct bounds
subroutine process(n, arr)
    integer, intent(in) :: n
    real :: arr(n)
    real :: sum
    integer :: i
    sum = 0.0
    do i = 1, n               ! correct upper bound
        sum = sum + arr(i)
    end do
    print *, 'Sum:', sum
end subroutine
```

## Examples

```fortran
program runtime_error_example
    implicit none
    integer :: i, j, result
    real :: x, y

    ! Runtime error: uninitialized variable
    i = j + 1               ! j was never assigned a value
    print *, i

    ! Runtime error: negative argument to sqrt
    x = -4.0
    y = sqrt(x)             ! domain error - runtime error

    ! Runtime error: division by zero
    result = 100 / (i - j)  ! i - j could be zero

end program
```

## Related Errors

- [Array bounds exceeded](/languages/fortran/array-bounds2)
- [Floating point division by zero](/languages/fortran/division-zero8)
- [Arithmetic overflow](/languages/fortran/overflow-error5)
