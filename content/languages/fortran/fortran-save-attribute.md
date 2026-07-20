---
title: "[Solution] Fortran Save Attribute — Persistent Local Variables"
description: "Fix Fortran save attribute errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1048
---

The `save` attribute makes local variables retain their values between calls. Errors involve unintended persistence (debugging nightmare) or missing `save` for variables that must persist.

## Common Causes

- Forgetting `save` for a counter that should persist (or vice versa)
- Inconsistent `save` declarations in a module (one public, one private)
- Using `save` with `intent` (incompatible for dummy arguments)
- Mixing explicit `save` and implicit `save` behavior

## How to Fix

### 1. Use explicit save for variables that must persist

```fortran
subroutine counter()
  integer, save :: n = 0
  n = n + 1
  print *, 'Call number:', n
end subroutine
```

### 2. Avoid save for variables that should reset

```fortran
subroutine bad_counter()
  integer, save :: n = 0  ! Persists: maybe not intended
  n = n + 1
end subroutine

subroutine good_counter()
  integer :: n = 0  ! Reset each call (F90+: initialized each call)
  n = n + 1
end subroutine
```

### 3. Use data statement initialization + save for legacy code

```fortran
subroutine legacy()
  integer n
  data n /0/
  save n  ! explicitly save
  n = n + 1
end subroutine
```

### 4. Use save in modules for module-level persistence

```fortran
module counters
  implicit none
  integer, save :: global_count = 0
contains
  subroutine increment()
    global_count = global_count + 1
  end subroutine
end module
```

### 5. Check for save-related debugging issues

```fortran
! If a variable seems to retain old values unexpectedly,
! check if it has an implicit save (common in Fortran 77)
```

## Examples

Module with save attributes:

```fortran
module stats
  implicit none
  integer, save :: call_count = 0
  real, save :: running_sum = 0.0

contains
  subroutine record(x)
    real, intent(in) :: x
    call_count = call_count + 1
    running_sum = running_sum + x
    print *, 'Mean so far:', running_sum / real(call_count)
  end subroutine
end module
```

## Related Errors

- [Fortran Parameter Attribute](../fortran-parameter-attribute)
- [Fortran Data Statement](../fortran-data-statement)
- [Fortran Module Error](../fortran-module-error)
