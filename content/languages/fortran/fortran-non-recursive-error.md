---
title: "[Solution] Fortran NON_RECURSIVE Error"
description: "Fix Fortran NON_RECURSIVE procedure errors when preventing recursive calls to subroutines."
languages: ["fortran"]
error-types: ["compile-error"]
severities: ["error"]
---

NON_RECURSIVE errors occur when the attribute is applied incorrectly or when a non-recursive procedure is called recursively.

## Common Causes

- NON_RECURSIVE procedure called recursively
- Missing NON_RECURSIVE on intended non-recursive procedures
- NON_RECURSIVE with SAVE attribute
- Stack overflow from unbounded recursion

## How to Fix

### 1. Mark procedures as NON_RECURSIVE

```fortran
subroutine process(n) non_recursive
    integer, intent(in) :: n
    ! This procedure cannot call itself
end subroutine
```

### 2. Prevent recursion explicitly

```fortran
subroutine traverse(node)
    integer, intent(in) :: node
    if (node > 0) then
        call traverse(left_child(node))  ! recursion!
    end if
end subroutine
```

## Examples

```fortran
program non_recursive_demo
    implicit none
    call factorial_iterative(5)
    contains
    subroutine factorial_iterative(n) non_recursive
        integer, intent(in) :: n
        integer :: i, result
        result = 1
        do i = 1, n
            result = result * i
        end do
        print *, n, '!=', result
    end subroutine
end program
```

## Related Errors

- [Subroutine error](/languages/fortran/subroutine)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Runtime error](/languages/fortran/runtime-error11)
