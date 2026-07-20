---
title: "[Solution] Fortran Co-Array — Parallel Array Errors"
description: "Fix co-array errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1073
---

Co-arrays (Fortran 2008) enable single-program-multiple-data parallelism. Errors involve wrong co-index syntax, synchronization issues, or incorrect image count assumptions.

## Common Causes

- Using `[*]` syntax without compiling with co-array support
- Wrong co-index (image number) causing out-of-bounds access
- Missing `sync all` or `sync images` between remote accesses
- Assuming all images execute the same code path

## How to Fix

### 1. Compile with co-array support

```bash
# Intel Fortran
ifort -coarray=shmy coarrays.f90

# GCC (CoarrayFortran)
gfortran -fcoarray=single coarrays.f90
```

### 2. Use the correct co-array syntax

```fortran
real :: x[*]  ! one co-dimension per image
x = 0.0
if (this_image() == 1) then
  x = 42.0
end if
sync all
print *, 'Image', this_image(), ':', x
```

### 3. Use num_images() for bounds checking

```fortran
if (this_image() <= num_images()) then
  ! safe to access
end if
```

### 4. Synchronize after remote access

```fortran
real :: remote_val[*]
remote_val = this_image() * 10.0
sync all
print *, 'From image 1:', remote_val[1]
```

### 5. Use co-array allocatable arrays

```fortran
real, allocatable :: arr(:)[:]
allocate(arr(100)[*])
arr = this_image()
sync all
```

## Examples

Simple co-array parallel sum:

```fortran
program parallel_sum
  implicit none
  integer :: partial_sum[*]
  integer :: i, total

  partial_sum = this_image() ** 2
  sync all

  if (this_image() == 1) then
    total = 0
    do i = 1, num_images()
      total = total + partial_sum[i]
    end do
    print *, 'Total:', total
  end if
end program
```

## Related Errors

- [Fortran Do Concurrent](../fortran-do-concurrent)
- [Fortran Module Error](../fortran-module-error)
- [Fortran Runtime Error](../fortran-runtime-error)
