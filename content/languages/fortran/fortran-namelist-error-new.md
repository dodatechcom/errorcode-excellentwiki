---
title: "[Solution] Fortran: namelist read or write error"
description: "Fix Fortran namelist I/O errors by validating syntax and checking variable declarations."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A namelist error in Fortran occurs when reading from or writing to a namelist group fails due to syntax errors in the namelist input, mismatched variable types, undeclared variables in the namelist, or incorrect group name references. Namelist I/O provides a convenient way to read named variables from input files, but the format is strict. Errors are reported through IOSTAT values and can cause the program to read incorrect values or terminate prematurely.

## Why It Happens

Namelist errors arise from several issues. The input file may contain syntax errors such as missing commas between values, incorrect assignment operators, or misspelled variable names. A variable referenced in the namelist input file may not be declared in the namelist group definition. The group name in the READ or WRITE statement may not match any defined namelist. Type mismatches between the input values and the declared variable types cause errors. Namelist input files use a specific format with `&GROUPNAME` to begin and `/` to end, and deviating from this format triggers errors. Special characters in character variables may conflict with namelist syntax delimiters. Arrays in namelist input require specific syntax with parentheses and commas that must be exact.

## How to Fix It

**Define namelist groups properly:**

```fortran
program namelist_example
    implicit none
    integer :: count
    real :: temperature
    character(len=20) :: location
    namelist /params/ count, temperature, location

    ! Initialize defaults
    count = 0
    temperature = 0.0
    location = 'unknown'

    ! Read from file
    open(10, file='input.nml', status='old')
    read(10, nml=params)
    close(10)

    print *, 'Count:', count
    print *, 'Temp:', temperature
    print *, 'Location:', trim(location)
end program
```

**Write valid namelist input files:**

```
&params
  count = 42
  temperature = 72.5
  location = "New York"
/
```

**Check for common syntax errors:**

```fortran
! Common mistakes in namelist input:
! WRONG: missing quotes around strings
!   location = New York
! CORRECT: use quotes
!   location = "New York"

! WRONG: using = instead of =
! WRONG: missing commas between items
! CORRECT format:
!   &params
!     count = 42,
!     temperature = 72.5
!   /
```

**Handle arrays in namelist:**

```fortran
program namelist_arrays
    implicit none
    integer :: values(5)
    namelist /data/ values

    values = 0

    open(10, file='array.nml', status='old')
    read(10, nml=data)
    close(10)

    print *, values
end program
```

```
&data
  values(1) = 10
  values(2) = 20
  values(3) = 30
  values(4) = 40
  values(5) = 50
/
```

**Check IOSTAT for error handling:**

```fortran
program safe_namelist
    implicit none
    integer :: ios, x
    namelist /settings/ x

    x = 0
    open(10, file='settings.nml', status='old', iostat=ios)
    if (ios /= 0) then
        print *, 'Cannot open namelist file'
        stop
    end if

    read(10, nml=settings, iostat=ios)
    if (ios /= 0) then
        print *, 'Namelist read error, using defaults'
    end if

    close(10)
    print *, 'x =', x
end program
```

## Common Mistakes

- Not initializing namelist variables before reading, leaving them undefined if the input file omits them
- Using reserved characters like commas or equals signs inside string values without proper quoting
- Forgetting that namelist input is case-sensitive for variable names
- Not providing a default value for every namelist variable
- Confusing the namelist group name with the file name or program name

## Related Pages

- [Format descriptor error in Fortran](/languages/fortran/fortran-format-error-new)
- [End of file encountered in Fortran](/languages/fortran/fortran-end-of-file-new)
- [I/O error in Fortran](/languages/fortran/fortran-io-error-v2)
- [Undefined variable in Fortran](/languages/fortran/fortran-undefined-variable-new)
