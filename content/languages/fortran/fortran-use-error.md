---
title: "[Solution] Fortran Use Error — Module Import Issues"
description: "Fix Fortran USE statement errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1130
---

USE statement errors involve importing names that do not exist, circular dependencies, or forgetting the use statement entirely.

## Common Causes

- Referencing a module entity without USE
- USE only clause missing needed entities
- Circular module dependencies
- Module not compiled before dependent code

## How to Fix

### 1. Add the correct USE statement

```fortran
use my_module
use my_module, only: func1, var2
```

### 2. Compile modules first

```bash
gfortran -c mymodule.f90
gfortran mymodule.o main.f90
```

### 3. Check module visibility

```fortran
module mymod
  implicit none
  private :: secret
  public :: visible
end module
```

### 4. Break circular dependencies

```fortran
! Move shared types to a third module
module shared_types
end module
module a
  use shared_types
end module
module b
  use shared_types
end module
```

### 5. Use rename to avoid name clashes

```fortran
use module_a, only: func => func_name
use module_b, only: func => other_func
```

## Examples

Proper module usage:

```fortran
module math_mod
  implicit none
contains
  pure function square(x) result(y)
    real, intent(in) :: x
    real :: y
    y = x * x
  end function
end module

program main
  use math_mod, only: square
  implicit none
  print *, square(5.0)
end program
```

## Related Errors

- [Fortran Module Error](../fortran-module-error)
- [Fortran Interface Error](../fortran-interface-error)
- [Fortran Implicit None Error](../fortran-implicit-none-custom)
