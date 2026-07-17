---
title: "End of file error in Fortran"
description: "End of file errors in Fortran occur when attempting to read past the end of a file."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["eof", "end-of-file", "read", "iostat", "fortran"]
weight: 5
---

## What This Error Means

An end of file error occurs when a READ statement tries to read data beyond the end of the file. Fortran reports this via IOSTAT as a negative value (-1 on most systems).

## Common Causes

- Reading more records than the file contains
- Not checking for EOF before reading
- Loop reading until EOF not implemented correctly
- File truncated during reading

## How to Fix

```fortran
! WRONG: No EOF check
program eof_example
    implicit none
    integer :: ios, value
    open(10, file='data.txt', status='old')
    do
        read(10, *, iostat=ios) value   ! May hit EOF
        print *, value
    end do
end program
```

```fortran
! CORRECT: Check IOSTAT for EOF
program eof_safe
    implicit none
    integer :: ios, value
    open(10, file='data.txt', status='old')
    do
        read(10, *, iostat=ios) value
        if (ios < 0) exit   ! End of file
        if (ios > 0) then
            print *, 'Read error'
            exit
        end if
        print *, value
    end do
    close(10)
end program
```

## Examples

```fortran
program example
    implicit none
    integer :: ios, n
    open(10, file='small.txt')
    do
        read(10, *, iostat=ios) n
        if (ios /= 0) exit
        print *, n
    end do
end program
```

## Related Errors

- [I/O Error](/languages/fortran/fortran-io-error) - file operation errors
- [Format Error](/languages/fortran/fortran-format-error) - format issues
