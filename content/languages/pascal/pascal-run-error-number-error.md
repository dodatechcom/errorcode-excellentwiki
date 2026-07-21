---
title: "[Solution] Pascal RUN ERROR Number Error"
description: "Fix Pascal RUNERROR procedure errors when triggering runtime errors with specific error codes."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

RUNERROR procedure errors occur when triggering runtime errors with invalid codes or when error handling does not catch the triggered error.

## Common Causes

- RUNERROR with invalid error code
- Error handler not installed with ON ERROR
- RUNERROR in nested try blocks
- Missing error code parameter

## How to Fix

### 1. Use valid error codes

```pascal
// WRONG: Invalid error code
RunError(9999);

// CORRECT: Use standard error codes
RunError(1);  // divide by zero
RunError(2);  // overflow
```

### 2. Handle with try/except

```pascal
try
  RunError(1);
except
  on E: Exception do
    WriteLn('Caught: ', E.Message);
end;
```

## Examples

```pascal
program RunErrorDemo;

begin
  try
    WriteLn('About to trigger error');
    RunError(1);
  except
    on E: Exception do
      WriteLn('Error caught: ', E.Message);
  end;
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Exception error](/languages/pascal/pascal-exception-error)
- [Try except error](/languages/pascal/pascal-try-except-error)
