---
title: "[Solution] Fortran Allocatable Array — Dynamic Array Errors"
description: "Fix Fortran allocatable array errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1046
---

Allocatable arrays are dynamically sized and must be allocated before use. Errors involve using an unallocated array, allocating with wrong shape, or forgetting to deallocate.

## Common Causes

- Accessing an allocatable array before `allocate` (unallocated status)
- Allocating with a shape that does not match the assumed-shape interface
- Forgetting to `deallocate` (memory leak)
- Using `allocatable` with `intent(out)` without re-allocating in the callee

## How to Fix

### 1. Always allocate before use

```fortran
real, allocatable :: arr(:)
allocate(arr(10))
arr = 1.0
print *, sum(arr)
deallocate(arr)
```

### 2. Use status check with allocated()

```fortran
real, allocatable :: arr(:)
if (.not. allocated(arr)) then
  allocate(arr(10))
end if
```

### 3. Allocate with automatic shape from another variable

```fortran
subroutine copy(src, dst)
  real, intent(in) :: src(:)
  real, allocatable, intent(out) :: dst(:)
  allocate(dst(size(src)))
  dst = src
end subroutine
```

### 4. Use source= for allocation from an existing array

```fortran
real, allocatable :: a(:), b(:)
allocate(a(10), source=0.0)
allocate(b, source=a)  ! b gets same shape and values
```

### 5. Deallocate when done

```fortran
real, allocatable :: work(:)
allocate(work(1000))
! ... use work ...
deallocate(work)
```

## Examples

Dynamic array with automatic reallocation (Fortran 2003):

```fortran
program dynamic_example
  implicit none
  real, allocatable :: data(:)
  integer :: n

  n = 5
  allocate(data(n))
  data = [(real(i), i=1,n)]

  ! Reallocate to larger size
  n = 10
  allocate(data(n), source=0.0)  ! old values lost
  print *, size(data)
  deallocate(data)
end program
```

## Related Errors

- [Fortran Realloc Error](../fortran-realloc-error)
- [Fortran Deallocate Error](../fortran-deallocate-error)
- [Fortran Allocate Error](../fortran-allocate-error)
