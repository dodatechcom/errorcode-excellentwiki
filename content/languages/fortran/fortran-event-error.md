---
title: "[Solution] Fortran EVENT Construct Error"
description: "Fix Fortran EVENT construct errors when using coarray event synchronization in Fortran 2018."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

EVENT construct errors occur when EVENT POST or EVENT WAIT is used incorrectly with coarrays.

## Common Causes

- EVENT without coarray variable
- EVENT POST on non-existent event
- EVENT WAIT without matching POST
- Missing EVENT type declaration

## How to Fix

### 1. Declare and use EVENT correctly

```fortran
use iso_fortran_env, only: event_type
type(event_type) :: sync_event
event post(sync_event)  ! post event
event wait(sync_event)  ! wait for event
```

### 2. Ensure proper coarray context

```fortran
type(event_type) :: ev[*]
event post(ev)  ! from any image
event wait(ev)  ! on any image
```

## Examples

```fortran
program event_demo
    use iso_fortran_env, only: event_type
    implicit none
    type(event_type) :: ready
    event post(ready)
    event wait(ready)
    print *, 'Event synchronized'
end program
```

## Related Errors

- [Coarray error](/languages/fortran/fortran-coarray)
- [Runtime error](/languages/fortran/runtime-error11)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
