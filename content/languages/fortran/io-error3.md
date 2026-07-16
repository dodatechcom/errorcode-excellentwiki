---
title: "I/O error"
description: "An I/O error occurs when a Fortran program encounters a problem reading from or writing to a file or device."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["io", "file", "input-output", "device"]
weight: 5
---

## What This Error Means

An I/O error occurs when a Fortran program fails to complete a file operation such as opening, reading, writing, or closing a file. This can happen due to missing files, permission issues, disk full conditions, or incorrect file unit usage. Fortran uses numbered unit identifiers for file operations, and errors in unit management are a common source of I/O problems.

## Common Causes

- Opening a file that does not exist without proper error handling
- Writing to a file without write permissions
- Using an invalid or unopened unit number for read/write operations
- Disk full or quota exceeded when writing output files

## How to Fix

```fortran
! WRONG: Not checking if file exists before reading
program io_example
    implicit none
    integer :: ios
    real :: x
    open(unit=10, file='data.txt', status='old')
    read(10, *) x          ! crashes if file doesn't exist
    close(10)
end program

! CORRECT: Use IOSTAT to check for errors
program io_example
    implicit none
    integer :: ios
    real :: x
    open(unit=10, file='data.txt', status='old', iostat=ios)
    if (ios /= 0) then
        print *, 'Error opening file, iostat =', ios
        stop
    end if
    read(10, *, iostat=ios) x
    if (ios /= 0) then
        print *, 'Error reading file'
    end if
    close(10)
end program
```

```fortran
! WRONG: Using an unopened unit number
program bad_unit
    implicit none
    write(99, *) 'Hello'    ! unit 99 was never opened
end program

! CORRECT: Always open before use
program good_unit
    implicit none
    integer :: ios
    open(unit=99, file='output.txt', status='replace', iostat=ios)
    if (ios == 0) then
        write(99, *) 'Hello'
        close(99)
    end if
end program
```

## Examples

```fortran
program io_error_example
    implicit none
    integer :: i, ios

    ! ERROR: Trying to read from a unit that doesn't exist
    read(50, *, iostat=ios) i
    if (ios /= 0) then
        print *, 'I/O error on unit 50, iostat =', ios
    end if

    ! ERROR: Writing to a read-only file
    open(unit=10, file='/etc/hostname', status='old')
    write(10, *) 'new hostname'   ! permission denied - I/O error
    close(10)

end program
```

## Related Errors

- [Array bounds exceeded](/languages/fortran/array-bounds2)
- [Runtime error](/languages/fortran/runtime-error11)
