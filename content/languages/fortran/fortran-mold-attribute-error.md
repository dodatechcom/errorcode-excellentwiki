---
title: "[Solution] Fortran MOLD Attribute Error"
description: "Fix Fortran MOLD attribute errors when allocating arrays with the mold keyword."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

MOLD attribute errors occur when the mold expression is not compatible with the allocatable variable.

## Common Causes

- Mold type does not match destination
- Mold shape causes unexpected allocation
- MOLD with non-allocatable variable
- MOLD on polymorphic types

## How to Fix

### 1. Match mold type to destination

```fortran
integer, allocatable :: arr(:)
integer :: template(10)
arr = template  ! allocates with size 10
```

### 2. Use mold for shape matching

```fortran
real, allocatable :: new_arr(:,:)
real :: existing(5,5)
allocate(new_arr, mold=existing)  ! allocates 5x5
new_arr = 0.0
```

## Examples

```fortran
program mold_demo
    implicit none
    real, allocatable :: source(:), target_arr(:)
    source = [1.0, 2.0, 3.0]
    allocate(target_arr, mold=source)
    target_arr = source * 2.0
    print *, 'Target:', target_arr
    deallocate(source, target_arr)
end program
```

## Related Errors

- [Allocatable error](/languages/fortran/fortran-allocatable-error)
- [Array shape mismatch](/languages/fortran/fortran-array-shape-mismatch)
- [Runtime error](/languages/fortran/runtime-error11)
