---
title: "[Solution] Fortran ISO Fortran Env — Environment Constants"
description: "Fix iso_fortran_env errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1072
---

`iso_fortran_env` provides named constants for kind parameters and compiler information. Errors involve using constants that do not exist in older Fortran standards or wrong module usage.

## Common Causes

- Using `iso_fortran_env` constants not available in the target standard
- Confusing `real32`/`real64` (named kinds) with `selected_real_kind` results
- Missing `use iso_fortran_env` statement
- Using `input_unit`, `output_unit`, `error_unit` incorrectly

## How to Fix

### 1. Import the module

```fortran
use iso_fortran_env
```

### 2. Use named kind constants

```fortran
use iso_fortran_env

real(real32) :: single
real(real64) :: double
integer(int32) :: i32
integer(int64) :: i64
```

### 3. Use I/O unit constants

```fortran
use iso_fortran_env

write(output_unit, *) 'Hello'
write(error_unit, *) 'Error'
read(input_unit, *) n
```

### 4. Use compiler version information

```fortran
use iso_fortran_env

print *, 'Compiler version:', compiler_version()
print *, 'Compiler options:', compiler_options()
```

### 5. Check available features

```fortran
use iso_fortran_env

print *, 'Numeric storage size:', numeric_storage_size
print *, 'Character storage size:', character_storage_size
```

## Examples

A complete iso_fortran_env usage:

```fortran
program iso_demo
  use iso_fortran_env
  implicit none

  real(real64) :: pi = acos(1.0_real64)
  integer(int64) :: now

  print *, 'Double precision pi:', pi
  print *, 'Compiler:', compiler_version()

  write(output_unit, '(A, I0)') 'Numeric storage: ', numeric_storage_size
end program
```

## Related Errors

- [Fortran Kind Parameter](../fortran-kind-parameter)
- [Fortran Selected Int Kind](../fortran-selected-int-kind)
- [Fortran Implicit None Error](../fortran-implicit-none-custom)
