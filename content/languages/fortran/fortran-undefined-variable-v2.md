---
title: "[Solution] Fortran: undefined variable reference"
description: "Fix Fortran errors when variables are used before being defined or are out of scope."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Fortran undefined variable errors occur when a variable is referenced before being defined, or when IMPLICIT NONE is used and a variable hasn't been declared.

## Common Causes

- Missing IMPLICIT NONE statement
- Variable used before being assigned
- Typo in variable name
- Variable declared in wrong scope
- Missing USE statement for module variables

## How to Fix

```fortran
! WRONG: Using undeclared variable
program undefined_example
    value = 5  ! Implicit typing, may cause issues
    print *, value
end program
```

```fortran
! CORRECT: Explicit declarations with IMPLICIT NONE
program defined_example
    implicit none
    integer :: value
    value = 5
    print *, value
end program
```

```fortran
! WRONG: Variable from wrong scope
module my_module
    implicit none
    integer :: module_var = 10
end module

program main
    implicit none
    print *, module_var  ! Error: not accessible
end program
```

```fortran
! CORRECT: Use module properly
module my_module
    implicit none
    integer, public :: module_var = 10
end module

program main
    use my_module
    implicit none
    print *, module_var  ! OK
end program
```

```fortran
! CORRECT: Initialize before use
program safe_init
    implicit none
    integer :: x, y
    
    x = 0  ! Initialize
    y = 0  ! Initialize
    
    x = compute(x, y)
    print *, x
contains
    function compute(a, b) result(res)
        integer, intent(in) :: a, b
        integer :: res
        res = a + b
    end function
end program
```

```fortran
! CORRECT: Check for uninitialized variables
program check_init
    implicit none
    integer :: x
    
    x = 42  ! Assigned
    
    if (x == 0) then
        print *, 'Warning: variable may be uninitialized'
    end if
    
    print *, x
end program
```

## Related Errors

- [Array Bounds](fortran-array-bounds-v2) - index errors
- [I/O Error](fortran-io-error-v2) - file errors
- [Division by Zero](fortran-division-by-zero-v2) - arithmetic errors
