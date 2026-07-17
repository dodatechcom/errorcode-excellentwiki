---
title: "[Solution] Fortran: namelist read error"
description: "Fix Fortran namelist I/O errors when reading or writing namelist groups with invalid data or formatting."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["namelist", "i-o", "read", "write", "format", "fortran"]
weight: 5
---

## What This Error Means

Fortran namelist errors occur when reading or writing namelist groups with incorrect syntax, missing delimiters, or data type mismatches.

## Common Causes

- Missing ampersand (&) delimiters
- Variable not in namelist group
- Data type mismatch
- Invalid value format
- Missing or extra variables

## How to Fix

```fortran
! WRONG: Missing namelist syntax
program namelist_error
    implicit none
    integer :: n
    real :: x
    namelist /params/ n, x
    
    ! Reading without proper format
    read(*, *) n, x  ! Not namelist format
end program
```

```fortran
! CORRECT: Proper namelist syntax
program namelist_safe
    implicit none
    integer :: n
    real :: x
    namelist /params/ n, x
    
    ! Write namelist
    n = 10
    x = 3.14
    write(*, nml=params)
    
    ! Read namelist
    rewind(*)
    read(*, nml=params)
    print *, n, x
end program
```

```fortran
! CORRECT: Namelist file format
! params.nml file content:
! &params
!   n = 10
!   x = 3.14
! /

program namelist_file
    implicit none
    integer :: n
    real :: x
    namelist /params/ n, x
    
    open(10, file='params.nml', status='old')
    read(10, nml=params)
    close(10)
    
    print *, 'n =', n
    print *, 'x =', x
end program
```

```fortran
! CORRECT: Handle namelist errors
program namelist_error_handling
    implicit none
    integer :: n, ios
    real :: x
    namelist /params/ n, x
    
    open(10, file='params.nml', status='old', iostat=ios)
    if (ios /= 0) then
        print *, 'Error opening namelist file'
        stop
    end if
    
    read(10, nml=params, iostat=ios)
    if (ios /= 0) then
        print *, 'Error reading namelist'
    end if
    
    close(10)
end program
```

```fortran
! CORRECT: Multiple namelist groups
program multi_namelist
    implicit none
    integer :: n
    real :: x
    character(len=20) :: name
    namelist /params/ n, x
    namelist /info/ name
    
    n = 10
    x = 3.14
    name = 'test'
    
    write(*, nml=params)
    write(*, nml=info)
end program
```

## Related Errors

- [I/O Error](fortran-io-error-v2) - file operation errors
- [Format Error](fortran-format-error-v2) - format mismatch
- [Runtime Error](fortran-runtime-error-v2) - general runtime
