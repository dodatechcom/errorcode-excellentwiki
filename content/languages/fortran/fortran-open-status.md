---
title: "[Solution] Fortran Open Status — File Opening Errors"
description: "Fix Fortran open statement errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1067
---

The `open` statement opens a file for I/O. Errors involve wrong status values, missing files, permission issues, or incompatible file modes.

## Common Causes

- File does not exist when `status='old'` is specified
- Writing to a file with `status='old'` instead of `status='replace'`
- Missing `action='readwrite'` for read/write access
- Unit number already in use

## How to Fix

### 1. Check status values

```fortran
! status='old'     — file must exist
! status='new'     — file must NOT exist
! status='replace' — create or overwrite
! status='scratch' — temporary file, deleted on close
! status='unknown' — implementation-dependent
```

### 2. Verify file exists before opening

```fortran
inquire(file='data.txt', exist=exists)
if (exists) then
  open(10, file='data.txt', status='old')
else
  print *, 'File not found'
end if
```

### 3. Use action= to control read/write

```fortran
open(10, file='out.txt', status='replace', action='write')
open(20, file='data.txt', status='old', action='read')
open(30, file='work.txt', status='scratch', action='readwrite')
```

### 4. Check unit number conflicts

```fortran
open(10, file='a.txt', status='old')  ! OK
open(10, file='b.txt', status='old')  ! ERROR: unit 10 already open
```

### 5. Use iostat to handle open errors

```fortran
integer :: ierr
open(10, file='data.txt', status='old', iostat=ierr)
if (ierr /= 0) then
  print *, 'Failed to open file'
  stop
end if
```

## Examples

A robust file open pattern:

```fortran
program file_io
  implicit none
  integer :: ios
  logical :: exists

  inquire(file='config.txt', exist=exists)
  if (.not. exists) then
    print *, 'config.txt not found, using defaults'
    call run_with_defaults()
    return
  end if

  open(unit=10, file='config.txt', status='old', &
       action='read', iostat=ios)
  if (ios /= 0) then
    print *, 'Cannot open config.txt'
    stop
  end if

  ! read config
  close(10)
end program
```

## Related Errors

- [Fortran IO Error](../fortran-io-error)
- [Fortran Inquire Error](../fortran-inquire)
- [Fortran Read Error](../fortran-read-error)
