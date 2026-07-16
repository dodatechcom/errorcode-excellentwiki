---
title: "Fortran I/O error"
description: "A Fortran I/O error occurs when a file operation fails due to invalid file handling, missing files, or permission issues."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["io", "file", "input-output"]
weight: 5
---

## What This Error Means

Fortran I/O errors occur during file read/write operations. They are triggered when the runtime cannot complete a requested I/O operation. Common triggers include attempting to read from a non-existent file, writing to a read-only file, or using an invalid file unit number.

## Common Causes

- Opening a file that does not exist (without the right status flags)
- Reading past the end of a file
- Using an unopened or already closed file unit
- Writing to a file opened with read-only status

## How to Fix

```fortran
! WRONG: Not checking if file exists before reading
program read_file
    implicit none
    integer :: ios
    character(len=100) :: line
    open(unit=10, file='data.txt', status='old')
    read(10, '(A)', iostat=ios) line  ! may fail if file missing
    close(10)
end program

! CORRECT: Use iostat and check status
program read_file
    implicit none
    integer :: ios
    character(len=100) :: line
    open(unit=10, file='data.txt', status='old', iostat=ios)
    if (ios /= 0) then
        print *, 'Error opening file'
        stop
    end if
    read(10, '(A)', iostat=ios) line
    if (ios < 0) then
        print *, 'End of file reached'
    else if (ios > 0) then
        print *, 'Read error occurred'
    end if
    close(10)
end program
```

```fortran
! WRONG: Reusing a closed unit number implicitly
program io_example
    implicit none
    close(10)                ! unit 10 was never opened
    write(10, *) 'Hello'    ! error - unit not opened

! CORRECT: Always open before use
program io_example
    implicit none
    open(unit=10, file='output.txt', status='replace')
    write(10, *) 'Hello'
    close(10)
end program
```

## Examples

```fortran
program io_error_example
    implicit none
    integer :: ios
    real :: value

    ! Trying to read a number from a text file
    open(unit=20, file='numbers.dat', status='old', iostat=ios)
    if (ios /= 0) then
        print *, 'Cannot open numbers.dat'
        stop 1
    end if

    ! This will produce an I/O error if file contains text
    read(20, *, iostat=ios) value
    if (ios /= 0) then
        print *, 'Failed to read number from file'
    end if

    close(20)
end program
```

## Related Errors

- [Array bounds exceeded](/languages/fortran/array-bounds)
