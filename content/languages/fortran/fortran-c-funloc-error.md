---
title: "[Solution] Fortran C_FUNLOC Error"
description: "Fix Fortran C_FUNLOC errors when passing Fortran procedures to C functions."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

C_FUNLOC errors occur when the function location is requested for a procedure that is not C-interoperable.

## Common Causes

- C_FUNLOC on non-C-interoperable procedure
- Procedure not declared with BIND(C)
- C_FUNLOC on internal procedure
- Missing ISO_C_BINDING

## How to Fix

### 1. Use BIND(C) on the procedure

```fortran
subroutine my_callback() bind(c)
    print *, 'Called from C'
end subroutine

type(c_funptr) :: fptr
fptr = c_funloc(my_callback)
```

### 2. Only use C_FUNLOC on external procedures

```fortran
! WRONG: Internal procedure
contains
    subroutine internal() bind(c)
    end subroutine
    ! fptr = c_funloc(internal)  ! may fail

! CORRECT: External procedure
```

## Examples

```fortran
program c_funloc_demo
    use iso_c_binding
    implicit none
    type(c_funptr) :: fptr
    fptr = c_funloc(my_func)
    print *, 'Function pointer created'
    contains
    subroutine my_func() bind(c)
        print *, 'C-callable function'
    end subroutine
end program
```

## Related Errors

- [FFI error](/languages/fortran/fortran-external-error)
- [Interface error](/languages/fortran/fortran-interface-error)
- [Runtime error](/languages/fortran/runtime-error11)
