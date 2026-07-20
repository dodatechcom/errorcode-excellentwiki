---
title: "[Solution] Fortran Namelist — Namelist I/O Errors"
description: "Fix Fortran namelist errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1059
---

Namelist I/O reads/writes variable values in a special format. Errors involve incorrect namelist syntax, wrong variable names in the input, or type mismatches between the namelist and input data.

## Common Causes

- Variable name in input file does not match the namelist definition
- Wrong type in input (e.g., string where integer expected)
- Missing or extra commas/whitespace in namelist input
- Reading a namelist from a file not opened with proper format

## How to Fix

### 1. Define the namelist correctly

```fortran
integer :: n
real :: x
character(len=20) :: name
namelist /params/ n, x, name
```

### 2. Open the file and read the namelist

```fortran
open(unit=10, file='input.nml', status='old')
read(10, nml=params)
close(10)
```

### 3. Use correct input syntax

```
&params
  n = 42
  x = 3.14
  name = "test"
/
```

### 4. Write namelists for output

```fortran
open(unit=20, file='output.nml')
write(20, nml=params)
close(20)
```

### 5. Check for errors with iostat

```fortran
integer :: ierr
read(10, nml=params, iostat=ierr)
if (ierr /= 0) then
  print *, 'Namelist read error:', ierr
end if
```

## Examples

A complete namelist example:

```fortran
program namelist_example
  implicit none
  integer :: iterations = 100
  real :: tolerance = 1.0e-6
  logical :: verbose = .false.
  character(len=80) :: output_file = 'result.dat'

  namelist /control/ iterations, tolerance, verbose, output_file

  ! Read from stdin
  read(*, nml=control)
  print *, 'Iterations:', iterations
  print *, 'Tolerance:', tolerance
  print *, 'Verbose:', verbose
  print *, 'Output:', trim(output_file)
end program
```

## Related Errors

- [Fortran IO Error](../fortran-io-error)
- [Fortran Format Error](../fortran-format-error)
- [Fortran Read Error](../fortran-read-error)
