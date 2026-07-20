---
title: "[Solution] Fortran Subroutine Argument — Parameter Mismatch"
description: "Fix Fortran subroutine argument errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1131
---

Subroutine argument mismatch occurs when the caller passes arguments that do not match the subroutine's interface in type, kind, shape, or count.

## Common Causes

- Wrong number of arguments in the call
- Type or kind mismatch between actual and dummy arguments
- Shape mismatch for array arguments
- Passing expression to intent(inout) argument

## How to Fix

### 1. Write explicit interfaces

```fortran
interface
  subroutine process(arr, n)
    real, intent(in) :: arr(:)
    integer, intent(in) :: n
  end subroutine
end interface
```

### 2. Match argument types exactly

```fortran
subroutine add(a, b, c)
  real, intent(in) :: a, b
  real, intent(out) :: c
  c = a + b
end subroutine

call add(1.0, 2.0, result)  ! all real
```

### 3. Use assumed-shape for flexible arrays

```fortran
subroutine sum_array(arr, total)
  real, intent(in) :: arr(:)
  real, intent(out) :: total
  total = sum(arr)
end subroutine
```

### 4. Do not pass expressions to intent(inout)

```fortran
call increment(x + 1)  ! WRONG: expression to inout
call increment(x)      ! OK: variable to inout
```

### 5. Use optional arguments

```fortran
subroutine configure(n, verbose)
  integer, intent(in) :: n
  logical, intent(in), optional :: verbose
  if (present(verbose)) print *, 'Verbose mode'
end subroutine
```

## Examples

A well-defined subroutine:

```fortran
subroutine interpolate(x1, y1, x2, y2, xq, yq)
  real, intent(in) :: x1, y1, x2, y2, xq
  real, intent(out) :: yq
  if (x2 == x1) then
    yq = 0.0
  else
    yq = y1 + (y2 - y1) * (xq - x1) / (x2 - x1)
  end if
end subroutine
```

## Related Errors

- [Fortran Interface Error](../fortran-interface-error)
- [Fortran Subroutine](../fortran-subroutine)
- [Fortran Intent Error](../fortran-intent-attribute)
