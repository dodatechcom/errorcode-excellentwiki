---
title: "[Solution] Fortran C_LOC and C_F_POINTER Error"
description: "Fix Fortran C_LOC and C_F_POINTER errors when interoperating with C pointers."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

C_LOC and C_F_POINTER errors occur when the C interoperability functions are called with non-target variables or incorrect types.

## Common Causes

- C_LOC on non-TARGET variable
- C_F_POINTER with incompatible shape
- C_LOC on allocatable without TARGET
- Missing ISO_C_BINDING import

## How to Fix

### 1. Ensure variable has TARGET attribute

```fortran
use iso_c_binding
real, target :: x
type(c_ptr) :: ptr
ptr = c_loc(x)  ! OK: x is TARGET
```

### 2. Match C_F_POINTER shape correctly

```fortran
use iso_c_binding
real, target :: arr(10)
type(c_ptr) :: c_ptr
real, pointer :: f_ptr(:)
c_ptr = c_loc(arr)
call c_f_pointer(c_ptr, f_ptr, [10])
```

## Examples

```fortran
program c_loc_demo
    use iso_c_binding
    implicit none
    integer, target :: value
    type(c_ptr) :: cptr
    value = 42
    cptr = c_loc(value)
    print *, 'C pointer created for value:', value
end program
```

## Related Errors

- [FFI error](/languages/fortran/fortran-external-error)
- [Pointer assignment error](/languages/fortran/fortran-pointer-assignment-error)
- [Runtime error](/languages/fortran/runtime-error11)
