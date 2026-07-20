---
title: "[Solution] Fortran Generic Interface — Overloaded Procedures"
description: "Fix Fortran generic interface errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1052
---

A generic interface provides a single procedure name that dispatches to different implementations based on argument types or shapes. Errors involve ambiguous generics, missing specific procedures, or wrong argument patterns.

## Common Causes

- Two specific procedures in a generic have overlapping signatures (ambiguous)
- The generic name shadows an intrinsic procedure
- Missing `interface` block for a generic name
- A specific procedure's signature does not match any generic pattern

## How to Fix

### 1. Define the generic interface with unique signatures

```fortran
module overloaded
  implicit none
contains
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

  interface add_module
    module procedure add_int, add_real
  end interface
end module
```

### 2. Avoid ambiguous generics

```fortran
! WRONG: ambiguous
interface bad_generic
  procedure :: f_int_arr, f_real_arr
end interface
! Both take real(:) and integer(:), but if signatures overlap, it's ambiguous
```

### 3. Use operator overloading carefully

```fortran
interface operator(+)
  module procedure add_vectors
end interface

function add_vectors(a, b) result(c)
  real, intent(in) :: a(:), b(:)
  real :: c(size(a))
  c = a + b
end function
```

### 4. Check for name shadowing

```fortran
! If your generic has the same name as an intrinsic, it shadows it
! Use only: to avoid surprises
```

### 5. List all specific procedures in the interface

```fortran
interface my_print
  module procedure print_int
  module procedure print_real
  module procedure print_array
end interface
```

## Examples

A complete generic module:

```fortran
module print_mod
  implicit none
contains
  subroutine print_int(x)
    integer, intent(in) :: x
    print *, 'Integer:', x
  end subroutine

  subroutine print_real(x)
    real, intent(in) :: x
    print *, 'Real:', x
  end subroutine

  subroutine print_str(s)
    character(len=*), intent(in) :: s
    print *, 'String:', s
  end subroutine

  interface my_print
    module procedure print_int, print_real, print_str
  end interface
end module
```

## Related Errors

- [Fortran Operator Overloading](../fortran-operator-overloading)
- [Fortran Interface Mismatch](../fortran-interface-mismatch)
- [Fortran Derived Type](../fortran-derived-type)
