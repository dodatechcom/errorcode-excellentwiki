---
title: "[Solution] Fortran Pointer Association — Pointer Errors"
description: "Fix Fortran pointer errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1056
---

Fortran pointers are associated with targets via `=>`. Errors involve using an unassociated pointer, pointer association with a non-target, or memory leaks from dangling pointers.

## Common Causes

- Using a pointer before it is associated (status is undefined)
- Associating a pointer with a non-target variable
- Dangling pointer: target goes out of scope but pointer remains
- Pointer aliasing causing unintended side effects

## How to Fix

### 1. Always nullify or associate before use

```fortran
real, pointer :: p
nullify(p)
! or
p => null()
```

### 2. Only point to TARGET variables

```fortran
real, target :: x
real, pointer :: p
p => x  ! OK: x is a target

real :: y
p => y  ! WRONG: y is not a target
```

### 3. Check pointer association with associated()

```fortran
real, pointer :: p
if (associated(p)) then
  print *, p
else
  print *, 'pointer not associated'
end if
```

### 4. Nullify pointers when target is deallocated

```fortran
real, pointer :: arr(:)
allocate(arr(10))
arr = 1.0
deallocate(arr)
nullify(arr)  ! prevents dangling pointer
```

### 5. Use pointer assignment carefully

```fortran
real, target :: a(10), b(10)
real, pointer :: p(:)
p => a
p(1:5) => b(1:6:2)  ! partial association
```

## Examples

Linked list with pointers:

```fortran
module linked_list
  implicit none
  type :: node
    integer :: value
    type(node), pointer :: next => null()
  end type

contains
  function create_node(val) result(n)
    integer, intent(in) :: val
    type(node), pointer :: n
    allocate(n)
    n%value = val
    n%next => null()
  end function
end module
```

## Related Errors

- [Fortran Nullify Error](../fortran-nullify)
- [Fortran Deallocate Error](../fortran-deallocate-error)
- [Fortran Target Attribute](../fortran-target-attribute)
