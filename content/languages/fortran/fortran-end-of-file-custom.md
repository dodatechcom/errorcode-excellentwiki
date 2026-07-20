---
title: "[Solution] Fortran End Of File — EOF Handling Errors"
description: "Fix Fortran end-of-file errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1065
---

End-of-file (EOF) errors occur when a read statement encounters the end of the input file or unit. Proper handling requires checking `iostat` or using the `end=` label.

## Common Causes

- Reading past the last record in a sequential file
- Reading an empty file
- Forgetting to check for EOF in a read loop
- Using format-directed read on unformatted data

## How to Fix

### 1. Use the end= label for sequential reads

```fortran
read(10, *, end=100) n
! code for successful read
goto 200
100 continue
print *, 'End of file reached'
200 continue
```

### 2. Use iostat to detect EOF

```fortran
integer :: ierr
do
  read(10, *, iostat=ierr) n
  if (ierr < 0) exit  ! end of file
  if (ierr > 0) then
    print *, 'Read error'
    exit
  end if
  print *, n
end do
```

### 3. Check if file is empty before reading

```fortran
inquire(file='data.txt', size=file_size)
if (file_size == 0) then
  print *, 'File is empty'
  stop
end if
```

### 4. Use size= to avoid EOF errors

```fortran
character(len=100) :: line
integer :: n_chars
read(10, '(A)', size=n_chars, advance='no') line
line = line(:n_chars)
```

### 5. Combine EOF with formatted reading

```fortran
open(10, file='data.txt', status='old')
do
  read(10, *, iostat=ierr) x, y
  if (ierr /= 0) exit
  call process(x, y)
end do
close(10)
```

## Examples

Complete EOF handling pattern:

```fortran
program read_file
  implicit none
  integer :: ios, line_count = 0
  real :: value
  character(len=80) :: line

  open(unit=10, file='numbers.txt', status='old', action='read')
  do
    read(10, *, iostat=ios) value
    if (ios < 0) exit  ! EOF
    if (ios > 0) then
      print *, 'Error on line', line_count + 1
      exit
    end if
    line_count = line_count + 1
    print *, 'Value:', value
  end do
  close(10)
  print *, 'Read', line_count, 'values'
end program
```

## Related Errors

- [Fortran IO Error](../fortran-io-error)
- [Fortran Read Error](../fortran-read-error)
- [Fortran IOSTAT Error](../fortran-iostat)
