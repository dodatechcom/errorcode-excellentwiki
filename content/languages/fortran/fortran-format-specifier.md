---
title: "[Solution] Fortran Format Specifier — Formatting Errors"
description: "Fix Fortran format specifier errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1062
---

Format specifiers control how data is formatted for reading or writing. Errors involve mismatched format descriptors, wrong field widths, or using format specifiers that do not match the data type.

## Common Causes

- Format descriptor does not match the data type (e.g., `F8.3` for an integer)
- Insufficient field width causing truncation or overflow
- Missing closing parenthesis in format string
- Using `I` format for real numbers or `F` format for integers

## How to Fix

### 1. Match format descriptors to data types

```fortran
integer :: n = 42
real :: x = 3.14159

print '(I5)', n       ! integer
print '(F10.5)', x    ! real
print '(A10)', 'hello'! character
```

### 2. Use adequate field widths

```fortran
! F format: Fw.d where w = total width, d = decimal places
real :: val = 1234.5678
print '(F10.3)', val   ! " 1234.568"
print '(F5.2)', val    ! *** (overflow!)
```

### 3. Use list-directed I/O for simplicity

```fortran
print *, x, n  ! no format needed
```

### 4. Use E format for scientific notation

```fortran
real :: big = 1.23e20
print '(ES12.4)', big  ! 1.2300E+20
```

### 5. Use G format for general output

```fortran
real :: val = 3.14
print '(G10.4)', val  ! chooses F or E as appropriate
```

## Examples

Various format specifiers:

```fortran
program format_demo
  implicit none
  integer :: i = 42
  real :: r = 3.14159
  character(len=5) :: s = "hello"

  ! Integer formats
  print '(I5)', i          ! "   42"
  print '(I0)', i          ! "42" (minimum width)

  ! Real formats
  print '(F8.3)', r        ! "   3.142"
  print '(E12.4)', r       ! " 0.3142E+01"
  print '(ES12.4)', r      ! " 3.1420E+00"

  ! String format
  print '(A6)', s          ! "hello "
  print '(A)', s           ! "hello"

  ! Multiple values
  print '(I5, F8.3, A6)', i, r, s
end program
```

## Related Errors

- [Fortran Write Format Error](../fortran-write-format)
- [Fortran Format Error](../fortran-format-error)
- [Fortran IO Error](../fortran-io-error)
