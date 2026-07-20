---
title: "[Solution] Fortran Operator Overloading — Custom Operators"
description: "Fix Fortran operator overloading errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1053
---

Fortran lets you overload operators (like `+`, `*`, `.dot.`) for derived types. Errors involve ambiguous overloads, wrong argument counts, or missing functions for required operators.

## Common Causes

- Overloading an operator with a function that takes the wrong number of arguments
- Ambiguous overloads where two functions have the same signature
- Using a custom operator without defining it first
- Overloading `=` (assignment) without the correct interface

## How to Fix

### 1. Define operator functions with correct argument count

```fortran
module vector_ops
  implicit none
  type :: vector
    real :: x, y, z
  end type

  interface operator(+)
    module procedure add_vectors
  end interface

contains
  function add_vectors(a, b) result(c)
    type(vector), intent(in) :: a, b
    type(vector) :: c
    c% x = a%x + b%x
    c%y = a%y + b%y
    c%z = a%z + b%z
  end function
end module
```

### 2. Define custom operators with dot notation

```fortran
interface operator(.cross.)
  module procedure cross_product
end interface

function cross_product(a, b) result(c)
  type(vector), intent(in) :: a, b
  type(vector) :: c
  c%x = a%y*b%z - a%z*b%y
  c%y = a%z*b%x - a%x*b%z
  c%z = a%x*b%y - a%y*b%x
end function
```

### 3. Avoid ambiguity by using distinct type signatures

```fortran
! Each operator function should have a unique argument pattern
function add_int(a, b) result(c)
  integer, intent(in) :: a, b
  integer :: c
  c = a + b
end function

function add_real(a, b) result(c)
  real, intent(in) :: a, b
  real :: c
  c = a + b
end function
```

### 4. Overload assignment with interface assignment

```fortran
interface assignment(=)
  module procedure assign_from_array
end interface

subroutine assign_from_array(arr, v)
  real, intent(in) :: arr(3)
  type(vector), intent(out) :: v
  v%x = arr(1); v%y = arr(2); v%z = arr(3)
end subroutine
```

### 5. Use only: to control operator availability

```fortran
use vector_ops, only: operator(+), vector
```

## Examples

A matrix type with overloaded operators:

```fortran
module matrix_mod
  implicit none
  type :: matrix2x2
    real :: a(2,2)
  end type

  interface operator(*)
    module procedure mat_mul
  end interface

contains
  function mat_mul(m1, m2) result(c)
    type(matrix2x2), intent(in) :: m1, m2
    type(matrix2x2) :: c
    c%a = matmul(m1%a, m2%a)
  end function
end module
```

## Related Errors

- [Fortran Generic Interface](../fortran-generic-interface)
- [Fortran Derived Type](../fortran-derived-type)
- [Fortran Type Bound Procedure](../fortran-type-bound-procedure)
