---
title: "Format / format error"
description: "A format error occurs when a Fortran I/O statement encounters a mismatch between the format specification and the data being written or read."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A format error occurs when the format descriptor in a Fortran `read` or `write` statement does not match the data type or number of variables being formatted. This includes mismatched data types (e.g., using an integer format descriptor for a real variable), insufficient format descriptors for the number of variables, or malformed format strings.

## Common Causes

- Using `I` format descriptor for real variables (should use `F` or `E`)
- Providing fewer format descriptors than variables in the I/O list
- Malformed format strings with incorrect field widths or missing delimiters
- Using `A` format for non-character data

## How to Fix

```fortran
! WRONG: Integer format for real variable
program format_example
    implicit none
    real :: x
    x = 3.14159
    write(*, '(I10)') x       ! I format is for integers, not reals
end program

! CORRECT: Use F format for real variables
program format_example
    implicit none
    real :: x
    x = 3.14159
    write(*, '(F10.4)') x     ! F10.4 means 10-wide, 4 decimal places
end program
```

```fortran
! WRONG: Fewer descriptors than variables
program mismatch_example
    implicit none
    integer :: a, b, c
    a = 1; b = 2; c = 3
    write(*, '(I5)') a, b, c   ! only 1 descriptor for 3 variables
end program

! CORRECT: Match descriptors to variables
program mismatch_example
    implicit none
    integer :: a, b, c
    a = 1; b = 2; c = 3
    write(*, '(3I5)') a, b, c  ! 3 descriptors for 3 variables
end program
```

## Examples

```fortran
program format_error_demo
    implicit none
    character(len=20) :: name
    real :: value
    integer :: count

    name = 'test'
    value = 42.5
    count = 10

    ! ERROR: format does not match variable types
    write(*, '(A, I5, I5)') name, value, count
    ! 'I5' used for 'value' which is real - should be 'F5.1'

    ! ERROR: reading with wrong format
    read(*, '(A10)') count    ! A format is for characters, count is integer
end program
```

## Related Errors

- [I/O error](/languages/fortran/io-error3)
- [Undefined variable](/languages/fortran/undefined-variable)
