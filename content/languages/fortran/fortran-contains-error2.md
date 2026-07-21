---
title: "[Solution] Fortran CONTAINS Error"
description: "Fix Fortran CONTAINS statement errors when defining internal procedures within a program unit."
languages: ["fortran"]
error-types: ["syntax-error"]
severities: ["error"]
---

CONTAINS errors occur when internal procedures are incorrectly defined or when CONTAINS is placed in the wrong position.

## Common Causes

- CONTAINS placed before specification statements
- Internal procedure accessing host variables without HOST association
- Missing END statement for internal procedure
- CONTAINS used in wrong program unit

## How to Fix

### 1. Place CONTAINS correctly

```fortran
program my_prog
    implicit none
    integer :: x
    ! specification statements here
    contains
    subroutine my_sub()
        x = 10  ! host association
    end subroutine
end program
```

### 2. Ensure proper scope

```fortran
subroutine parent()
    implicit none
    integer :: counter
    counter = 0
    contains
    subroutine increment()
        counter = counter + 1  ! host association
    end subroutine
end subroutine
```

## Examples

```fortran
program contains_demo
    implicit none
    integer :: value
    value = 42
    call show_value()
    contains
    subroutine show_value()
        print *, 'Value:', value
    end subroutine
end program
```

## Related Errors

- [Module error](/languages/fortran/module-error)
- [Subroutine error](/languages/fortran/subroutine)
- [Implicit none error](/languages/fortran/implicit-none-error)
