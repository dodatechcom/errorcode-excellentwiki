---
title: "[Solution] Fortran NON_OVERRIDABLE Error"
description: "Fix Fortran NON_OVERRIDABLE attribute errors in type-bound procedure declarations."
languages: ["fortran"]
error-types: ["compile-error"]
severities: ["error"]
---

NON_OVERRIDABLE errors occur when the attribute is applied incorrectly or when a non-overridable procedure is called through a polymorphic variable.

## Common Causes

- NON_OVERRIDABLE on procedure that is overridden
- FINAL procedure marked as NON_OVERRIDABLE
- Calling non-overridable through class(*) variable
- Missing NON_OVERRIDABLE on FINAL procedures

## How to Fix

### 1. Use NON_OVERRIDABLE correctly

```fortran
type :: base_type
contains
    procedure, non_overridable :: fixed_method
end type
```

### 2. Do not override non-overridable

```fortran
type, extends(base_type) :: child_type
contains
    ! WRONG: Cannot override non_overridable
    ! procedure :: fixed_method => child_fixed

    ! CORRECT: Add new method
    procedure :: new_method => child_new
end type
```

## Examples

```fortran
program non_overridable_demo
    implicit none
    type :: animal
    contains
        procedure, non_overridable :: classify
    end type
    type(animal) :: a
    print *, a%classify()
    contains
    character(10) function classify(self)
        class(animal), intent(in) :: self
        classify = 'Unknown'
    end function
end program
```

## Related Errors

- [Type bound procedure error](/languages/fortran/fortran-type-bound-procedure)
- [Interface error](/languages/fortran/fortran-interface-error)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
