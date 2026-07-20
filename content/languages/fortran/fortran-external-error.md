---
title: "[Solution] Fortran External Attribute — External Procedure Declaration"
description: "Fix Fortran external attribute errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1132
---

The `external` attribute declares a procedure as external. Errors involve using external when a module use would be better, or forgetting external for procedures passed as arguments.

## Common Causes

- Passing a procedure as an argument without external declaration
- Using external when the procedure is already in a module
- External declaration conflicts with module procedure of same name
- Forgetting that external procedures lack automatic interfaces

## How to Fix

### 1. Declare procedures passed as arguments

```fortran
external :: my_func
call apply(my_func, 5.0)
```

### 2. Use interface blocks for external procedures

```fortran
interface
  function my_func(x) result(y)
    real, intent(in) :: x
    real :: y
  end function
end interface
```

### 3. Prefer module procedures over external

```fortran
module funcs
contains
  pure function my_func(x) result(y)
    real, intent(in) :: x
    real :: y
    y = x ** 2
  end function
end module
```

### 4. Use external for procedure arguments in Fortran 77 style

```fortran
subroutine apply(f, x)
  external :: f
  real, intent(in) :: x
  real :: result
  result = f(x)
  print *, result
end subroutine
```

### 5. Do not use external for module procedures

```fortran
use my_module
! Do NOT also declare: external :: my_module_func
```

## Examples

Using external with an interface:

```fortran
program external_demo
  implicit none
  interface
    function double_it(x) result(y)
      real, intent(in) :: x
      real :: y
    end function
  end interface
  external :: double_it

  print *, double_it(5.0)
end program

function double_it(x) result(y)
  real, intent(in) :: x
  real :: y
  y = x * 2.0
end function
```

## Related Errors

- [Fortran Interface Error](../fortran-interface-error)
- [Fortran Module Error](../fortran-module-error)
- [Fortran Pure Function](../fortran-pure-function)
