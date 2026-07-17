---
title: "[Solution] Fortran: I/O error on unit"
description: "Fix Fortran I/O errors when file operations fail, including file not found, permission denied, or format errors."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Fortran I/O errors occur when file operations (OPEN, READ, WRITE, CLOSE) fail. Error codes provide specific information about the failure type.

## Common Causes

- File doesn't exist
- Permission denied
- Disk full
- Invalid file unit
- File already open
- Format specification error

## How to Fix

```fortran
! WRONG: No error handling
program io_error
    implicit none
    integer :: value
    open(10, file='data.txt')
    read(10, *) value  ! May fail
    close(10)
end program
```

```fortran
! CORRECT: Check I/O status
program io_safe
    implicit none
    integer :: value, ios
    character(len=100) :: errmsg
    
    open(10, file='data.txt', status='old', iostat=ios, err=100)
    read(10, *, iostat=ios) value
    if (ios /= 0) then
        print *, 'Read error:', ios
    end if
    close(10)
    stop
    
100 print *, 'Error opening file'
end program
```

```fortran
! CORRECT: Use IOMSG for detailed errors
program io_detailed
    implicit none
    integer :: ios
    character(len=256) :: iomsg
    
    open(10, file='data.txt', status='old', &
         iostat=ios, iomsg=iomsg, action='read')
    
    if (ios /= 0) then
        print *, 'Open error:', trim(iomsg)
        stop
    end if
    
    close(10)
end program
```

```fortran
! CORRECT: Check file exists first
program check_file
    implicit none
    logical :: exists
    character(len=100) :: filename = 'data.txt'
    
    inquire(file=filename, exist=exists)
    
    if (exists) then
        open(10, file=filename, status='old')
        ! Read file
        close(10)
    else
        print *, 'File not found: ', filename
    end if
end program
```

```fortran
! CORRECT: Handle specific error codes
program handle_errors
    implicit none
    integer :: ios
    
    open(10, file='data.txt', iostat=ios)
    
    select case (ios)
    case (0)
        print *, 'File opened successfully'
    case (2)
        print *, 'File not found'
    case (5)
        print *, 'Permission denied'
    case (13)
        print *, 'File already in use'
    case default
        print *, 'Unknown error:', ios
    end select
    
    close(10)
end program
```

## Related Errors

- [Runtime Error](fortran-runtime-error-v2) - EOF during read
- [End of File](fortran-end-of-file-v2) - unexpected EOF
- [Format Error](fortran-format-error-v2) - format mismatch
