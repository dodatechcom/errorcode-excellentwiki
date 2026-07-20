---
title: "[Solution] Fortran Type Bound Procedure — Object Methods"
description: "Fix Fortran type-bound procedure errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1055
---

Type-bound procedures attach methods to derived types. Errors involve missing `pass` or `nopass` attributes, wrong procedure references, or using the wrong dispatch mechanism (polymorphic vs non-polymorphic).

## Common Causes

- Using `procedure :: method` without `pass` when the type should be passed
- Calling a type-bound procedure on an uninitialized polymorphic variable
- Forgetting the `class` keyword for the first argument in a `pass` procedure
- Circular references in type-bound procedure definitions

## How to Fix

### 1. Use pass (default) for methods that operate on the object

```fortran
type :: widget
  real :: value
contains
  procedure :: get_value => widget_get_value
end type

contains
  function widget_get_value(self) result(v)
    class(widget), intent(in) :: self
    real :: v
    v = self%value
  end function
```

### 2. Use nopass for static/factory methods

```fortran
type :: utility
contains
  procedure, nopass :: version => utility_version
end type

function utility_version() result(v)
  character(len=*), parameter :: v = "1.0"
end function
```

### 3. Call type-bound procedures with the % syntax

```fortran
type(widget) :: w
w%value = 42.0
print *, w%get_value()
```

### 4. Use class for polymorphic dispatch

```fortran
class(widget), allocatable :: w
allocate(widget :: w)
w%value = 10.0
print *, w%get_value()
```

### 5. Define abstract types with deferred procedures

```fortran
type, abstract :: shape
contains
  procedure(shape_area_iface), deferred :: area
end type

abstract interface
  function shape_area_iface(self) result(a)
    class(shape), intent(in) :: self
    real :: a
  end function
end interface
```

## Examples

A polymorphic shape hierarchy:

```fortran
module shapes
  implicit none
  type, abstract :: shape
  contains
    procedure(area_if), deferred :: area
    procedure :: describe => shape_describe
  end type

  type, extends(shape) :: circle
    real :: radius
  contains
    procedure :: area => circle_area
  end type

  type, extends(shape) :: rectangle
    real :: width, height
  contains
    procedure :: area => rect_area
  end type

  abstract interface
    function area_if(self) result(a)
      class(shape), intent(in) :: self
      real :: a
    end function
  end interface

contains
  function circle_area(self) result(a)
    class(circle), intent(in) :: self
    real :: a
    a = 3.14159 * self%radius**2
  end function

  function rect_area(self) result(a)
    class(rectangle), intent(in) :: self
    real :: a
    a = self%width * self%height
  end function

  subroutine shape_describe(self)
    class(shape), intent(in) :: self
    print *, 'Area:', self%area()
  end subroutine
end module
```

## Related Errors

- [Fortran Derived Type](../fortran-derived-type-custom)
- [Fortran Interface Error](../fortran-interface-error)
- [Fortran Pointer Association](../fortran-pointer-association)
