---
title: "[Solution] Fortran BLOCK Construct Error"
description: "Fix Fortran BLOCK construct errors when declaring local variables within executable code."
languages: ["fortran"]
error-types: ["syntax-error"]
severities: ["error"]
---

BLOCK construct errors occur when BLOCK is used incorrectly or when variable declarations inside BLOCK conflict with outer scope.

## Common Causes

- Variable name conflict between BLOCK and outer scope
- BLOCK without matching END BLOCK
- Invalid declaration inside BLOCK
- BLOCK in wrong context

## How to Fix

### 1. Avoid name conflicts

```fortran
block
    integer :: temp  ! new variable
    temp = 42
    print *, temp
end block
```

### 2. Use BLOCK for scoped declarations

```fortran
do i = 1, 10
    block
        real :: local_sum
        local_sum = real(i)
        print *, local_sum
    end block
end do
```

## Examples

```fortran
program block_demo
    implicit none
    integer :: i
    do i = 1, 5
        block
            integer :: square
            square = i * i
            print *, i, 'squared =', square
        end block
    end do
end program
```

## Related Errors

- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Variable error](/languages/fortran/undefined-variable)
- [Syntax error](/languages/fortran/fortran-format-error)
