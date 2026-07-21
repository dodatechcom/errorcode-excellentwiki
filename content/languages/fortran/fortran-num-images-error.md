---
title: "[Solution] Fortran NUM_IMAGES Error"
description: "Fix Fortran NUM_IMAGES errors when querying the number of active images in a coarray program."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

NUM_IMAGES errors occur when the function returns unexpected values or when used in non-coarray context.

## Common Causes

- NUM_IMAGES called without coarray support
- NUM_IMAGES returning 1 in serial execution
- Using NUM_IMAGES before image setup
- NUM_IMAGES with invalid TEAM argument

## How to Fix

### 1. Check coarray support

```fortran
integer :: n
n = num_images()  ! returns 1 in serial
```

### 2. Use for load balancing

```fortran
integer :: me, n
me = this_image()
n = num_images()
do i = me, work_size, n
    call process(i)
end do
```

## Examples

```fortran
program num_images_demo
    implicit none
    print *, 'Running on', num_images(), 'image(s)'
    print *, 'I am image', this_image()
end program
```

## Related Errors

- [Coarray error](/languages/fortran/fortran-coarray)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Runtime error](/languages/fortran/runtime-error11)
