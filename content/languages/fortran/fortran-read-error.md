---
title: "[Solution] Fortran Read Error — Input Reading Failures"
description: "Fix Fortran read errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1064
---

Read errors happen when input data cannot be parsed into the expected variables. Common causes include type mismatches, premature end-of-file, or malformed data.

## Common Causes

- Input data does not match the variable type (e.g., "abc" into an integer)
- End-of-file reached before all variables were read
- Wrong format specifier in the read statement
- Missing input file or wrong unit number

## How to Fix

### 1. Use iostat to catch errors

```fortran
integer :: ierr, n
read(*, *, iostat=ierr) n
if (ierr /= 0) then
  print *, 'Read error:', ierr
end if
```

### 2. Check for end-of-file with iostat

```fortran
! Negative iostat value indicates end-of-file
read(*, *, iostat=ierr) n
if (ierr < 0) then
  print *, 'End of file'
else if (ierr > 0) then
  print *, 'Error reading input'
end if
```

### 3. Use advance='no' for partial reads

```fortran
read(*, '(A)', advance='no', iostat=ierr) line
```

### 4. Read character strings and convert manually

```fortran
character(len=20) :: str
integer :: n
read(*, '(A)') str
read(str, *) n  ! separate conversion
```

### 5. Use namelist for structured input

```fortran
namelist /input/ n, x
read(*, nml=input)
```

## Examples

Robust input reading:

```fortran
program read_example
  implicit none
  integer :: n, ierr
  real :: values(10)

  print *, 'Enter 10 numbers:'
  do i = 1, 10
    read(*, *, iostat=ierr) values(i)
    if (ierr /= 0) then
      print *, 'Error at input', i
      stop
    end if
  end do

  print *, 'Sum:', sum(values)
end program
```

## Related Errors

- [Fortran IO Error](../fortran-io-error)
- [Fortran End Of File](../fortran-end-of-file)
- [Fortran IOSTAT Error](../fortran-iostat)
