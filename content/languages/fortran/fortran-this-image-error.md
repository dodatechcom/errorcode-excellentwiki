---
title: "[Solution] Fortran THIS_IMAGE Error"
description: "Fix Fortran THIS_IMAGE errors when querying the current image index in coarray programs."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

THIS_IMAGE errors occur when the function is called with incorrect arguments or outside coarray context.

## Common Causes

- THIS_IMAGE with wrong coarray argument
- THIS_IMAGE outside parallel context
- Subscript arguments exceeding coarray bounds
- Missing coarray variable declaration

## How to Fix

### 1. Use THIS_IMAGE correctly

```fortran
integer :: me
me = this_image()  ! current image number
```

### 2. With specific coarray

```fortran
integer :: me
me = this_image(my_caf)
```

## Examples

```fortran
program this_image_demo
    implicit none
    integer :: me
    me = this_image()
    print *, 'Hello from image', me
end program
```

## Related Errors

- [Coarray error](/languages/fortran/fortran-coarray)
- [Array bounds error](/languages/fortran/array-bounds)
- [Runtime error](/languages/fortran/runtime-error11)
