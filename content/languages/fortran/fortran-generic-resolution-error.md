---
title: "[Solution] Fortran GENERIC Resolution Error"
description: "Fix Fortran GENERIC interface resolution errors when multiple specific procedures match a call."
languages: ["fortran"]
error-types": ["compile-error"]
severities: ["error"]
---

GENERIC resolution errors occur when a generic interface has ambiguous specific procedures or when no specific procedure matches.

## Common Causes

- Multiple specific procedures with same argument types
- No specific procedure matches the call
- Generic name conflicts with inherited procedures
- Ambiguous resolution between generic procedures

## How to Fix

### 1. Ensure unique specific procedures

```fortran
interface my_overload
    module procedure int_add
    module procedure real_add
end interface
```

### 2. Avoid ambiguous signatures

```fortran
! WRONG: Ambiguous
! procedure :: func_int_int
! procedure :: func_real_int  ! if int and real are same kind

! CORRECT: Distinct signatures
procedure :: func_int
procedure :: func_real
procedure :: func_string
```

## Examples

```fortran
program generic_demo
    implicit none
    print *, add_int(1, 2)
    print *, add_real(1.0, 2.0)
    contains
    integer function add_int(a, b)
        integer, intent(in) :: a, b
        add_int = a + b
    end function
    real function add_real(a, b)
        real, intent(in) :: a, b
        add_real = a + b
    end function
end program
```

## Related Errors

- [Interface error](/languages/fortran/fortran-interface-error)
- [Generic interface error](/languages/fortran/fortran-generic-interface)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
