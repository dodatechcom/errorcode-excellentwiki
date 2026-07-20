---
title: "[Solution] Fortran IOSTAT — I/O Status Reporting"
description: "Fix Fortran iostat errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1066
---

`iostat` returns the status of an I/O operation: 0 for success, positive for error, negative for end-of-file. Errors involve misinterpreting the iostat value or not checking it at all.

## Common Causes

- Not checking iostat after I/O operations
- Misinterpreting negative values (EOF) as errors
- Using `iostat` with unit `*` (standard input/output)
- Forgetting that `iostat=` applies to the I/O statement, not individual variables

## How to Fix

### 1. Always use iostat on I/O statements

```fortran
integer :: ierr
read(10, *, iostat=ierr) x
select case (ierr)
case (0)
  ! success
case (:-1)
  ! end of file
case (1:)
  ! error
  print *, 'I/O error:', ierr
end select
```

### 2. Use iomsg for error messages (Fortran 2003)

```fortran
character(len=256) :: msg
integer :: ierr
read(10, *, iostat=ierr, iomsg=msg) x
if (ierr /= 0) print *, 'Error:', trim(msg)
```

### 3. Use iostat in inquire

```fortran
integer :: ierr
inquire(file='data.txt', exist=exists, iostat=ierr)
```

### 4. Use iostat in open

```fortran
integer :: ierr
open(10, file='data.txt', status='old', iostat=ierr)
if (ierr /= 0) stop 'Cannot open file'
```

### 5. Use iostat in write for error detection

```fortran
integer :: ierr
write(10, *, iostat=ierr) x, y
if (ierr /= 0) print *, 'Write failed'
```

## Examples

Complete iostat usage:

```fortran
program iostat_demo
  implicit none
  integer :: ios, n
  character(len=256) :: errmsg

  open(10, file='data.txt', status='old', iostat=ios, iomsg=errmsg)
  if (ios /= 0) then
    print *, 'Open error:', trim(errmsg)
    stop
  end if

  do
    read(10, *, iostat=ios, iomsg=errmsg) n
    if (ios < 0) exit
    if (ios > 0) then
      print *, 'Read error:', trim(errmsg)
      exit
    end if
    print *, 'Read:', n
  end do
  close(10)
end program
```

## Related Errors

- [Fortran IO Error](../fortran-io-error)
- [Fortran End Of File](../fortran-end-of-file-custom)
- [Fortran Open Error](../fortran-open-error)
