---
title: "[Solution] HRESULT S_FALSE (0x00000001) — Operation Successful but False"
description: "Understand Windows HRESULT S_FALSE (0x00000001). Why a successful HRESULT returns a non-zero value and how to handle it."
platforms: ["windows"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["hresult", "s-false", "0x00000001", "success-false", "com"]
weight: 5
---

# HRESULT S_FALSE (0x00000001) — Operation Successful but False

**Error Code:** `0x00000001`

S_FALSE is a success code (severity bit = 0) that indicates the operation completed successfully but returned a FALSE condition. It is not technically an error but a non-standard success value.

## What This Error Means

S_FALSE has the severity bit set to 0, meaning the operation succeeded. However, the value 1 (instead of 0) conveys additional semantic meaning: the operation completed but the result is "false" or "no match." `SUCCEEDED()` macros will return true for this code, but code checking for `S_OK` specifically will miss it.

## Common Causes

- Enumeration methods returning "no more items" or "end of list"
- Boolean operations that completed but returned FALSE
- Conditional checks that passed but yielded a negative result
- COM methods using S_FALSE to signal "not applicable" or "not found" without failing

## How to Fix

### Use SUCCEEDED Macro Correctly

```cpp
hr = pEnum->Next(1, &item, &fetched);
if (SUCCEEDED(hr)) {
    if (hr == S_OK) {
        // Item retrieved successfully
    } else if (hr == S_FALSE) {
        // No more items to enumerate
    }
}
```

### Check for Both S_OK and S_FALSE

```cpp
if (hr == S_OK || hr == S_FALSE) {
    // Operation succeeded, check result value
}
```

### Do Not Treat as Error

```cpp
// Wrong: treating S_FALSE as error
if (hr != S_OK) { /* error handling */ }

// Correct: check specifically for failure
if (FAILED(hr)) { /* error handling */ }
```

## Related Errors

- [E_FAIL (0x80004005)]({{< relref "/os/windows/hresult-e-fail" >}}) — General failure, the error counterpart to S_FALSE
- [E_ABORT (0x80004004)]({{< relref "/os/windows/hresult-e-abort" >}}) — Operation aborted, an error state
- [E_NOTIMPL (0x80004001)]({{< relref "/os/windows/hresult-e-notimpl" >}}) — Not implemented, may be returned alongside S_FALSE enumerations
