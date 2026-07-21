---
title: "[Solution] Fortran COARRAY Error"
description: "Fix Fortran coarray communication errors including image isolation and synchronization issues."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

Coarray errors occur when image indexing is incorrect, sync operations fail, or coarray variables are accessed from wrong images.

## Common Causes

- Image index out of range
- Missing SYNC IMAGES after coarray operation
- Coarray not allocated on remote image
- Accessing coarray before SYNC

## How to Fix

### 1. Check image index bounds

```fortran
integer :: me, n
me = this_image()
n = num_images()
if (me >= 1 .and. me <= n) then
    ! safe to proceed
end if
```

### 2. Use SYNC IMAGES properly

```fortran
sync images(*)
```

## Examples

```fortran
program coarray_demo
    implicit none
    integer :: me, n
    me = this_image()
    n = num_images()
    print *, 'Image', me, 'of', n
    sync images(*)
    if (me == 1) print *, 'All images synchronized'
end program
```

## Related Errors

- [Array bounds error](/languages/fortran/array-bounds)
- [Runtime error](/languages/fortran/runtime-error11)
- [Undefined variable](/languages/fortran/undefined-variable)
