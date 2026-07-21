---
title: "[Solution] Fortran REDUCE Intrinsic Error"
description: "Fix Fortran REDUCE intrinsic function errors when combining array elements with a binary operation."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

REDUCE intrinsic errors occur when the operation function has incorrect signature or when the array is empty without a identity element.

## Common Causes

- Operation function not matching expected signature
- Empty array without identity element
- REDUCE on non-array variable
- Wrong number of arguments to operation

## How to Fix

### 1. Define operation correctly

```fortran
function add(a, b) result(c)
    real, intent(in) :: a, b
    real :: c
    c = a + b
end function

result = reduce(array, add)
```

### 2. Provide identity for empty arrays

```fortran
result = reduce(array, add, identity=0.0)
```

## Examples

```fortran
program reduce_demo
    implicit none
    integer :: arr(5)
    integer :: total
    arr = [1, 2, 3, 4, 5]
    total = sum(arr)
    print *, 'Sum:', total
end program
```

## Related Errors

- [Array bounds error](/languages/fortran/array-bounds)
- [Runtime error](/languages/fortran/runtime-error11)
- [Interface error](/languages/fortran/fortran-interface-error)
