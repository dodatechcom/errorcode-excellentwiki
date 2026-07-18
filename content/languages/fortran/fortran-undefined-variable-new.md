---
title: "[Solution] Fortran: undefined variable or variable not declared"
description: "Fix Fortran undefined variable errors by enabling implicit none and declaring all variables."
languages: ["fortran"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An undefined variable error in Fortran means the compiler encountered a variable name that has not been declared in a type statement. Fortran historically allows implicit typing where variables starting with I through N are integers and others are reals. However, modern Fortran practice requires explicit declarations using `implicit none`. Without this directive, misspelled variable names silently create new variables of implicit types rather than producing errors, leading to subtle bugs.

## Why It Happens

The primary cause is omitting `implicit none` at the beginning of a program or subprogram unit. Without it, any undefined name is automatically typed by its starting letter, masking spelling errors and typos. Even with `implicit none`, a variable may be undefined if it is used before being assigned a value. Common scenarios include using a variable in an expression before any assignment, referencing a variable declared in a different scope that is not accessible, or misspelling a variable name so it does not match the declaration. Module variables that are not properly accessed with the `use` statement also appear undefined. Function return values used before the function is called may trigger this error.

## How to Fix It

**Always use implicit none:**

```fortran
! WRONG: no implicit none, typos silently create new variables
program bad_example
    integer :: count
    counnt = 42  ! Typo creates a new integer variable
end program

! CORRECT: implicit none catches the typo
program good_example
    implicit none
    integer :: count
    counnt = 42  ! Compiler error: counnt not declared
end program
```

**Declare all variables before use:**

```fortran
program declarations
    implicit none
    integer :: i, n
    real :: x, y, result
    character(len=20) :: name
    logical :: is_valid

    n = 10
    x = 3.14
    result = x * n
    print *, result
end program
```

**Check variable scoping and module usage:**

```fortran
module my_module
    implicit none
    integer, public :: shared_var
    integer, private :: secret_var  ! Not accessible outside module
end module

program main
    use my_module, only: shared_var
    implicit none
    ! secret_var is not available here
    print *, shared_var
end program
```

**Initialize variables before use:**

```fortran
program init_example
    implicit none
    integer :: sum_val, i
    sum_val = 0  ! Initialize before accumulation
    do i = 1, 10
        sum_val = sum_val + i
    end do
    print *, 'Sum =', sum_val
end program
```

**Check for typos in variable names:**

```fortran
program typo_check
    implicit none
    integer :: temperature
    temperature = 72
    ! Common typo: using temp instead of temperature
    ! print *, temp  ! Would cause compile error with implicit none
    print *, temperature
end program
```

## Common Mistakes

- Forgetting `implicit none` in subroutines and functions (not just the main program)
- Using different variable names in declarations and usage due to typos
- Not initializing variables before using them in calculations
- Assuming module variables are automatically available without the `use` statement
- Declaring a variable in one scope and expecting it to be visible in another

## Related Pages

- [Array bounds exceeded in Fortran](/languages/fortran/fortran-array-bounds-new)
- [Memory allocation failed in Fortran](/languages/fortran/fortran-allocate-error-v2)
- [Format descriptor error in Fortran](/languages/fortran/fortran-format-error-v2)
- [Compiler internal error in Fortran](/languages/fortran/fortran-compiler-error-new)
