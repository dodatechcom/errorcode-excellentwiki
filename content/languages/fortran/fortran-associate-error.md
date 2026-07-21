---
title: "[Solution] Fortran ASSOCIATE Error"
description: "Fix Fortran ASSOCIATE construct errors when creating variable associations for complex expressions."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

ASSOCIATE errors occur when the associated expression is not valid or when the association target is modified during the construct.

## Common Causes

- ASSOCIATE with non-existent variable
- Modifying the original variable inside ASSOCIATE
- ASSOCIATE with non-associatable expression
- Selector is not a variable or expression

## How to Fix

### 1. Use valid expressions

```fortran
associate(x => array(i))
    x = x + 1  ! modifies array(i)
end associate
```

### 2. Do not modify selector inside ASSOCIATE

```fortran
associate(alias => some_var)
    ! WRONG: Modifying alias changes some_var
    ! alias = 0

    ! CORRECT: Use for read-only
    print *, alias
end associate
```

## Examples

```fortran
program associate_demo
    implicit none
    real :: values(3) = [1.0, 2.0, 3.0]
    associate(v => values(2))
        print *, 'Before:', v
        v = 10.0
        print *, 'After:', v
    end associate
    print *, 'Array:', values
end program
```

## Related Errors

- [Pointer assignment error](/languages/fortran/fortran-pointer-assignment-error)
- [Runtime error](/languages/fortran/runtime-error11)
- [Undefined variable](/languages/fortran/undefined-variable)
