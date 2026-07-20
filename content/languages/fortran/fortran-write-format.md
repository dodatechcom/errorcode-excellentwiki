---
title: "[Solution] Fortran Write Format — Output Formatting Errors"
description: "Fix Fortran write format errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1063
---

Write format errors occur when the format string does not match the data being written, or the output unit has restrictions on format usage.

## Common Causes

- Format string has fewer descriptors than data items (data truncated)
- Format string has more descriptors than data items (extra output or error)
- Using format specifiers incompatible with the data type
- Writing to a unit with unformatted status using formatted I/O

## How to Fix

### 1. Ensure format matches data count

```fortran
! WRONG: 3 items, 2 descriptors
print '(I5, F8.2)', 1, 2.0, 3  ! third item ignored or error

! CORRECT
print '(I5, F8.2, I5)', 1, 2.0, 3
```

### 2. Use unlimited format repeat for variable-length output

```fortran
print '(5(I5))', (i, i=1,10)  ! repeats the format
```

### 3. Use write with explicit unit number

```fortran
write(unit=*, fmt='(I5, F8.3)') n, x
```

### 4. Use trim for character output

```fortran
character(len=20) :: s = "hello"
write(*, '(A)') trim(s)
```

### 5. Use advance='no' for partial-line output

```fortran
do i = 1, 5
  write(*, '(I3, A)', advance='no') i, ' '
end do
print *  ! newline
```

## Examples

Formatted write to a file:

```fortran
program write_example
  implicit none
  integer, parameter :: n = 5
  real :: x(n), y(n)
  integer :: i

  x = [(real(i), i=1,n)]
  y = x**2

  open(unit=10, file='output.dat', status='replace')
  do i = 1, n
    write(10, '(F8.3, A, F10.4)') x(i), ', ', y(i)
  end do
  close(10)
end program
```

## Related Errors

- [Fortran Format Specifier](../fortran-format-specifier)
- [Fortran IO Error](../fortran-io-error)
- [Fortran Open Error](../fortran-open-error)
