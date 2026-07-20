---
title: "[Solution] Fortran Common Block — Legacy Shared Memory"
description: "Fix Fortran common block errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["warning"]
weight: 1060
---

Common blocks share variables between program units without modules. They are a legacy feature that can cause subtle bugs from misaligned declarations.

## Common Causes

- Mismatched declarations of the same common block in different program units
- Different ordering of variables in the common block across units
- Using common blocks when modules would be safer
- Overlapping common blocks (a Fortran extension)

## How to Fix

### 1. Ensure identical declarations across all units

```fortran
! In main.f90
common /data/ n, x, arr
integer n
real x, arr(10)

! In sub.f90 — must match exactly
common /data/ n, x, arr
integer n
real x, arr(10)
```

### 2. Use modules instead of common blocks

```fortran
module data_module
  implicit none
  integer :: n
  real :: x
  real :: arr(10)
end module

! Then use data_module in all program units
```

### 3. Use block construct for local common blocks

```fortran
block
  common /local_data/ temp
  real :: temp
end block
```

### 4. Avoid common blocks in new code

```fortran
! OLD (bad)
common /config/ max_iter, tol

! NEW (good)
module config_mod
  implicit none
  integer, parameter :: max_iter = 1000
  real, parameter :: tol = 1.0e-6
end module
```

### 5. Use save for common block persistence

```fortran
common /state/ counter
integer counter
save /state/  ! explicit save
```

## Examples

Migrating from common to module:

```fortran
! BEFORE: common block
common /globals/ pi, gravity
real pi, gravity
data pi /3.14159/, gravity /9.81/

! AFTER: module
module globals
  implicit none
  real, parameter :: pi = 3.14159
  real, parameter :: gravity = 9.81
end module
```

## Related Errors

- [Fortran Module Error](../fortran-module-error)
- [Fortran Data Statement](../fortran-data-statement)
- [Fortran Save Attribute](../fortran-save-attribute)
