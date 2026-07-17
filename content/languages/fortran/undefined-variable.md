---
title: "Undefined variable"
description: "An undefined variable error occurs when a Fortran program references a variable that has not been declared."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An undefined variable error occurs when the Fortran compiler encounters a variable name that has not been declared in a type statement or via implicit typing rules. When `implicit none` is used, all variables must be explicitly declared. Without `implicit none`, Fortran applies default implicit typing (I-N are `real`, everything else is `integer`), which can mask true typos.

## Common Causes

- Typo in a variable name
- Missing `implicit none` combined with misspelled variable names creating new variables
- Variable declared in a different scope (e.g., local to another subroutine)
- Using a variable before its `type` statement in the declaration section

## How to Fix

```fortran
! WRONG: Missing declaration
program bad_example
    implicit none
    x = 5.0           ! ERROR: x is not declared
    print *, x
end program

! CORRECT: Declare all variables
program good_example
    implicit none
    real :: x
    x = 5.0
    print *, x
end program
```

```fortran
! WRONG: Typo creates a new variable instead of using the intended one
program typo_example
    implicit none
    real :: temperature, result
    temperature = 98.6
    result = temprature + 1.0   ! typo: 'temprature' instead of 'temperature'
    print *, result              ! result is 1.0, not 99.6
end program

! CORRECT: Double-check variable names
program fixed_example
    implicit none
    real :: temperature, result
    temperature = 98.6
    result = temperature + 1.0
    print *, result              ! correct: 99.6
end program
```

## Examples

```fortran
program undefined_var_example
    implicit none
    integer :: count, total

    total = 0
    do count = 1, 10
        totla = totla + count    ! typo: totla instead of total
    end do

    ! With implicit none, this produces:
    ! Error: Symbol 'totla' is undeclared

    ! Without implicit none, totla would silently be created
    ! as a separate real variable with implicit typing
    print *, 'Total:', total     ! prints 0, not 55
end program
```

## Related Errors

- [Format error](/languages/fortran/format-error2)
- [Runtime error](/languages/fortran/runtime-error11)
