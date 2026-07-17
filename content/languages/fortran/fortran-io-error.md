---
title: "I/O error in Fortran"
description: "I/O errors in Fortran occur when file operations fail due to file not found, permission issues, or format mismatches."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Fortran I/O errors occur during file operations (OPEN, READ, WRITE, CLOSE). They are reported with error codes via the IOSTAT specifier or ERR label.

## Common Causes

- File doesn't exist for reading
- Permission denied for writing
- Format string doesn't match data
- Unit number already in use
- End of file reached unexpectedly

## How to Fix

```fortran
! WRONG: No error handling for file open
program io_example
    implicit none
    integer :: ios
    open(unit=10, file='data.txt', status='old')
    ! Error if file doesn't exist
end program
```

```fortran
! CORRECT: Handle I/O errors
program io_safe
    implicit none
    integer :: ios, ierr
    open(unit=10, file='data.txt', status='old', iostat=ierr)
    if (ierr /= 0) then
        print *, 'Error opening file: ', ierr
        stop
    end if
    read(10, *, iostat=ios) x
    if (ios /= 0) then
        print *, 'Error reading file'
    end if
    close(10)
end program
```

## Examples

```fortran
program example
    implicit none
    integer :: ierr
    open(10, file='nonexistent.txt', status='old', iostat=ierr)
    ! ierr will be non-zero if file doesn't exist
end program
```

## Related Errors

- [End of File](/languages/fortran/fortran-end-of-file) - EOF handling
- [Format Error](/languages/fortran/fortran-format-error) - format mismatches
