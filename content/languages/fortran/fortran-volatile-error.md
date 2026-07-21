---
title: "[Solution] Fortran VOLATILE Attribute Error"
description: "Fix Fortran VOLATILE attribute errors when declaring variables that may change outside program control."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

VOLATILE attribute errors occur when VOLATILE is incorrectly applied or when the compiler optimizes away reads from volatile variables.

## Common Causes

- VOLATILE on local variables without external modification
- Missing VOLATILE on variables modified by interrupts
- VOLATILE preventing optimization of hot loops
- VOLATILE with INTENT constraints

## How to Fix

### 1. Use VOLATILE for hardware/external variables

```fortran
real, volatile :: hw_register
! Compiler will not cache value
hw_register = read_hw_port()
```

### 2. Do not use VOLATILE unnecessarily

```fortran
! WRONG: VOLATILE on local variable
real, volatile :: temp  ! wasteful

! CORRECT: Only for external/hardware access
real, volatile :: timer_value
```

## Examples

```fortran
program volatile_demo
    implicit none
    integer, volatile :: counter
    counter = 0
    do while (counter < 10)
        counter = counter + 1
    end do
    print *, 'Final:', counter
end program
```

## Related Errors

- [Runtime error](/languages/fortran/runtime-error11)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Save attribute error](/languages/fortran/fortran-save-attribute)
