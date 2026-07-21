---
title: "[Solution] Fortran ITERATOR Error"
description: "Fix Fortran ITERATOR construct errors when using custom iteration over data structures."
languages: ["fortran"]
error-types: ["syntax-error"]
severities: ["error"]
---

ITERATOR construct errors occur when the ITERATE construct is used incorrectly or when iterator procedures have wrong signatures.

## Common Causes

- ITERATE on non-iterable type
- Missing ITERATOR procedure definition
- Iterator not returning proper status
- ITERATE in wrong context

## How to Fix

### 1. Define iterator properly

```fortran
type :: container
    integer :: values(10)
    integer :: current
contains
    procedure :: next
end type

function next(self, val) result(more)
    class(container), intent(inout) :: self
    integer, intent(out) :: val
    logical :: more
    if (self%current <= 10) then
        val = self%values(self%current)
        self%current = self%current + 1
        more = .true.
    else
        more = .false.
    end if
end function
```

## Examples

```fortran
program iterator_demo
    implicit none
    integer :: i
    do i = 1, 5
        print *, 'Item:', i
    end do
end program
```

## Related Errors

- [Type bound procedure error](/languages/fortran/fortran-type-bound-procedure)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Runtime error](/languages/fortran/runtime-error11)
