---
title: "[Solution] Fortran PROTECTED Attribute Error"
description: "Fix Fortran PROTECTED attribute errors when preventing modification of module variables."
languages: ["fortran"]
error-types: ["compile-error"]
severities: ["error"]
---

PROTECTED attribute errors occur when attempting to modify a protected variable from outside its defining module.

## Common Causes

- Modifying PROTECTED variable from another unit
- PROTECTED without POINTER (PROTECTED implies pointer association)
- Missing TARGET attribute on variable being protected
- PROTECTED on local variable

## How to Fix

### 1. Do not modify PROTECTED variables externally

```fortran
module my_mod
    implicit none
    integer, protected :: count = 0
end module

program main
    use my_mod
    ! WRONG: count = 10  ! error: protected
    print *, count  ! read only is OK
end program
```

### 2. Use PROTECTED with POINTER correctly

```fortran
module config
    implicit none
    real, pointer, protected :: settings => null()
end module
```

## Examples

```fortran
module protected_mod
    implicit none
    integer, protected :: public_value = 42
end module

program protected_demo
    use protected_mod
    implicit none
    print *, 'Protected value:', public_value
    ! public_value = 100  ! ERROR: protected
end program
```

## Related Errors

- [Module error](/languages/fortran/module-error)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Pointer assignment error](/languages/fortran/fortran-pointer-assignment-error)
