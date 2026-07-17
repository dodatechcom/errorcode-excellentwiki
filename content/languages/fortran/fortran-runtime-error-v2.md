---
title: "[Solution] Fortran runtime: end-of-file during read"
description: "Fix Fortran runtime errors when end-of-file is encountered unexpectedly during a read operation."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Fortran runtime error "end of file during read" occurs when a READ statement encounters the end of a file before all data items have been read. This typically indicates a mismatch between the file format and the READ statement.

## Common Causes

- File has fewer records than expected
- READ format doesn't match file format
- File was truncated or corrupted
- Missing END= or IOSTAT= specifier
- Reading past the last record

## How to Fix

```fortran
! WRONG: No end-of-file handling
program read_error
    implicit none
    integer :: i, value
    open(10, file='data.txt')
    do i = 1, 100
        read(10, *) value  ! May hit EOF
    end do
    close(10)
end program
```

```fortran
! CORRECT: Handle end-of-file
program read_safe
    implicit none
    integer :: i, value, ios
    open(10, file='data.txt', status='old')
    do i = 1, 100
        read(10, *, iostat=ios) value
        if (ios /= 0) exit  ! EOF or error
        print *, 'Value:', value
    end do
    close(10)
end program
```

```fortran
! CORRECT: Use END= specifier
program read_end
    implicit none
    integer :: value
    open(10, file='data.txt', status='old')
100 read(10, *, end=200) value
    print *, 'Value:', value
    goto 100
200 close(10)
    print *, 'End of file reached'
end program
```

```fortran
! CORRECT: Check file size first
program check_file
    implicit none
    integer :: n, ios
    character(len=100) :: line
    
    open(10, file='data.txt', status='old', iostat=ios)
    if (ios /= 0) then
        print *, 'Error opening file'
        stop
    end if
    
    n = 0
    do
        read(10, *, iostat=ios) line
        if (ios /= 0) exit
        n = n + 1
    end do
    
    rewind(10)
    print *, 'File has', n, 'lines'
    close(10)
end program
```

## Related Errors

- [I/O Error](fortran-io-error-v2) - file operation errors
- [End of File](fortran-end-of-file-v2) - unexpected EOF
- [Format Error](fortran-format-error-v2) - format mismatch
