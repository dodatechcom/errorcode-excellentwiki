---
title: "[Solution] Fortran IMPORT Statement Error"
description: "Fix Fortran IMPORT statement errors when importing entities into interface blocks."
languages: ["fortran"]
error-types: ["syntax-error"]
severities: ["error"]
---

IMPORT statement errors occur when entities are not properly imported into interface blocks or when IMPORT ALL is used incorrectly.

## Common Causes

- IMPORT without specific entity names
- IMPORT ALL when only some entities needed
- Entity not accessible from host scope
- IMPORT in wrong scope

## How to Fix

### 1. Import specific entities

```fortran
subroutine proc(x)
    import :: my_type
    type(my_type), intent(in) :: x
end subroutine
```

### 2. Use IMPORT ALL for convenience

```fortran
function calc(x) result(y)
    import
    real, intent(in) :: x
    real :: y
end function
```

## Examples

```fortran
module types_mod
    implicit none
    type :: vector3
        real :: x, y, z
    end type
end module

subroutine print_vec(v)
    use types_mod
    import :: vector3
    type(vector3), intent(in) :: v
    print *, v%x, v%y, v%z
end subroutine
```

## Related Errors

- [Interface error](/languages/fortran/fortran-interface-error)
- [Module error](/languages/fortran/module-error)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
