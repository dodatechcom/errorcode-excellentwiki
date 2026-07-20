---
title: "[Solution] Fortran Derived Type — Custom Type Errors"
description: "Fix Fortran derived type errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1054
---

Derived types let you define custom composite types. Errors involve missing components, wrong component access syntax, circular type references, or uninitialized type-bound procedure dispatchers.

## Common Causes

- Accessing a component that does not exist in the derived type
- Circular type definitions (type A contains type B which contains type A)
- Using `%` syntax on a non-derived-type variable
- Forgetting `type-bound` procedures for the type

## How to Fix

### 1. Define types with clear component declarations

```fortran
type :: point
  real :: x, y
end type

type :: line
  type(point) :: p1, p2
end type
```

### 2. Access components with the % operator

```fortran
type(point) :: p
p%x = 1.0
p%y = 2.0
print *, p%x, p%y
```

### 3. Use allocatable components for dynamic data

```fortran
type :: dynamic_array
  real, allocatable :: data(:)
end type

type(dynamic_array) :: arr
allocate(arr%data(100))
arr%data = 0.0
```

### 4. Initialize derived types with constructor syntax

```fortran
type(point) :: origin
origin = point(0.0, 0.0)  ! constructor syntax

! Or component-wise
origin%x = 0.0
origin%y = 0.0
```

### 5. Use type-bound procedures for methods

```fortran
type :: circle
  real :: radius
contains
  procedure :: area => circle_area
  procedure :: circumference => circle_circ
end type
```

## Examples

A complete derived type with bound procedures:

```fortran
module geometry
  implicit none
  type :: point
    real :: x, y
  contains
    procedure :: distance => point_distance
    procedure :: print => point_print
  end type

  interface point
    module procedure new_point
  end interface

contains
  function new_point(x, y) result(p)
    real, intent(in) :: x, y
    type(point) :: p
    p%x = x
    p%y = y
  end function

  function point_distance(self, other) result(d)
    class(point), intent(in) :: self, other
    real :: d
    d = sqrt((self%x - other%x)**2 + (self%y - other%y)**2)
  end function

  subroutine point_print(self)
    class(point), intent(in) :: self
    print *, '(', self%x, ',', self%y, ')'
  end subroutine
end module
```

## Related Errors

- [Fortran Type Bound Procedure](../fortran-type-bound-procedure)
- [Fortran Operator Overloading](../fortran-operator-overloading)
- [Fortran Derived Type Error](../fortran-derived-type-error)
