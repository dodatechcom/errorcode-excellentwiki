---
title: "Format error in Fortran"
description: "Format errors in Fortran occur when the format specification doesn't match the data being read or written."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["format", "read", "write", "specification", "fortran"]
weight: 5
---

## What This Error Means

Fortran uses format specifications (FORMAT statements or inline formats) to control I/O. A format error occurs when the format doesn't match the data type, count, or layout.

## Common Causes

- Reading string into integer variable
- Format has fewer descriptors than variables
- Wrong format for data type (e.g., I format for real)
- Mismatched parentheses in format

## How to Fix

```fortran
! WRONG: Format mismatch
program fmt_error
    implicit none
    integer :: x
    read(*, '(A)') x   ! Reading string into integer
end program
```

```fortran
! CORRECT: Matching format
program fmt_safe
    implicit none
    integer :: x
    character(len=20) :: str
    read(*, '(I5)') x        ! Integer format
    read(*, '(A)') str        ! String format for strings
end program
```

## Examples

```fortran
program example
    implicit none
    real :: pi
    pi = 3.14159
    write(*, '(I5)') pi    ! Error: I format for real number
    write(*, '(F5.2)') pi  ! Correct: F format for real
end program
```

## Related Errors

- [I/O Error](/languages/fortran/fortran-io-error) - file operation errors
- [End of File](/languages/fortran/fortran-end-of-file) - EOF errors
