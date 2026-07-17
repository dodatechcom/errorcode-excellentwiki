---
title: "[Solution] Fortran: format specification error"
description: "Fix Fortran errors when format specifications don't match the data being read or written."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["format", "specification", "read", "write", "i-o", "fortran"]
weight: 5
---

## What This Error Means

Format specification errors occur when the format descriptor doesn't match the data type, count, or layout. Common with FORMAT statements, inline formats, and namelist I/O.

## Common Causes

- Wrong format for data type (e.g., I for real)
- Format has fewer descriptors than variables
- Mismatched parentheses in format
- Reading string into numeric variable
- Incorrect repeat count

## How to Fix

```fortran
! WRONG: Format mismatch
program format_error
    implicit none
    integer :: x
    read(*, '(A)') x   ! Reading string into integer
end program
```

```fortran
! CORRECT: Matching format
program format_safe
    implicit none
    integer :: x
    character(len=20) :: str
    read(*, '(I5)') x        ! Integer format
    read(*, '(A)') str        ! String format
end program
```

```fortran
! CORRECT: Use list-directed I/O (free format)
program list_directed
    implicit none
    integer :: a, b
    real :: x, y
    
    read(*, *) a, b, x, y  ! No format needed
    print *, a, b, x, y
end program
```

```fortran
! CORRECT: Format with repeat counts
program format_repeat
    implicit none
    integer :: i, arr(5)
    
    ! Write 5 integers with I4 format
    write(*, '(5I4)') arr
    
    ! Or use repeat
    write(*, '(5(I4))') arr
end program
```

```fortran
! CORRECT: Complex format specifications
program complex_format
    implicit none
    real :: pi, e
    character(len=20) :: name
    
    pi = 3.14159265
    e = 2.71828183
    name = 'MATLAB'
    
    ! F format for reals, A for strings
    write(*, '(A, F8.4, A, F8.4)') name, pi, ' and ', e
end program
```

```fortran
! CORRECT: Namelist I/O
program namelist_example
    implicit none
    integer :: n
    real :: x, y
    namelist /params/ n, x, y
    
    n = 10
    x = 1.5
    y = 2.5
    
    write(*, nml=params)
end program
```

## Related Errors

- [I/O Error](fortran-io-error-v2) - file operation errors
- [End of File](fortran-end-of-file-v2) - EOF errors
- [Runtime Error](fortran-runtime-error-v2) - general runtime
