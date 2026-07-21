---
title: "[Solution] Fortran SOURCE Attribute Error"
description: "Fix Fortran SOURCE attribute errors when allocating arrays with source keyword."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

SOURCE attribute errors occur when the source expression is not compatible with the allocatable variable.

## Common Causes

- Source shape does not match destination
- Source type incompatible with destination
- SOURCE with non-allocatable expression
- SOURCE on character arrays with wrong length

## How to Fix

### 1. Ensure type and shape match

```fortran
integer, allocatable :: arr(:)
integer :: template(5)
template = [1, 2, 3, 4, 5]
allocate(arr, source=template)  ! OK: same type
```

### 2. Use correct source expression

```fortran
real, allocatable :: matrix(:,:)
real :: template(3,3)
template = 0.0
allocate(matrix, source=template)
```

## Examples

```fortran
program source_demo
    implicit none
    integer, allocatable :: original(:), copy(:)
    original = [10, 20, 30, 40, 50]
    allocate(copy, source=original)
    print *, 'Copy:', copy
    deallocate(original, copy)
end program
```

## Related Errors

- [Allocatable error](/languages/fortran/fortran-allocatable-error)
- [Array shape mismatch](/languages/fortran/fortran-array-shape-mismatch)
- [Runtime error](/languages/fortran/runtime-error11)
