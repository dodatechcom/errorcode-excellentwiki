---
title: "[Solution] Fortran Module Use — Module Import Errors"
description: "Fix Fortran module use errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1050
---

The `use` statement imports entities from a module. Errors involve using a name not defined in the module, circular module dependencies, or forgetting `use` for a required module.

## Common Causes

- Referencing a module procedure without a `use` statement
- Circular dependencies: module A uses module B which uses module A
- Using `only:` but forgetting the needed entity
- Module not compiled before the dependent program

## How to Fix

### 1. Import all or specific entities

```fortran
use my_module          ! everything
use my_module, only: func1, var2  ! specific
```

### 2. Avoid circular dependencies

```fortran
! WRONG: circular
module A
  use B
end module
module B
  use A
end module

! CORRECT: restructure
module C  ! shared types
end module
module A
  use C
end module
module B
  use C
end module
```

### 3. Compile modules before programs

```bash
gfortran -c mymodule.f90
gfortran mymodule.o main.f90
```

### 4. Use the only clause to avoid name clashes

```fortran
use module_a, only: func_a
use module_b, only: func_a => func_a_b  ! rename
```

### 5. Check module visibility (public/private)

```fortran
module mymod
  implicit none
  private :: secret
  public :: visible
  integer :: secret = 42
  integer :: visible = 10
end module
```

## Examples

A module dependency chain:

```fortran
module math_utils
  implicit none
  real, parameter :: PI = 3.14159265
contains
  function circle_area(r) result(area)
    real, intent(in) :: r
    real :: area
    area = PI * r**2
  end function
end module

program main
  use math_utils
  implicit none
  print *, circle_area(1.0)
end program
```

## Related Errors

- [Fortran Interface Error](../fortran-interface-error)
- [Fortran Module Error](../fortran-module-error)
- [Fortran Use Error](../fortran-use-error)
