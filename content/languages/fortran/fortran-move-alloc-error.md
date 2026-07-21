---
title: "[Solution] Fortran MOVE_ALLOC Error"
description: "Fix Fortran MOVE_ALLOC intrinsic errors when transferring allocation between allocatable arrays."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

MOVE_ALLOC errors occur when the source is not allocated or when the destination is already allocated without proper deallocation.

## Common Causes

- Source not allocated when MOVE_ALLOC called
- Destination already allocated without MOVE_ALLOC
- MOVE_ALLOC with non-allocatable arguments
- Status check not performed after MOVE_ALLOC

## How to Fix

### 1. Check allocation before move

```fortran
if (allocated(source)) then
    call move_alloc(source, dest)
end if
```

### 2. Let MOVE_ALLOC handle deallocation

```fortran
! WRONG: Deallocate before move
deallocate(dest)
call move_alloc(source, dest)

! CORRECT: MOVE_ALLOC handles it
call move_alloc(source, dest)  ! dest is auto-deallocated
```

## Examples

```fortran
program move_alloc_demo
    implicit none
    integer, allocatable :: src(:), dst(:)
    allocate(src(100))
    src = 42
    call move_alloc(src, dst)
    if (allocated(dst)) print *, 'Dest allocated, size:', size(dst)
    if (.not. allocated(src)) print *, 'Source deallocated'
    deallocate(dst)
end program
```

## Related Errors

- [Allocatable error](/languages/fortran/fortran-allocatable-error)
- [Deallocate error](/languages/fortran/fortran-deallocate-error)
- [Runtime error](/languages/fortran/runtime-error11)
