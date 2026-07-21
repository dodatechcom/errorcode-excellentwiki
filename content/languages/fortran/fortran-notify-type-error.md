---
title: "[Solution] Fortran NOTIFY TYPE Error"
description: "Fix Fortran NOTIFY_TYPE errors when using event notification for coarray synchronization."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

NOTIFY_TYPE errors occur when notification objects are used incorrectly or when NOTIFY is posted without matching WAIT.

## Common Causes

- NOTIFY without corresponding WAIT
- NOTIFY_TYPE variable not properly initialized
- NOTIFY on invalid image
- Missing STAT= for error handling

## How to Fix

### 1. Use NOTIFY and WAIT in pairs

```fortran
type(notify_type) :: my_notify
notify(my_notify)
wait(my_notify)
```

### 2. Initialize before use

```fortran
type(notify_type) :: sync
! Post notification
notify(sync)
! Wait for it
wait(sync)
```

## Examples

```fortran
program notify_demo
    implicit none
    integer :: me
    me = this_image()
    print *, 'Image', me, 'notify demo'
end program
```

## Related Errors

- [Coarray error](/languages/fortran/fortran-coarray)
- [Event error](/languages/fortran/fortran-event-error)
- [Runtime error](/languages/fortran/runtime-error11)
