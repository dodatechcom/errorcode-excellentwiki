---
title: "[Solution] Fortran Inquire — File Inquiry Errors"
description: "Fix Fortran inquire errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1068
---

The `inquire` statement queries file properties without opening it. Errors involve querying a file that does not exist, using invalid specifiers, or ignoring iostat.

## Common Causes

- Querying a file that does not exist (check `exist=` first)
- Using `inquire` with both `file=` and `unit=` simultaneously
- Not all compilers support all inquire specifiers (e.g., `name=` in Fortran 90)
- Using inquire results before the inquire statement completes

## How to Fix

### 1. Check file existence first

```fortran
logical :: exists
inquire(file='data.txt', exist=exists)
if (exists) then
  open(10, file='data.txt', status='old')
end if
```

### 2. Use inquire to check file size

```fortran
integer :: sz
inquire(file='data.txt', size=sz)
print *, 'File size:', sz, 'bytes'
```

### 3. Use unit-based inquire for open files

```fortran
inquire(unit=10, opened=isOpen, named=hasName, name=filename)
```

### 4. Check I/O status of inquire

```fortran
integer :: ios
inquire(file='data.txt', exist=exists, iostat=ios)
if (ios /= 0) print *, 'Inquire error'
```

### 5. Use inquire for pending output

```fortran
inquire(unit=10, pending=pending)
if (pending) then
  ! flush the output
  flush(10)
end if
```

## Examples

Comprehensive file inquiry:

```fortran
program inquire_demo
  implicit none
  character(len=256) :: filename
  logical :: exists, opened, named
  integer :: sz, ios

  filename = 'test.dat'
  inquire(file=filename, exist=exists, size=sz, iostat=ios)

  if (.not. exists) then
    print *, trim(filename), ' does not exist'
    stop
  end if

  print *, 'File exists, size:', sz

  inquire(file=filename, opened=opened, named=named)
  if (opened) then
    print *, 'File is already open'
  end if
end program
```

## Related Errors

- [Fortran IO Error](../fortran-io-error)
- [Fortran Open Status](../fortran-open-status)
- [Fortran End Of File](../fortran-end-of-file-custom)
