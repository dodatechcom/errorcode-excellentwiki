---
title: "[Solution] Fortran Subroutine — Subprogram Errors"
description: "Fix Fortran subroutine errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1079
---

Subroutines perform actions through side effects on arguments. Errors involve argument mismatches, missing `call` keyword, or incorrect intent usage.

## Common Causes

- Forgetting the `call` keyword when invoking a subroutine
- Argument type or shape mismatch between caller and callee
- Modifying an `intent(in)` argument
- Too many or too few arguments in the call

## How to Fix

### 1. Always use call for subroutines

```fortran
subroutine greet()
  print *, 'Hello'
end subroutine

call greet()  ! CORRECT
greet()       ! WRONG: missing call
```

### 2. Match argument types exactly

```fortran
subroutine swap(a, b)
  real, intent(inout) :: a, b
  real :: temp
  temp = a
  a = b
  b = temp
end subroutine

real :: x, y
call swap(x, y)  ! OK: both real
```

### 3. Use optional arguments with present()

```fortran
subroutine log_msg(msg, level)
  character(len=*), intent(in) :: msg
  integer, intent(in), optional :: level
  integer :: lvl
  if (present(level)) then
    lvl = level
  else
    lvl = 1
  end if
  print *, 'Level', lvl, ':', msg
end subroutine

call log_msg('hello')
call log_msg('warning', 2)
```

### 4. Use assumed-shape arrays for flexibility

```fortran
subroutine sum_array(arr, total)
  real, intent(in) :: arr(:)
  real, intent(out) :: total
  total = sum(arr)
end subroutine
```

### 5. Use recursive subroutines when needed

```fortran
recursive subroutine countdown(n)
  integer, intent(in) :: n
  if (n <= 0) return
  print *, n
  call countdown(n - 1)
end subroutine
```

## Examples

A complete subroutine module:

```fortran
module statistics
  implicit none
contains
  subroutine mean_and_std(data, n, avg, std)
    integer, intent(in) :: n
    real, intent(in) :: data(n)
    real, intent(out) :: avg, std
    real :: variance
    integer :: i

    avg = sum(data) / real(n)
    variance = 0.0
    do i = 1, n
      variance = variance + (data(i) - avg)**2
    end do
    variance = variance / real(n - 1)
    std = sqrt(variance)
  end subroutine
end module
```

## Related Errors

- [Fortran Intent Error](../fortran-intent-attribute)
- [Fortran Interface Error](../fortran-interface-error)
- [Fortran Module Error](../fortran-module-error)
