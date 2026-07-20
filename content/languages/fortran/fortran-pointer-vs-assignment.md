---
title: "[Solution] Fortran Pointer Assignment — Pointer vs Target"
description: "Fix Fortran pointer assignment vs value assignment errors."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1129
---

Confusing pointer assignment (`=>`) with value assignment (`=`) is a common Fortran mistake. Using `=` on a pointer copies the value, while `=>` associates the pointer with a target.

## Common Causes

- Using `=` instead of `=>` for pointer association
- Using `=>` instead of `=` for value assignment to a pointer
- Pointer assignment to a non-target variable
- Forgetting that pointer assignment changes the pointer's association

## How to Fix

### 1. Use => for pointer association

```fortran
real, target :: x = 5.0
real, pointer :: p
p => x  ! p points to x
```

### 2. Use = for value assignment through pointer

```fortran
p => x
p = 10.0  ! changes x to 10.0
```

### 3. Do not use => on non-target variables

```fortran
real :: y
real, pointer :: q
q => y  ! WARNING: y is not a target
```

### 4. Use associated() to check pointer status

```fortran
if (associated(p)) print *, p
```

### 5. Nullify before use

```fortran
real, pointer :: p
nullify(p)
if (.not. associated(p)) print *, 'p is null'
```

## Examples

Pointer vs assignment:

```fortran
program ptr_demo
  implicit none
  real, target :: a = 1.0, b = 2.0
  real, pointer :: p1, p2

  p1 => a       ! p1 points to a
  p2 => b       ! p2 points to b
  p1 = p2       ! a becomes 2.0 (value assignment)
  print *, a, b  ! 2.0 2.0

  p1 => b       ! p1 now points to b
  p1 = 99.0     ! b becomes 99.0
  print *, b     ! 99.0
end program
```

## Related Errors

- [Fortran Pointer Association](../fortran-pointer-association)
- [Fortran Nullify](../fortran-nullify)
- [Fortran Target Attribute](../fortran-target-attribute)
