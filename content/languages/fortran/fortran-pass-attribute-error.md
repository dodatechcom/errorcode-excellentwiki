---
title: "[Solution] Fortran PASS Attribute Error"
description: "Fix Fortran PASS attribute errors when passing the implicit object to type-bound procedures."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

PASS attribute errors occur when the PASS attribute is incorrectly specified or when the passed-object argument is missing.

## Common Causes

- PASS with wrong argument position
- Missing passed-object argument in type-bound procedure call
- PASS(nopass) when procedure does not use object
- PASS on procedure that accesses wrong argument

## How to Fix

### 1. Specify PASS correctly

```fortran
type :: my_type
    integer :: value
contains
    procedure :: get_value => my_get_value
end type

function my_get_value(self) result(v)
    class(my_type), intent(in) :: self
    integer :: v
    v = self%value
end function
```

### 2. Use NOPASS when not needed

```fortran
type :: my_type
contains
    procedure :: static_method => my_static
    procedure, nopass :: helper => my_helper
end type
```

## Examples

```fortran
program pass_demo
    implicit none
    type :: point
        real :: x, y
    contains
        procedure :: distance
    end type
    type(point) :: p
    p%x = 1.0
    p%y = 2.0
    print *, 'Distance:', p%distance()
    contains
    real function distance(self)
        class(point), intent(in) :: self
        distance = sqrt(self%x**2 + self%y**2)
    end function
end program
```

## Related Errors

- [Type bound procedure error](/languages/fortran/fortran-type-bound-procedure)
- [Interface error](/languages/fortran/fortran-interface-error)
- [Runtime error](/languages/fortran/runtime-error11)
