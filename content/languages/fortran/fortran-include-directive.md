---
title: "[Solution] Fortran Include Directive — File Inclusion Errors"
description: "Fix Fortran include directive errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1080
---

The `include` directive copies text from another file into the source at compile time. Errors involve missing include files, wrong paths, or using `include` where a module `use` would be better.

## Common Causes

- The included file does not exist in the search path
- Using `include` for code that should be in a module
- Circular includes
- `include` is not part of the Fortran standard (it is a preprocessor directive)

## How to Fix

### 1. Check include paths

```bash
gfortran -I/path/to/includes myprog.f90
```

### 2. Use include for parameter files

```fortran
include 'params.f90'
! params.f90 contains:
! integer, parameter :: MAX_SIZE = 1000
! real, parameter :: PI = 3.14159265
```

### 3. Use modules instead of include for most cases

```fortran
! OLD (include)
include 'constants.f90'

! NEW (module)
use constants
```

### 4. Use include for Fortran 77 continuation lines

```fortran
      include 'legacy_code.f'
```

### 5. Check for platform-specific includes

```fortran
! Different compilers may search different paths
! Use -I or environment variables to set paths
```

## Examples

An include file for common declarations:

```fortran
! common_declarations.inc
integer, parameter :: DP = selected_real_kind(15)
integer, parameter :: MAX_ITER = 1000
real(DP), parameter :: TOLERANCE = 1.0e-12

! Main program
program simulation
  implicit none
  include 'common_declarations.inc'
  real(DP) :: x
  integer :: iter
  x = 0.0_DP
  do iter = 1, MAX_ITER
    x = x + 1.0_DP
  end do
  print *, x
end program
```

## Related Errors

- [Fortran Module Error](../fortran-module-error)
- [Fortran Parameter Attribute](../fortran-parameter-attribute)
- [Fortran Implicit None Error](../fortran-implicit-none-custom)
