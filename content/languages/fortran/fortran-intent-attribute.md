---
title: "[Solution] Fortran Intent — Intent(In/Out/Inout) Errors"
description: "Fix Fortran intent attribute errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1047
---

The `intent` attribute specifies whether a dummy argument can be read (`in`), written (`out`), or both (`inout`). Violating the intent (e.g., modifying an `intent(in)` argument) is a compile-time error.

## Common Causes

- Attempting to assign to an `intent(in)` dummy argument
- Passing a literal or expression to an `intent(out)` or `intent(inout)` argument
- Forgetting that `intent(out)` deallocates allocatable components on entry
- Using `intent(in)` when the subroutine needs to modify the argument

## How to Fix

### 1. Respect intent(in) — never assign to it

```fortran
subroutine bad(x)
  real, intent(in) :: x
  x = 5.0  ! ERROR: cannot modify intent(in)
end subroutine

subroutine good(x)
  real, intent(in) :: x
  print *, x  ! OK: reading is fine
end subroutine
```

### 2. Do not pass expressions to intent(out/inout)

```fortran
call sub(1.0)        ! ERROR: literal to intent(out)
call sub(variable)   ! OK: variable to intent(out)
```

### 3. Use intent(inout) when you need to read and modify

```fortran
subroutine increment(x)
  real, intent(inout) :: x
  x = x + 1.0
end subroutine
```

### 4. Use intent(out) for output-only arguments

```fortran
subroutine compute(n, result)
  integer, intent(in) :: n
  real, intent(out) :: result
  result = real(n) ** 2
end subroutine
```

### 5. Check allocatable intent(out) behavior

```fortran
subroutine reset(arr)
  real, allocatable, intent(out) :: arr(:)
  ! arr is deallocated on entry
  allocate(arr(10))
  arr = 0.0
end subroutine
```

## Examples

A well-specified subroutine:

```fortran
subroutine linear_interpolate(x, y, xq, yq)
  real, intent(in) :: x(:), y(:), xq
  real, intent(out) :: yq
  integer :: i, n

  n = size(x)
  do i = 1, n-1
    if (xq >= x(i) .and. xq <= x(i+1)) then
      yq = y(i) + (y(i+1) - y(i)) * (xq - x(i)) / (x(i+1) - x(i))
      return
    end if
  end do
  yq = 0.0
end subroutine
```

## Related Errors

- [Fortran Dimension Attribute Error](../fortran-dimension-attribute)
- [Fortran Subroutine Error](../fortran-subroutine)
- [Fortran Interface Error](../fortran-interface-error)
