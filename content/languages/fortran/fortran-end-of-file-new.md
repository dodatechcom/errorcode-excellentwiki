---
title: "[Solution] Fortran: end of file encountered during read"
description: "Fix Fortran end of file errors by checking file existence and handling EOF conditions properly."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An end of file error in Fortran occurs when a READ statement attempts to read past the end of a file. This happens when the program expects more data records than actually exist in the file. The error is typically reported as an I/O status error with a specific code indicating premature end of file. The program may crash or produce undefined variable values for data items that were not successfully read from the file.

## Why It Happens

This error occurs in several scenarios. The most common is reading a file without checking whether more records are available, especially in a loop that reads until some condition is met rather than until EOF. The file may have fewer records than expected due to incomplete data generation, truncated file transfers, or user editing errors. Using fixed-format reads where the record length does not match the actual data can also cause premature EOF. In direct access files, requesting a record number beyond the file's actual length triggers this error. Sequential access reads that do not use `iostat` or `end` labels cannot gracefully handle running out of data. Passing a file unit that has already reached EOF to another READ statement without rewinding also produces this error.

## How to Fix It

**Check I/O status on every READ:**

```fortran
program safe_read
    implicit none
    integer :: ios, value
    open(10, file='data.txt', status='old')

    do
        read(10, *, iostat=ios) value
        if (ios /= 0) exit  ! Exit on any I/O error including EOF
        print *, value
    end do

    close(10)
end program
```

**Use the end label for sequential files:**

```fortran
program read_with_end
    implicit none
    integer :: value

    open(10, file='data.txt', status='old')
100 read(10, *, end=200) value
    print *, value
    goto 100

200 close(10)
    print *, 'End of file reached'
end program
```

**Verify file contents before reading:**

```fortran
program check_file
    implicit none
    integer :: ios, recl, nrec
    character(len=100) :: line

    open(10, file='data.txt', status='old', iostat=ios)
    if (ios /= 0) then
        print *, 'Error opening file'
        stop
    end if

    ! Count records
    nrec = 0
    do
        read(10, '(A)', iostat=ios) line
        if (ios /= 0) exit
        nrec = nrec + 1
    end do

    rewind(10)
    print *, 'File has', nrec, 'records'
    close(10)
end program
```

**Read entire file into an array safely:**

```fortran
program read_all
    implicit none
    integer, allocatable :: data(:)
    integer :: ios, count, temp
    integer :: i

    open(10, file='numbers.txt', status='old')
    count = 0
    do
        read(10, *, iostat=ios) temp
        if (ios /= 0) exit
        count = count + 1
    end do

    rewind(10)
    allocate(data(count))
    do i = 1, count
        read(10, *) data(i)
    end do
    close(10)

    print *, 'Read', count, 'values'
    deallocate(data)
end program


## Common Mistakes

- Not checking `iostat` on READ statements, allowing silent failures
- Assuming a file has a specific number of records without verifying
- Not rewinding a file after counting records before actually reading them
- Using list-directed I/O when record format is known and fixed-length records would be safer
- Forgetting to close files, which can cause resource leaks and unpredictable behavior

## Related Pages

- [I/O error in Fortran](/languages/fortran/fortran-io-error-v2)
- [Format descriptor error in Fortran](/languages/fortran/fortran-format-error-new)
- [Memory allocation failed in Fortran](/languages/fortran/fortran-allocate-error-v2)
- [Undefined variable in Fortran](/languages/fortran/fortran-undefined-variable-new)
