---
title: "[Solution] Fortran: compiler internal error or segmentation fault"
description: "Fix Fortran compiler internal errors by reducing optimization and isolating problematic code."
languages: ["fortran"]
error-types: ["compile-time-error"]
severities: ["critical"]
weight: 5
---

## What This Error Means

A Fortran compiler internal error (ICE) occurs when the compiler itself encounters an unexpected condition during compilation and cannot proceed. This is distinct from a compilation error in user code and represents a bug in the compiler. A segmentation fault during compilation similarly indicates the compiler has accessed invalid memory. These errors may appear as `internal compiler error`, `segfault`, or `gfortran: internal compiler error`. They are rare but disruptive, often triggered by specific combinations of language features, optimization levels, or edge cases in the code.

## Why It Happens

Compiler internal errors are caused by bugs in the compiler's code generation, optimization passes, or type checking logic. Certain patterns in source code can trigger these bugs, such as complex derived type operations, deeply nested constructs, or specific uses of assumed-shape arrays with certain optimization flags. High optimization levels like `-O3` or `-Ofast` are more likely to trigger ICEs because they exercise more complex code transformations. Using very old compiler versions with newer language features can also cause internal errors. Large source files that stress the compiler's memory management may cause segfaults during compilation. Specific language extensions like Coarrays, OpenMP directives combined with certain constructs, or Fortran 2018 features may have incomplete compiler support.

## How to Fix It

**Reduce optimization level:**

```bash
# If compilation crashes at -O3, try lower levels
gfortran -O2 -c source.f90
gfortran -O1 -c source.f90
gfortran -O0 -c source.f90  # No optimization

# Try without problematic optimizations
gfortran -O2 -fno-tree-ter -c source.f90
```

**Isolate the problematic code:**

```fortran
! Comment out sections to find the trigger
! Start with the full file, then binary search
! by commenting out halves of the code

program isolate_bug
    implicit none
    ! Comment out complex sections one at a time
    ! to identify which code triggers the ICE
    integer :: i
    do i = 1, 100
        print *, i
    end do
end program
```

**Check for known compiler bugs:**

```bash
# Check compiler version
gfortran --version

# Search for known bugs
# https://gcc.gnu.org/bugzilla/  (for GFortran)
# https://software.intel.com/en-us/forums/intel-fortran-compilers  (for ifort)

# Try updating to the latest compiler version
sudo apt update && sudo apt install gfortran
```

**Simplify complex constructs:**

```fortran
! If complex derived types cause ICEs, simplify them
! WRONG: complex nested type with allocatable components
! type container
!     type(inner), allocatable :: items(:)
! end type

! CORRECT: simplify for compilation
type container
    real :: items(100)
end type
```

**Report the bug if reproducible:**

```bash
# Create a minimal reproducible example
# Save just the code that triggers the ICE
# Report to compiler maintainers with:
# - Compiler version and options
# - Operating system
# - Minimal source code that reproduces the issue


## Common Mistakes

- Assuming the error is in user code when it is actually a compiler bug
- Not trying different optimization levels before spending hours debugging source code
- Using bleeding-edge compiler versions that may have undiscovered bugs
- Combining multiple experimental compiler flags without testing each individually
- Not reporting reproducible compiler bugs to the development team

## Related Pages

- [Array bounds exceeded in Fortran](/languages/fortran/fortran-array-bounds-new)
- [Memory allocation failed in Fortran](/languages/fortran/fortran-allocate-error-new)
- [Floating point overflow in Fortran](/languages/fortran/fortran-overflow-new)
- [Divide by zero in Fortran](/languages/fortran/fortran-divide-by-zero-new)
