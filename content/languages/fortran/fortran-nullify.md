---
title: "[Solution] Fortran Nullify — Nullifying Pointers"
description: "Fix Fortran nullify errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1057
---

`nullify` disassociates a pointer from its target. Errors involve forgetting to nullify, using a nullified pointer, or nullifying a non-pointer variable.

## Common Causes

- Forgetting to nullify after deallocation (dangling pointer)
- Nullifying a variable that is not a pointer
- Using `nullify` on a non-pointer in modern Fortran (use `=> null()` instead)
- Checking pointer status with `== null()` instead of `associated()`

## How to Fix

### 1. Nullify after deallocation

```fortran
real, pointer :: arr(:)
allocate(arr(10))
deallocate(arr)
nullify(arr)
```

### 2. Initialize pointers with null()

```fortran
real, pointer :: p
p => null()  ! modern alternative to nullify
```

### 3. Check association status with associated()

```fortran
if (associated(p)) then
  print *, p
end if
```

### 4. Do not nullify non-pointer variables

```fortran
real :: x
nullify(x)  ! ERROR: x is not a pointer
```

### 5. Use nullify for arrays of pointers

```fortran
type(node), pointer :: list(:)
allocate(list(10))
! ... use list ...
do i = 1, 10
  nullify(list(i)%next)
end do
```

## Examples

Safe pointer lifecycle:

```fortran
program pointer_lifecycle
  implicit none
  real, pointer :: p
  real, target :: x

  ! Initialize
  nullify(p)
  print *, associated(p)  ! false

  ! Associate
  x = 42.0
  p => x
  print *, associated(p)  ! true
  print *, p              ! 42.0

  ! Disassociate
  nullify(p)
  print *, associated(p)  ! false
end program
```

## Related Errors

- [Fortran Pointer Association](../fortran-pointer-association)
- [Fortran Deallocate Error](../fortran-deallocate-error)
- [Fortran Target Attribute](../fortran-target-attribute)
