---
title: "[Solution] Fortran IMAGE_INDEX Error"
description: "Fix Fortran IMAGE_INDEX errors when converting between coarray indices and linear image numbers."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

IMAGE_INDEX errors occur when the function is called with invalid coarray or subscript arguments.

## Common Causes

- IMAGE_INDEX with wrong coarray variable
- Subscript array too small or too large
- Negative or zero image index
- IMAGE_INDEX called outside coarray context

## How to Fix

### 1. Use correct coarray reference

```fortran
integer :: img
img = image_index(coarray_var, [1, 1])
```

### 2. Validate subscript array

```fortran
integer :: sub(1)
sub = [3]
img = image_index(my_caf, sub)
```

## Examples

```fortran
program image_index_demo
    implicit none
    integer :: me, total_imgs
    me = this_image()
    total_imgs = num_images()
    print *, 'I am image', me, 'of', total_imgs
end program
```

## Related Errors

- [Coarray error](/languages/fortran/fortran-coarray)
- [Array bounds error](/languages/fortran/array-bounds)
- [Runtime error](/languages/fortran/runtime-error11)
