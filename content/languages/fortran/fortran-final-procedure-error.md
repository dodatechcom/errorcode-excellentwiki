---
title: "[Solution] Fortran FINAL Procedure Error"
description: "Fix Fortran FINAL procedure errors when defining automatic deallocation or cleanup procedures."
languages: ["fortran"]
error-types: ["compile-error"]
severities: ["error"]
---

FINAL procedure errors occur when FINAL is not properly defined or when FINAL procedures access invalid data.

## Common Causes

- FINAL procedure missing or incorrectly declared
- FINAL on non-derived type
- FINAL procedure accessing finalized object after deallocation
- FINAL not called when expected

## How to Fix

### 1. Define FINAL correctly

```fortran
type :: resource
    integer :: handle
contains
    final :: cleanup_resource
end type

subroutine cleanup_resource(self)
    type(resource), intent(inout) :: self
    ! Cleanup code here
    self%handle = 0
end subroutine
```

### 2. Do not access object after FINAL

```fortran
subroutine cleanup(self)
    type(resource), intent(inout) :: self
    call close_handle(self%handle)
    ! Do not use self after this
end subroutine
```

## Examples

```fortran
program final_demo
    implicit none
    type :: managed_ptr
        integer, pointer :: data(:)
    contains
        final :: free_managed
    end type
    type(managed_ptr) :: obj
    allocate(obj%data(100))
    obj%data = 42
    print *, 'Allocated and assigned'
    contains
    subroutine free_managed(self)
        type(managed_ptr), intent(inout) :: self
        if (associated(self%data)) deallocate(self%data)
    end subroutine
end program
```

## Related Errors

- [Deallocate error](/languages/fortran/fortran-deallocate-error)
- [Memory leak](/languages/fortran/fortran-memory-error)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
