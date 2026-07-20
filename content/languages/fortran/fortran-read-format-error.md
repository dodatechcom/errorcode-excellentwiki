---
title: "[Solution] Fortran Read Error — Input Parsing Failures"
description: "Fix Fortran read format errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1127
---

Read errors in Fortran occur when the format specifier does not match the data, or when reading from a file with incorrect mode.

## Common Causes

- Format descriptor count does not match variable count
- Reading character data with numeric format
- Reading unformatted file with formatted read
- End-of-file during multi-variable read

## How to Fix

### 1. Match format descriptors to variables

```fortran
integer :: a, b
read(10, '(2I5)') a, b  ! two integers, two descriptors
```

### 2. Use list-directed for unstructured input

```fortran
read(10, *) value1, value2
```

### 3. Use advance='no' for partial-line reads

```fortran
read(10, '(A4)', advance='no') chunk
```

### 4. Check iostat before using the read values

```fortran
integer :: ios
read(10, *, iostat=ios) x
if (ios /= 0) x = 0.0
```

### 5. Use size= to avoid EOF errors

```fortran
character(len=100) :: line
integer :: nchars
read(10, '(A)', advance='no', size=nchars) line
line = line(:nchars)
```

## Examples

Robust formatted reading:

```fortran
program read_formatted
  implicit none
  integer :: ios, id
  real :: value
  character(len=20) :: name

  open(10, file='data.txt', status='old')
  do
    read(10, *, iostat=ios) id, name, value
    if (ios /= 0) exit
    print *, id, trim(name), value
  end do
  close(10)
end program
```

## Related Errors

- [Fortran Format Specifier](../fortran-format-specifier)
- [Fortran IO Error](../fortran-io-error)
- [Fortran End Of File](../fortran-end-of-file-custom)
