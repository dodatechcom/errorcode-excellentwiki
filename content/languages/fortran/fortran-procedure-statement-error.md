---
title: "[Solution] Fortran PROCEDURE Statement Error"
description: "Fix Fortran PROCEDURE statement errors when declaring procedure pointers or abstract interfaces."
languages: ["fortran"]
error-types: ["syntax-error"]
severities: ["error"]
---

PROCEDURE statement errors occur when procedure declarations have incorrect interface blocks or when procedure pointer initialization fails.

## Common Causes

- PROCEDURE without interface block
- Procedure pointer initialized to wrong signature
- Abstract interface not matching procedure
- PROCEDURE in wrong declaration section

## How to Fix

### 1. Provide proper interface

```fortran
procedure(my_interface), pointer :: proc_ptr
```

### 2. Initialize before use

```fortran
proc_ptr => my_actual_procedure
if (associated(proc_ptr)) then
    call proc_ptr()
end if
```

## Examples

```fortran
program procedure_statement_demo
    implicit none
    abstract interface
        function func_t(x) result(y)
            real, intent(in) :: x
            real :: y
        end function
    end interface
    procedure(func_t), pointer :: fptr
    fptr => my_function
    print *, fptr(2.0)
    contains
    real function my_function(x)
        real, intent(in) :: x
        my_function = x * 2.0
    end function
end program
```

## Related Errors

- [Interface error](/languages/fortran/fortran-interface-error)
- [Pointer assignment error](/languages/fortran/fortran-pointer-assignment-error)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
