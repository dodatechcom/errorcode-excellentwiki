---
title: "[Solution] Fortran: unexpected end of file"
description: "Fix Fortran errors when encountering unexpected end of file during read operations."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Unexpected end of file occurs when Fortran READ statement reaches the end of file before all requested data has been read. This indicates a file format or content mismatch.

## Common Causes

- File has fewer records than expected
- READ statement expects more data than available
- File truncated during write
- Incorrect file format assumed
- Missing records due to editing

## How to Fix

```fortran
! WRONG: Assume file has enough data
program eof_error
    implicit none
    integer :: values(100)
    integer :: i
    
    open(10, file='data.txt', status='old')
    do i = 1, 100
        read(10, *) values(i)  ! May hit EOF early
    end do
    close(10)
end program
```

```fortran
! CORRECT: Handle EOF gracefully
program eof_safe
    implicit none
    integer :: values(100), n, ios
    integer :: i
    
    open(10, file='data.txt', status='old')
    n = 0
    
    do i = 1, 100
        read(10, *, iostat=ios) values(i)
        if (ios /= 0) exit
        n = n + 1
    end do
    
    close(10)
    print *, 'Read', n, 'values'
end program
```

```fortran
! CORRECT: Count records first
program count_records
    implicit none
    integer :: n, ios
    real :: dummy
    
    open(10, file='data.txt', status='old')
    n = 0
    
    do
        read(10, *, iostat=ios) dummy
        if (ios /= 0) exit
        n = n + 1
    end do
    
    rewind(10)
    
    ! Now read with known count
    block
        real :: data(n)
        integer :: i
        do i = 1, n
            read(10, *) data(i)
        end do
    end block
    
    close(10)
end program
```

```fortran
! CORRECT: Use END= specifier
program eof_goto
    implicit none
    integer :: value
    
    open(10, file='data.txt', status='old')
100 read(10, *, end=200) value
    print *, value
    goto 100
200 close(10)
    print *, 'End of file'
end program
```

```fortran
! CORRECT: Check file size
program check_size
    implicit none
    integer :: file_size, ios
    character(len=100) :: filename = 'data.txt'
    
    inquire(file=filename, size=file_size, iostat=ios)
    if (ios == 0) then
        print *, 'File size:', file_size, 'bytes'
    end if
end program
```

## Related Errors

- [I/O Error](fortran-io-error-v2) - file operation errors
- [Runtime Error](fortran-runtime-error-v2) - general runtime
- [Format Error](fortran-format-error-v2) - format mismatch
